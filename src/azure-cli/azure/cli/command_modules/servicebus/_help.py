# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['servicebus'] = """
type: group
short-summary: Manage Azure Service Bus namespaces, queues, topics, subscriptions, rules and geo-disaster recovery configuration alias
"""

helps['servicebus georecovery-alias'] = """
type: group
short-summary: Manage Azure Service Bus Geo-Disaster Recovery Configuration Alias
"""

helps['servicebus georecovery-alias authorization-rule'] = """
type: group
short-summary: Manage Azure Service Bus Authorization Rule for Namespace with Geo-Disaster Recovery Configuration Alias
"""

helps['servicebus georecovery-alias authorization-rule keys'] = """
type: group
short-summary: Manage Azure Authorization Rule keys for Service Bus Namespace
"""

helps['servicebus georecovery-alias authorization-rule keys list'] = """
type: command
short-summary: List the keys and connection strings of Authorization Rule for the Service Bus Namespace
examples:
  - name: List the keys and connection strings of Authorization Rule for the namespace.
    text: az servicebus georecovery-alias authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --alias myaliasname
"""

helps['servicebus georecovery-alias authorization-rule list'] = """
type: command
short-summary: Shows the list of Authorization Rule by Service Bus Namespace
examples:
  - name: Shows the list of Authorization Rule by Service Bus Namespace
    text: az servicebus georecovery-alias authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias break-pair'] = """
type: command
short-summary: Disables Service Bus Geo-Disaster Recovery Configuration Alias and stops replicating changes from primary to secondary namespaces
examples:
  - name: Disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces
    text: az servicebus georecovery-alias break-pair --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias delete'] = """
type: command
short-summary: Deletes Service Bus Geo-Disaster Recovery Configuration Alias request accepted
examples:
  - name: Delete Service Bus Geo-Disaster Recovery Configuration Alias request accepted
    text: az servicebus georecovery-alias delete --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias exists'] = """
type: command
short-summary: Check if Geo Recovery Alias Name is available
examples:
  - name: Check availability of the Geo-Disaster Recovery Configuration Alias Name
    text: az servicebus georecovery-alias exists --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias fail-over'] = """
type: command
short-summary: Invokes Service Bus Geo-Disaster Recovery Configuration Alias failover and re-configure the alias to point to the secondary namespace
examples:
  - name: Invokes Geo-Disaster Recovery Configuration Alias failover and reconfigure the alias to point to the secondary namespace
    text: az servicebus georecovery-alias fail-over --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
"""

helps['servicebus georecovery-alias set'] = """
type: command
short-summary: Sets Service Bus Geo-Disaster Recovery Configuration Alias for the give Namespace
examples:
  - name: Sets Geo Disaster Recovery configuration - Alias for the give Namespace
    text: az servicebus georecovery-alias set --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname --partner-namespace armresourceid
  - name: Sets Service Bus Geo-Disaster Recovery Configuration Alias for the give Namespace (autogenerated)
    text: az servicebus georecovery-alias set --alias myaliasname --namespace-name primarynamespace --partner-namespace armresourceid --resource-group myresourcegroup --subscription MySubscription
    crafted: true
"""

helps['servicebus georecovery-alias show'] = """
type: command
short-summary: shows properties of Service Bus Geo-Disaster Recovery Configuration Alias for Primay/Secondary Namespace
examples:
  - name: show properties Geo-Disaster Recovery Configuration Alias of the Primary Namespace
    text: az servicebus georecovery-alias show  --resource-group myresourcegroup --namespace-name primarynamespace --alias myaliasname
  - name: Get details of Alias (Geo DR Configuration)  of the Secondary Namespace
    text: az servicebus georecovery-alias show  --resource-group myresourcegroup --namespace-name secondarynamespace --alias myaliasname
  - name: shows properties of Service Bus Geo-Disaster Recovery Configuration Alias for Primay/Secondary Namespace (autogenerated)
    text: az servicebus georecovery-alias show --alias myaliasname --namespace-name primarynamespace --resource-group myresourcegroup --subscription MySubscription
    crafted: true
"""

helps['servicebus migration'] = """
type: group
short-summary: Manage Azure Service Bus Migration of Standard to Premium
"""

helps['servicebus migration abort'] = """
type: command
short-summary: Disable the Service Bus Migration of Standard to Premium namespace
long-summary: abort command stops the replication of entities from standard to premium namespaces. The entities replicated to premium namespace before abort command will be available under premium namespace. The aborted migration can not be resumed, its has to restarted.
examples:
  - name: Disable Service Bus Migration of Standard to Premium namespace
    text: az servicebus migration abort --resource-group myresourcegroup --name standardnamespace
"""

helps['servicebus migration complete'] = """
type: command
short-summary: Completes the Service Bus Migration of Standard to Premium namespace
long-summary: After completing migration, the existing connection strings to standard namespace will connect to premium namespace automatically. Post migration name is the name that can be used to connect to standard namespace after migration is complete.
examples:
  - name: Completes the Service Bus Migration of Standard to Premium namespace
    text: az servicebus migration complete --resource-group myresourcegroup --name standardnamespace
"""

helps['servicebus migration show'] = """
type: command
short-summary: shows properties of properties of Service Bus Migration
examples:
  - name: shows properties of properties of Service Bus Migration
    text: az servicebus migration show --resource-group myresourcegroup --name standardnamespace
"""

helps['servicebus migration start'] = """
type: command
short-summary: Create and Start Service Bus Migration of Standard to Premium namespace.
long-summary: Service Bus Migration requires an empty Premium namespace to replicate entities from Standard namespace.
examples:
  - name: Create and Start Service Bus Migration of Standard to Premium namespace
    text: az servicebus migration start --resource-group myresourcegroup --name standardnamespace --target-namespace ARMIDpremiumnamespace --post-migration-name mypostmigrationname
"""

helps['servicebus namespace'] = """
type: group
short-summary: Manage Azure Service Bus Namespace
"""

helps['servicebus namespace authorization-rule'] = """
type: group
short-summary: Manage Azure Service Bus Namespace Authorization Rule
"""

helps['servicebus namespace authorization-rule create'] = """
type: command
short-summary: Create Authorization Rule for the given Service Bus Namespace
examples:
  - name: Create Authorization Rule 'myauthorule' for the given Service Bus Namespace 'mynamespace' in resourcegroup
    text: az servicebus namespace authorization-rule create --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --rights Send Listen
"""

helps['servicebus namespace authorization-rule delete'] = """
type: command
short-summary: Deletes the Authorization Rule of the Service Bus Namespace.
examples:
  - name: Deletes the Authorization Rule of the Service Bus Namespace.
    text: az servicebus namespace authorization-rule delete --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['servicebus namespace authorization-rule keys'] = """
type: group
short-summary: Manage Azure Authorization Rule connection strings for Namespace
"""

helps['servicebus namespace authorization-rule keys list'] = """
type: command
short-summary: List the keys and connection strings of Authorization Rule for Service Bus Namespace
examples:
  - name: List the keys and connection strings of Authorization Rule for Service Bus Namespace
    text: az servicebus namespace authorization-rule keys list --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['servicebus namespace authorization-rule keys renew'] = """
type: command
short-summary: Regenerate keys of Authorization Rule for the Service Bus Namespace.
examples:
  - name: Regenerate keys of Authorization Rule for the Service Bus Namespace.
    text: az servicebus namespace authorization-rule keys renew --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --key PrimaryKey
  - name: Regenerate keys of Authorization Rule for the Service Bus Namespace (autogenerated)
    text: az servicebus namespace authorization-rule keys renew --key PrimaryKey --name myauthorule --namespace-name mynamespace --resource-group myresourcegroup --subscription MySubscription
    crafted: true
"""

helps['servicebus namespace authorization-rule list'] = """
type: command
short-summary: Shows the list of Authorization Rule by Service Bus Namespace
examples:
  - name: Shows the list of Authorization Rule by Service Bus Namespace
    text: az servicebus namespace authorization-rule list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus namespace authorization-rule show'] = """
type: command
short-summary: Shows the details of Service Bus Namespace Authorization Rule
examples:
  - name: Shows the details of Service Bus Namespace Authorization Rule
    text: az servicebus namespace authorization-rule show --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule
"""

helps['servicebus namespace authorization-rule update'] = """
type: command
short-summary: Updates Authorization Rule for the given Service Bus Namespace
examples:
  - name: Updates Authorization Rule 'myauthorule' for the given Service Bus Namespace 'mynamespace' in resourcegroup
    text: az servicebus namespace authorization-rule update --resource-group myresourcegroup --namespace-name mynamespace --name myauthorule --rights Send
"""

helps['servicebus namespace create'] = """
type: command
short-summary: Create a Service Bus Namespace
examples:
  - name: Create a Service Bus Namespace.
    text: az servicebus namespace create --resource-group myresourcegroup --name mynamespace --location westus --tags tag1=value1 tag2=value2 --sku Standard
  - name: Create a new namespace with Identity and Encryption enabled.
    text: az servicebus namespace create --resource-group myresourcegroup --name mynamespace --location westus --sku Premium --mi-user-assigned /subscriptions/{subscriptionId}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName --encryption-config key-name=key1 key-vault-uri=https://mykeyvault.vault.azure.net/ user-assigned-identity=/subscriptions/{subscriptionId}}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName --encryption-config key-name=key1 key-vault-uri=https://mykeyvault.vault.azure.net/ user-assigned-identity=/subscriptions/{subscriptionId}}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName
"""

helps['servicebus namespace delete'] = """
type: command
short-summary: Deletes the Service Bus Namespace
examples:
  - name: Deletes the Service Bus Namespace
    text: az servicebus namespace delete --resource-group myresourcegroup --name mynamespace
"""

helps['servicebus namespace exists'] = """
type: command
short-summary: check for the availability of the given name for the Namespace
examples:
  - name: check for the availability of mynamespace for the Namespace
    text: az servicebus namespace exists --name mynamespace
"""

helps['servicebus namespace list'] = """
type: command
short-summary: List the Service Bus Namespaces
examples:
  - name: Get the Service Bus Namespaces by resource group
    text: az servicebus namespace list --resource-group myresourcegroup
"""

helps['servicebus namespace network-rule-set'] = """
type: group
short-summary: Manage Azure ServiceBus networkruleSet for namespace
"""

helps['servicebus namespace network-rule-set ip-rule'] = """
type: group
short-summary: Manage Azure ServiceBus ip-rules in networkruleSet for namespace
"""

helps['servicebus namespace network-rule-set virtual-network-rule'] = """
type: group
short-summary: Manage Azure ServiceBus subnet-rule in networkruleSet for namespace
"""

helps['servicebus namespace network-rule-set ip-rule add'] = """
type: command
short-summary: Add a IP-Rule for network rule of namespace.
examples:
  - name: add a IP rule in NetworkruleSet for a namespace
    text: az servicebus namespace network-rule-set ip-rule add --resource-group myresourcegroup --namespace-name mynamespace --ip-rule ip-address=10.0.0.0/24 action=Allow
"""

helps['servicebus namespace network-rule-set virtual-network-rule add'] = """
type: command
short-summary: Add a Virtual-Network-Rule for network rule of namespace.
examples:
  - name: add a VirtualNetwork rule in NetworkruleSet for a namespace
    text: az servicebus namespace network-rule-set virtual-network-rule add --resource-group myresourcegroup --namespace-name mynamespace --subnet id={subnetId} ignore-missing-endpoint=True
"""

helps['servicebus namespace network-rule-set list'] = """
type: command
short-summary: Show properties of Network rule of the given Namespace.
examples:
  - name: Show properties of Network rule of the given Namespace
    text: az servicebus namespace network-rule-set list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus namespace network-rule-set update'] = """
type: command
short-summary: Update network rule properties of the given Namespace.
examples:
  - name: Update network rule properties of the given Namespace, can be used to update public network access, trusted service and default action.
    text: az servicebus namespace network-rule-set update --resource-group myresourcegroup --namespace-name mynamespace --public-network-access Enabled
"""

helps['servicebus namespace network-rule-set ip-rule remove'] = """
type: command
short-summary: Remove Ip-Rule from network rule of namespace
examples:
  - name: remove IP rule from NetworkruleSet for a namespace
    text: az servicebus namespace network-rule-set ip-rule remove --resource-group myresourcegroup --namespace-name mynamespace --ip-rule ip-address=10.0.0.0/24
"""

helps['servicebus namespace network-rule-set virtual-network-rule remove'] = """
type: command
short-summary: Remove network rule for a namespace
examples:
  - name: remove VirtualNetwork rule from NetworkruleSet of namespace
    text: az servicebus namespace network-rule-set virtual-network-rule remove --resource-group myresourcegroup --namespace-name mynamespace --subnet id=/subscriptions/{subscriptionId}/resourceGroups/{resourcegroup}/providers/Microsoft.Network/virtualNetworks/{vnetname}/subnets/{subnetname}
"""

helps['servicebus namespace show'] = """
type: command
short-summary: Shows the Service Bus Namespace details
examples:
  - name: shows the Namespace details.
    text: az servicebus namespace show --resource-group myresourcegroup --name mynamespace
"""

helps['servicebus namespace update'] = """
type: command
short-summary: Updates a Service Bus Namespace
examples:
  - name: Updates a Service Bus Namespace.
    text: az servicebus namespace update --resource-group myresourcegroup --name mynamespace --tags tag=value
  - name: Updates a Service Bus Namespace (autogenerated)
    text: az servicebus namespace update --name mynamespace --resource-group myresourcegroup --sku Basic
    crafted: true
"""

helps['servicebus namespace replica'] = """
type: group
short-summary: Manage servicebus namespace replicas.
"""

helps['servicebus namespace replica add'] = """
type: command
short-summary: Add one or more Replica properties to a namespace.
examples:
  - name: Add one or more Replica properties to a namespace.
    text: |
        az servicebus namespace replica add --namespace-name mynamespace -g MyResourceGroup --geo-data-replication-config role-type=Secondary location-name=mylocation
"""

helps['servicebus namespace replica remove'] = """
type: command
short-summary: Remove one or more Replica properties to a namespace.
examples:
  - name: Remove one or more Replica properties to a namespace.
    text: |
        az servicebus namespace replica remove --namespace-name mynamespace -g MyResourceGroup --geo-data-replication-config role-type=Secondary location-name=mylocation
"""

helps['servicebus queue'] = """
type: group
short-summary: Manage Azure Service Bus Queue and Authorization Rule
"""

helps['servicebus queue create'] = """
type: command
short-summary: Create the Service Bus Queue
examples:
  - name: Create Service Bus Queue.
    text: az servicebus queue create --resource-group myresourcegroup --namespace-name mynamespace --name myqueue
"""

helps['servicebus queue delete'] = """
type: command
short-summary: Deletes the Service Bus Queue
examples:
  - name: Deletes the queue
    text: az servicebus queue delete --resource-group myresourcegroup --namespace-name mynamespace --name myqueue
"""

helps['servicebus queue list'] = """
type: command
short-summary: List the Queue by Service Bus Namespace
examples:
  - name: Get the Queues by Service Bus Namespace.
    text: az servicebus queue list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus queue show'] = """
type: command
short-summary: shows the Service Bus Queue Details
examples:
  - name: Shows the Service Bus Queue Details
    text: az servicebus queue show --resource-group myresourcegroup --namespace-name mynamespace --name myqueue
"""

helps['servicebus queue update'] = """
type: command
short-summary: Updates existing Service Bus Queue
examples:
  - name: Updates Service Bus Queue.
    text: az servicebus queue update --resource-group myresourcegroup --namespace-name mynamespace --name myqueue --auto-delete-on-idle PT3M
"""

helps['servicebus topic'] = """
type: group
short-summary: Manage Azure Service Bus Topic and Authorization Rule
"""

helps['servicebus topic create'] = """
type: command
short-summary: Create the Service Bus Topic
examples:
  - name: Create a new Service Bus Topic
    text: az servicebus topic create --resource-group myresourcegroup --namespace-name mynamespace --name mytopic --max-message-size-in-kilobytes 102400
"""

helps['servicebus topic delete'] = """
type: command
short-summary: Deletes the Service Bus Topic
examples:
  - name: Deletes the Service Bus Topic
    text: az servicebus topic delete --resource-group myresourcegroup --namespace-name mynamespace --name mytopic
"""

helps['servicebus topic list'] = """
type: command
short-summary: List the Topic by Service Bus Namespace
examples:
  - name: Get the Topics by Namespace.
    text: az servicebus topic list --resource-group myresourcegroup --namespace-name mynamespace
"""

helps['servicebus topic show'] = """
type: command
short-summary: Shows the Service Bus Topic Details
examples:
  - name: Shows the Topic details.
    text: az servicebus topic show --resource-group myresourcegroup --namespace-name mynamespace --name mytopic
"""

helps['servicebus topic subscription'] = """
type: group
short-summary: Manage Azure Service Bus Subscription
"""

helps['servicebus topic subscription create'] = """
type: command
short-summary: Create the ServiceBus Subscription
examples:
  - name: Create a new Subscription.
    text: az servicebus topic subscription create --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription
"""

helps['servicebus topic subscription delete'] = """
type: command
short-summary: Deletes the Service Bus Subscription
examples:
  - name: Deletes the Subscription
    text: az servicebus topic subscription delete --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription
"""

helps['servicebus topic subscription list'] = """
type: command
short-summary: List the Subscription by Service Bus Topic
examples:
  - name: Shows the Subscription by Service Bus Topic.
    text: az servicebus topic subscription list --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic
"""

helps['servicebus topic subscription rule'] = """
type: group
short-summary: Manage Azure Service Bus Rule
"""

helps['servicebus topic subscription rule create'] = """
type: command
short-summary: Create the ServiceBus Rule for Subscription
examples:
  - name: Create Rule.
    text: az servicebus topic subscription rule create --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule --filter-sql-expression myproperty=myvalue
"""

helps['servicebus topic subscription rule delete'] = """
type: command
short-summary: Deletes the ServiceBus Rule
examples:
  - name: Deletes the ServiceBus Rule
    text: az servicebus topic subscription rule delete --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule
"""

helps['servicebus topic subscription rule list'] = """
type: command
short-summary: List the ServiceBus Rule by Subscription
examples:
  - name: Shows the Rule ServiceBus by Subscription.
    text: az servicebus topic subscription rule list --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription
"""

helps['servicebus topic subscription rule show'] = """
type: command
short-summary: Shows ServiceBus Rule Details
examples:
  - name: Shows the ServiceBus Rule details.
    text: az servicebus topic subscription rule show --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule
"""

helps['servicebus topic subscription rule update'] = """
type: command
short-summary: Updates the ServiceBus Rule for Subscription
examples:
  - name: Updates Rule.
    text: az servicebus topic subscription rule update --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --subscription-name mysubscription --name myrule --filter-sql-expression myproperty=myupdatedvalue
"""

helps['servicebus topic subscription show'] = """
type: command
short-summary: Shows Service Bus Subscription Details
examples:
  - name: Shows the Subscription details.
    text: az servicebus topic subscription show --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription
"""

helps['servicebus topic subscription update'] = """
type: command
short-summary: Updates the ServiceBus Subscription
examples:
  - name: Update a new Subscription.
    text: az servicebus topic subscription update --resource-group myresourcegroup --namespace-name mynamespace --topic-name mytopic --name mysubscription --lock-duration PT3M
  - name: Updates the ServiceBus Subscription (autogenerated)
    text: az servicebus topic subscription update --name mysubscription --namespace-name mynamespace --resource-group myresourcegroup --status Active --subscription MySubscription --topic-name mytopic
    crafted: true
"""

helps['servicebus topic update'] = """
type: command
short-summary: Updates the Service Bus Topic
examples:
  - name: Updates existing Service Bus Topic.
    text: az servicebus topic update --resource-group myresourcegroup --namespace-name mynamespace --name mytopic --enable-ordering True
  - name: Updates the Service Bus Topic (autogenerated)
    text: az servicebus topic update --auto-delete-on-idle PT3M --name mytopic --namespace-name mynamespace --resource-group myresourcegroup
    crafted: true
  - name: Updates the Service Bus Topic (autogenerated)
    text: az servicebus topic update --enable-batched-operations true --name mytopic --namespace-name mynamespace --resource-group myresourcegroup
    crafted: true
"""

helps['servicebus namespace private-endpoint-connection'] = """
type: group
short-summary: Manage servicebus namespace private endpoint connection.
"""

helps['servicebus namespace private-endpoint-connection approve'] = """
type: command
short-summary: Approve a private endpoint connection request for servicebus namespace.
examples:
  - name: Approve a private endpoint connection request for servicebus namespace by ID.
    text: |
        az servicebus namespace private-endpoint-connection approve --id "/subscriptions/0000-0000-0000-0000/resourceGroups/MyResourceGroup/providers/Microsoft.ServiceBus/namesapces/mynamepsace/privateEndpointConnections/mynamespace.b56b5a95-0588-4f8b-b348-15db61590a6c"
  - name: Approve a private endpoint connection request for servicebus namespace by ID.
    text: |
        id = (az servicebus namespace show -n mynamespace --query "privateEndpointConnections[0].id")
        az servicebus namespace private-endpoint-connection approve --id $id
  - name: Approve a private endpoint connection request for servicebus namespace using namespace name and connection name.
    text: |
        az servicebus namespace private-endpoint-connection approve -g myRg --namespace-name mynamespace --name myconnection
  - name: Approve a private endpoint connection request for servicebus namespace using namespace name and connection name.
    text: |
        name = (az servicebus namespace show -n mynamespace --query "privateEndpointConnections[0].name")
        az servicebus namespace private-endpoint-connection approve -g myRg --namespace-name mynamespace --name $name
"""

helps['servicebus namespace private-endpoint-connection delete'] = """
type: command
short-summary: Delete a private endpoint connection request for servicebus namespace.
examples:
  - name: Delete a private endpoint connection request for servicebus namespace by ID.
    text: |
        az servicebus namespace private-endpoint-connection delete --id "/subscriptions/0000-0000-0000-0000/resourceGroups/MyResourceGroup/providers/Microsoft.ServiceBus/namespaces/mynamespace/privateEndpointConnections/mynamespace.b56b5a95-0588-4f8b-b348-15db61590a6c"
  - name: Delete a private endpoint connection request for servicebus namespace by ID.
    text: |
        id = (az servicebus namespace show -n mynamespace --query "privateEndpointConnections[0].id")
        az servicebus namespace private-endpoint-connection delete --id $id
  - name: Delete a private endpoint connection request for servicebus namespace using account name and connection name.
    text: |
        az servicebus namespace private-endpoint-connection delete -g myRg --namespace-name mynamespace --name myconnection
  - name: Delete a private endpoint connection request for servicebus namespace using namespace name and connection name.
    text: |
        name = (az servicebus namespace show -n mynamespace --query "privateEndpointConnections[0].name")
        az servicebus namespace private-endpoint-connection delete -g myRg --namespace-name mynamespace --name $name
"""

helps['servicebus namespace private-endpoint-connection reject'] = """
type: command
short-summary: Reject a private endpoint connection request for servicebus namespace.
examples:
  - name: Reject a private endpoint connection request for servicebus namespace by ID.
    text: |
        az servicebus namespace private-endpoint-connection reject --id "/subscriptions/0000-0000-0000-0000/resourceGroups/MyResourceGroup/providers/Microsoft.ServiceBus/namespaces/mynamespace/privateEndpointConnections/mynamespace.b56b5a95-0588-4f8b-b348-15db61590a6c"
  - name: Reject a private endpoint connection request for servicebus namespace by ID.
    text: |
        id = (az servicebus namespace show -n mynamespace --query "privateEndpointConnections[0].id")
        az servicebus namespace private-endpoint-connection reject --id $id
  - name: Reject a private endpoint connection request for servicebus namespace using namespace name and connection name.
    text: |
        az servicebus namespace private-endpoint-connection reject -g myRg --namespace-name mynamespace --name myconnection
  - name: Reject a private endpoint connection request for servicebus namespace using namespace name and connection name.
    text: |
        name = (az servicebus namespace show -n mynamespace --query "privateEndpointConnections[0].name")
        az servicebus namespace private-endpoint-connection reject -g myRg --namespace-name mynamespace --name $name
"""

helps['servicebus namespace private-endpoint-connection show'] = """
type: command
short-summary: Show details of a private endpoint connection request for servicebus namespace.
examples:
  - name: Show details of a private endpoint connection request for servicebus namespace by ID.
    text: |
        az servicebus namespace private-endpoint-connection show --id "/subscriptions/0000-0000-0000-0000/resourceGroups/MyResourceGroup/providers/Microsoft.ServiceBus/namespaces/mynamespace/privateEndpointConnections/mynamespace.b56b5a95-0588-4f8b-b348-15db61590a6c"
  - name: Show details of a private endpoint connection request for servicebus namespace by ID.
    text: |
        id = (az servicebus namespace show -n mynamespace --query "privateEndpointConnections[0].id")
        az servicebus namespace private-endpoint-connection show --id $id
  - name: Show details of a private endpoint connection request for servicebus namespace using namespace name and connection name.
    text: |
        az servicebus namespace private-endpoint-connection show -g myRg --namespace-name mynamespace --name myconnection
  - name: Show details of a private endpoint connection request for servicebus namespace using namespace name and connection name.
    text: |
        name = (az servicebus namespace show -n mynamespace --query "privateEndpointConnections[0].name")
        az servicebus namespace private-endpoint-connection show -g myRg --namespace-name mynamespace --name $name
"""

helps['servicebus namespace private-link-resource'] = """
type: group
short-summary: Manage servicebus namespace private link resources.
"""

helps['servicebus namespace private-link-resource show'] = """
type: command
short-summary: Get the private link resources that need to be created for a servicebus namespace.
examples:
  - name: Get the private link resources that need to be created for a servicebus namespace.
    text: |
        az servicebus namespace private-link-resource show --namespace-name mynamespace -g MyResourceGroup
"""

helps['servicebus namespace encryption'] = """
type: group
short-summary: Manage servicebus namespace encryption properties.
"""

helps['servicebus namespace encryption add'] = """
type: command
short-summary: Add Encryption properties to a namespace.
examples:
  - name: Set 2 different encryption properties for a namespace that has User Assigned Identity already enabled
    text: |
        az servicebus namespace encryption add --namespace-name mynamespace -g MyResourceGroup --encryption-config key-name=key1 key-vault-uri=https://mykeyvault.vault.azure.net/ user-assigned-identity=/subscriptions/{subscriptionId}}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName --encryption-config key-name=key1 key-vault-uri=https://mykeyvault.vault.azure.net/ user-assigned-identity=/subscriptions/{subscriptionId}}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName2
"""

helps['servicebus namespace encryption remove'] = """
type: command
short-summary: Remove one or more Encryption properties from a namespace.
examples:
  - name: Remove encryption properties for a namespace that has User Assigned Identity already enabled
    text: |
        az servicebus namespace encryption remove --namespace-name mynamespace -g MyResourceGroup --encryption-config key-name=key1 key-vault-uri=https://mykeyvault.vault.azure.net/ user-assigned-identity=/subscriptions/{subscriptionId}}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName
"""

helps['servicebus namespace identity'] = """
type: group
short-summary: Manage servicebus namespace identity.
"""

helps['servicebus namespace identity assign'] = """
type: command
short-summary: Assign System or User or System, User assigned identities to a namespace
examples:
  - name: Assign system assigned and user assigned identity to a namespace. (give a list of identity id's for --user-assigned)
    text: |
        az servicebus namespace identity assign --namespace-name mynamespace -g MyResourceGroup --system-assigned --user-assigned /subscriptions/{subscriptionId}}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName /subscriptions/{subscriptionId}}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName2
"""

helps['servicebus namespace identity remove'] = """
type: command
short-summary: Removes System or User or System, User assigned identities from a namespace
examples:
  - name: Remove system assigned and a user assigned identity from a namespace. (give a list of identity id's for --user-assigned)
    text: |
        az servicebus namespace identity remove --namespace-name mynamespace -g MyResourceGroup --system-assigned --user-assigned /subscriptions/{subscriptionId}}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName
"""
