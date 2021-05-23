pip install azure-mgmt-resource

from azure.mgmt.resource import ResourceManagementClient

LOCATION = 'eastus'
GROUP_NAME ='sample_resource_group'

resource_client = ResourceManagementClient(credentials, subscription_id)
resource_client.resource_groups.create_or_update(GROUP_NAME, {'location': LOCATION})


print("List Resource Groups")   #### for getting the list of resources.
for item in client.resource_groups.list():
    print_item(item)