# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network private-endpoint dns-zone-group add",
)
class Add(AAZCommand):
    """Add a private endpoint dns zone into a dns zone group.

    :example: Add a private endpoint dns zone group.
        az network private-endpoint dns-zone-group add --endpoint-name MyPE -g MyRG -n MyZoneGroup --zone-name Zone1 --private-dns-zone PrivateDNSZone1
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/privateendpoints/{}/privatednszonegroups/{}", "2022-01-01", "properties.privateDnsZoneConfigs[]"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the private dns zone group.",
            required=True,
        )
        _args_schema.endpoint_name = AAZStrArg(
            options=["--endpoint-name"],
            help="Name of the private endpoint.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.zone_name = AAZStrArg(
            options=["--zone-name"],
            help="Name of the resource that is unique within a resource group. This name can be used to access the resource.",
            required=True,
        )
        _args_schema.private_dns_zone_id = AAZStrArg(
            options=["--private-dns-zone-id"],
            help="Name or ID of the private dns zone.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PrivateDnsZoneGroupsGet(ctx=self.ctx)()
        self.pre_instance_create()
        self.InstanceCreateByJson(ctx=self.ctx)()
        self.post_instance_create(self.ctx.selectors.subresource.required())
        yield self.PrivateDnsZoneGroupsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_create(self):
        pass

    @register_callback
    def post_instance_create(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.selectors.subresource.required(), client_flatten=True)
        return result

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            result = self.ctx.vars.instance
            result = result.properties.privateDnsZoneConfigs
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].name == self.ctx.args.zone_name,
                filters
            )
            idx = next(filters)[0]
            return result[idx]

        def _set(self, value):
            result = self.ctx.vars.instance
            result = result.properties.privateDnsZoneConfigs
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].name == self.ctx.args.zone_name,
                filters
            )
            idx = next(filters, [len(result)])[0]
            result[idx] = value
            return

    class PrivateDnsZoneGroupsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "privateDnsZoneGroupName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "privateEndpointName", self.ctx.args.endpoint_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _AddHelper._build_schema_private_dns_zone_group_read(cls._schema_on_200)

            return cls._schema_on_200

    class PrivateDnsZoneGroupsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{privateEndpointName}/privateDnsZoneGroups/{privateDnsZoneGroupName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "privateDnsZoneGroupName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "privateEndpointName", self.ctx.args.endpoint_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _AddHelper._build_schema_private_dns_zone_group_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceCreateByJson(AAZJsonInstanceCreateOperation):

        def __call__(self, *args, **kwargs):
            self.ctx.selectors.subresource.set(self._create_instance())

        def _create_instance(self):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType
            )
            _builder.set_prop("name", AAZStrType, ".zone_name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("privateDnsZoneId", AAZStrType, ".private_dns_zone_id")

            return _instance_value


class _AddHelper:
    """Helper class for Add"""

    _schema_private_dns_zone_group_read = None

    @classmethod
    def _build_schema_private_dns_zone_group_read(cls, _schema):
        if cls._schema_private_dns_zone_group_read is not None:
            _schema.etag = cls._schema_private_dns_zone_group_read.etag
            _schema.id = cls._schema_private_dns_zone_group_read.id
            _schema.name = cls._schema_private_dns_zone_group_read.name
            _schema.properties = cls._schema_private_dns_zone_group_read.properties
            return

        cls._schema_private_dns_zone_group_read = _schema_private_dns_zone_group_read = AAZObjectType()

        private_dns_zone_group_read = _schema_private_dns_zone_group_read
        private_dns_zone_group_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        private_dns_zone_group_read.id = AAZStrType()
        private_dns_zone_group_read.name = AAZStrType()
        private_dns_zone_group_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_private_dns_zone_group_read.properties
        properties.private_dns_zone_configs = AAZListType(
            serialized_name="privateDnsZoneConfigs",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        private_dns_zone_configs = _schema_private_dns_zone_group_read.properties.private_dns_zone_configs
        private_dns_zone_configs.Element = AAZObjectType()

        _element = _schema_private_dns_zone_group_read.properties.private_dns_zone_configs.Element
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_private_dns_zone_group_read.properties.private_dns_zone_configs.Element.properties
        properties.private_dns_zone_id = AAZStrType(
            serialized_name="privateDnsZoneId",
        )
        properties.record_sets = AAZListType(
            serialized_name="recordSets",
            flags={"read_only": True},
        )

        record_sets = _schema_private_dns_zone_group_read.properties.private_dns_zone_configs.Element.properties.record_sets
        record_sets.Element = AAZObjectType()

        _element = _schema_private_dns_zone_group_read.properties.private_dns_zone_configs.Element.properties.record_sets.Element
        _element.fqdn = AAZStrType()
        _element.ip_addresses = AAZListType(
            serialized_name="ipAddresses",
        )
        _element.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        _element.record_set_name = AAZStrType(
            serialized_name="recordSetName",
        )
        _element.record_type = AAZStrType(
            serialized_name="recordType",
        )
        _element.ttl = AAZIntType()

        ip_addresses = _schema_private_dns_zone_group_read.properties.private_dns_zone_configs.Element.properties.record_sets.Element.ip_addresses
        ip_addresses.Element = AAZStrType()

        _schema.etag = cls._schema_private_dns_zone_group_read.etag
        _schema.id = cls._schema_private_dns_zone_group_read.id
        _schema.name = cls._schema_private_dns_zone_group_read.name
        _schema.properties = cls._schema_private_dns_zone_group_read.properties


__all__ = ["Add"]
