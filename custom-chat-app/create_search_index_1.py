import os
from dotenv import load_dotenv, find_dotenv
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ConnectionType
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from config import get_logger

# initialize logging object
logger = get_logger(__name__)

env_path = find_dotenv()
load_dotenv(env_path)

connection_string = os.getenv("AIPROJECT_CONNECTION_STRING")

# create a project client using environment variables loaded from the .env file
project = AIProjectClient.from_connection_string(
    conn_str=connection_string, 
    credential=DefaultAzureCredential(),
)
