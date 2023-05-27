"""Base Azure methods"""

import os

from azure.identity import DefaultAzureCredential

from terraform_checker.config import CONFIG as config


config = config["azure"]

def authenticate():
    """Authenticates to Azure via environment variables"""
    os.environ["AZURE_CLIENT_ID"] = config["client_id"]
    os.environ["AZURE_CLIENT_SECRET"] = config["client_secret"]
    os.environ["AZURE_TENANT_ID"] = config["tenant_id"]
    credential = DefaultAzureCredential()
    return credential
