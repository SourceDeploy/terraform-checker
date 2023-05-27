"""Azure resource classes"""
from azure.mgmt.resource import ResourceManagementClient

from terraform_checker.azure import authenticate


# Read resources in Azure
class Resources:
    """Azure resources"""
    def __init__(self):
        """Init"""
        self.credentials = authenticate()

    def get_all(self, subscription_id):
        """Get all resources"""
        client = ResourceManagementClient(credential=authenticate(), subscription_id=subscription_id)
        client.resources.