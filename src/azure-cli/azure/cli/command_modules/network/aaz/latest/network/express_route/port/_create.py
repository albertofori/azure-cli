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
    "network express-route port create",
)
class Create(AAZCommand):
    """Create an ExpressRoute port.

    :example: Create an ExpressRoute port. (autogenerated)
        az network express-route port create --bandwidth 200 --encapsulation Dot1Q --location westus2 --name MyExpressRoutePort --peering-location westus --resource-group MyResourceGroup
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressrouteports/{}", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
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
            help="ExpressRoute port name.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.location = AAZResourceLocationArg(
            help="Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.bandwidth_in_gbps = AAZIntArg(
            options=["--bandwidth-in-gbps"],
            help="Bandwidth of the circuit. Usage: INT {Mbps,Gbps}. Defaults to Gbps.",
        )
        _args_schema.encapsulation = AAZStrArg(
            options=["--encapsulation"],
            help="Encapsulation method on physical ports.  Allowed values: Dot1Q, QinQ.",
            enum={"Dot1Q": "Dot1Q", "QinQ": "QinQ"},
        )
        _args_schema.peering_location = AAZStrArg(
            options=["--peering-location"],
            help="The name of the peering location that the port is mapped to physically.",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...]. Use \"\" to clear existing tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Parameters"

        # define Arg Group "Properties"
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ExpressRoutePortsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ExpressRoutePortsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}",
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
                    "expressRoutePortName", self.ctx.args.name,
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("bandwidthInGbps", AAZIntType, ".bandwidth_in_gbps")
                properties.set_prop("encapsulation", AAZStrType, ".encapsulation")
                properties.set_prop("peeringLocation", AAZStrType, ".peering_location")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

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

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.id = AAZStrType()
            _schema_on_200_201.identity = AAZObjectType()
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200_201.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200_201.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200_201.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.allocation_date = AAZStrType(
                serialized_name="allocationDate",
                flags={"read_only": True},
            )
            properties.bandwidth_in_gbps = AAZIntType(
                serialized_name="bandwidthInGbps",
            )
            properties.circuits = AAZListType(
                flags={"read_only": True},
            )
            properties.encapsulation = AAZStrType()
            properties.ether_type = AAZStrType(
                serialized_name="etherType",
                flags={"read_only": True},
            )
            properties.links = AAZListType()
            properties.mtu = AAZStrType(
                flags={"read_only": True},
            )
            properties.peering_location = AAZStrType(
                serialized_name="peeringLocation",
            )
            properties.provisioned_bandwidth_in_gbps = AAZFloatType(
                serialized_name="provisionedBandwidthInGbps",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )

            circuits = cls._schema_on_200_201.properties.circuits
            circuits.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.circuits.Element
            _element.id = AAZStrType()

            links = cls._schema_on_200_201.properties.links
            links.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.links.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200_201.properties.links.Element.properties
            properties.admin_state = AAZStrType(
                serialized_name="adminState",
            )
            properties.connector_type = AAZStrType(
                serialized_name="connectorType",
                flags={"read_only": True},
            )
            properties.interface_name = AAZStrType(
                serialized_name="interfaceName",
                flags={"read_only": True},
            )
            properties.mac_sec_config = AAZObjectType(
                serialized_name="macSecConfig",
            )
            properties.patch_panel_id = AAZStrType(
                serialized_name="patchPanelId",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rack_id = AAZStrType(
                serialized_name="rackId",
                flags={"read_only": True},
            )
            properties.router_name = AAZStrType(
                serialized_name="routerName",
                flags={"read_only": True},
            )

            mac_sec_config = cls._schema_on_200_201.properties.links.Element.properties.mac_sec_config
            mac_sec_config.cak_secret_identifier = AAZStrType(
                serialized_name="cakSecretIdentifier",
            )
            mac_sec_config.cipher = AAZStrType()
            mac_sec_config.ckn_secret_identifier = AAZStrType(
                serialized_name="cknSecretIdentifier",
            )
            mac_sec_config.sci_state = AAZStrType(
                serialized_name="sciState",
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
