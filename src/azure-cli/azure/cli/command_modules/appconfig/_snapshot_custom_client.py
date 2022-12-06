from azure.appconfiguration import AzureAppConfigurationClient
from enum import Enum
from azure.appconfiguration import _models
from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict
from azure.core.exceptions import ClientAuthenticationError, ResourceExistsError, ResourceNotFoundError, HttpResponseError, map_error
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer
from typing import Dict, List, Optional, Any
from _snapshotmodels import Snapshot, SnapshotListResult
import json



class RequestMethod(Enum):
    GET = "GET"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


_ERROR_MAP = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError
        }


def _build_request(
    template_url_default: str,
    method: str,
    *,
    path_arguments: dict[str] = {},
    if_match: Optional[str] = None,
    if_none_match: Optional[str] = None,
    sync_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", "2022-11-01-preview")  # type: str
    accept = _headers.pop(
        "Accept", "application/vnd.microsoft.appconfig.keyset+json, application/json, application/problem+json"
    )

     # Construct URL
    _url = kwargs.pop("template_url", template_url_default)
    _url = _format_url_section(_url, **path_arguments)

    _serializer = Serializer()
    
    # Construct parameters
    _params["api-version"] = _serializer.query("api_version", api_version, "str")
   
    # Construct headers
    if sync_token is not None:
        _headers["Sync-Token"] = _serializer.header("sync_token", sync_token, "str")

    if if_match is not None:
        _headers["If-Match"] = _serializer.header("if_match", if_match, "str")
    if if_none_match is not None:
        _headers["If-None-Match"] = _serializer.header("if_none_match", if_none_match, "str")

    _headers["Accept"] = _serializer.header("accept", accept, "str")

    return HttpRequest(method=method.upper(), url=_url, params=_params, headers=_headers, **kwargs)


# Requests
def build_get_snapshot_request(
    name: str,
    if_match: Optional[str] = None,
    if_none_match: Optional[str] = None,
    sync_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    return _build_request(
        "/snapshots/{name}",
        RequestMethod.GET.value,
        path_arguments={"name": name},
        if_match=if_match,
        if_none_match=if_none_match,
        sync_token=sync_token,
        **kwargs
    )


def build_list_snapshots_request(
    sync_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    return _build_request(
        "/snapshots",
        RequestMethod.GET.value,
        sync_token=sync_token,
        **kwargs
    )


def build_status_update_request(
    name: str,
    archive_snapshot: bool,
    if_match: Optional[str] = None,
    if_none_match: Optional[str] = None,
    sync_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    request_body = { "status" : "archived" if archive_snapshot else "ready" }

    return _build_request(
        "/snapshots/{name}",
        RequestMethod.PATCH.value,
        path_arguments={"name": name},
        json=request_body,
        if_match=if_match,
        if_none_match=if_none_match,
        sync_token=sync_token,
        **kwargs
    )


def build_put_snapshot_request(
    name: str,
    filters: List[Dict[str, str]],
    composition_type: str,
    retention_period: str=None,
    tags: Dict[str, str]=None,
    if_match: Optional[str] = None,
    if_none_match: Optional[str] = None,
    sync_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:

    request_body = {}

    if not filters or len(filters) < 1:
        raise ValueError("There should be at least one filter specified.")

    request_body["filters"] = filters

    if composition_type:
        if composition_type not in ("all", "group_by_key"):
            raise ValueError("Value should either be 'all' or 'group_by_key'.")

        request_body["composition_type"] = composition_type

    if retention_period:
        if not retention_period.isdigit():
            raise ValueError("Retention period value should be numeric.")

        request_body["retention_period"] = retention_period

    if tags:
        request_body["tags"] = tags

    return _build_request(
        "/snapshots/{name}",
        RequestMethod.PUT.value,
        path_arguments={"name": name},
        json=request_body,
        if_match=if_match,
        if_none_match=if_none_match,
        sync_token=sync_token,
        **kwargs
    )

def _convert_request(request, files=None):
    data = request.content if not files else None
    request = HttpRequest(method=request.method, url=request.url, headers=request.headers, data=data)
    if files:
        request.set_formdata_body(files)
    return request


def _format_url_section(template, **kwargs):
    components = template.split("/")
    while components:
        try:
            return template.format(**kwargs)
        except KeyError as key:
            formatted_components = template.split("/")
            components = [c for c in formatted_components if "{}".format(key.args[0]) not in c]
            template = "/".join(components)


class AppConfigSnapshotClient:

    def __init__(self, appConfigClient):
        self.appConfigurationImpl = appConfigClient._impl
        self._serializer = self.appConfigurationImpl._serialize
        self._deserializer = self.appConfigurationImpl._deserialize
        self._sync_token = self.appConfigurationImpl._config.sync_token

    @classmethod
    def from_connection_string(cls, connection_string):
        return cls(AzureAppConfigurationClient.from_connection_string(connection_string))

    def create_snapshot(self,
                        name: str,
                        filters: List[Dict[str, str]],
                        composition_type: str=None,
                        retention_period: str=None,
                        tags: Dict[str, str]=None,
                        if_match: Optional[str] = None,
                        if_none_match: Optional[str] = None,
                        **kwargs: Any):
        _headers = kwargs.pop("headers", {}) or {}

        request = build_put_snapshot_request(
            name=name,
            filters=filters,
            composition_type=composition_type,
            retention_period=retention_period,
            tags=tags,
            sync_token=self._sync_token,
            if_match=if_match,
            if_none_match=if_none_match,
            headers=_headers
        )

        request = _convert_request(request)

        path_format_arguments = {
            'endpoint': self._serializer.url("self._config.endpoint", self.appConfigurationImpl._config.endpoint, 'str', skip_quote=True),
        }
        # request.url = _format_url_section(
        #     http_request.url, **path_format_arguments)
        # stream = kwargs.pop("stream", True)
        # pipeline_response = self._client._pipeline.run(
        #     http_request, stream=stream, **kwargs)
        # return pipeline_response.http_response
        response = self.appConfigurationImpl._client.send_request(request)

        if response.status_code not in [201]:
            map_error(status_code=response.status_code,
                      response=response, error_map=_ERROR_MAP)
            error = self._deserializer.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        return Snapshot.from_json(json.loads(response.body().decode()))


    def get_snapshot(self,
                     name: str,
                     if_match: Optional[str] = None,
                     if_none_match: Optional[str] = None,
                     **kwargs: Any):

        _headers = kwargs.pop("headers", {}) or {}

        request = build_get_snapshot_request(
            name=name,
            if_match=if_match,
            if_none_match=if_none_match,
            sync_token=self._sync_token,
            headers=_headers
        )

        request = _convert_request(request)

        response = self.appConfigurationImpl._send_request(request)

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=_ERROR_MAP)
            error = self._deserializer.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        return Snapshot.from_json(json.loads(response.body().decode()))


    @distributed_trace
    def list_snapshots(self, **kwargs: Any):

        _headers = kwargs.pop("headers", {}) or {}


# TODO: Add deserialization
        cls = kwargs.pop("cls", None)

        request = build_list_snapshots_request(
            sync_token=self._sync_token,
            headers=_headers
        )

        request = _convert_request(request)

        response = self.appConfigurationImpl._send_request(request)

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=_ERROR_MAP)
            error = self._deserializer.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        return SnapshotListResult.from_json(json.loads(response.body().decode()))


    @distributed_trace
    def archive_snapshot(self,
                         name: str,
                         if_match: Optional[str] = None,
                         if_none_match: Optional[str] = None,
                         **kwargs: Any):
        _headers = kwargs.pop("headers", {}) or {}

# TODO: Add deserialization
        cls = kwargs.pop("cls", None)

        request = build_status_update_request(
            name=name,
            archive_snapshot=True,
            if_match=if_match,
            if_none_match=if_none_match,
            sync_token=self._sync_token,
            headers=_headers
        )

        request = _convert_request(request)

        response = self.appConfigurationImpl._send_request(request)

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=_ERROR_MAP)
            error = self._deserializer.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        return Snapshot.from_json(json.loads(response.body().decode()))

    @distributed_trace
    def recover_snapshot(self,
                         name: str,
                         if_match: Optional[str] = None,
                         if_none_match: Optional[str] = None,
                         **kwargs: Any):
        _headers = kwargs.pop("headers", {}) or {}

# TODO: Add deserialization
        cls = kwargs.pop("cls", None)

        request = build_status_update_request(
            name=name,
            archive_snapshot=False,
            if_match=if_match,
            if_none_match=if_none_match,
            sync_token=self._sync_token,
            headers=_headers
        )

        request = _convert_request(request)

        response =self.appConfigurationImpl._send_request(request)

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=_ERROR_MAP)
            error = self._deserializer.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        return Snapshot.from_json(json.loads(response.body().decode()))