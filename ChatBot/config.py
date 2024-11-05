import os
from dotenv import load_dotenv

load_dotenv()

ENDPOINT_URL = os.getenv("ENDPOINT_URL", "https://n0023-m2w9q9eb-westeurope.openai.azure.com/")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")
SEARCH_ENDPOINT = os.getenv("SEARCH_ENDPOINT", "https://sostenibilidad.search.windows.net")
SEARCH_KEY = os.getenv("SEARCH_KEY", "-----")
SEARCH_INDEX_NAME = os.getenv("SEARCH_INDEX_NAME", "sostenibilidad2")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "--------")
AZURE_CONTENT_SAFETY_ENDPOINT="https://seguridad-del-contenido.cognitiveservices.azure.com/"
AZURE_CONTENT_SAFETY_API_KEY="--------"
BOT_APP_ID = os.getenv("MicrosoftAppId", "--------")
BOT_APP_PASSWORD = os.getenv("MicrosoftAppPassword", "------------")

# Credenciales de Cosmos DB
COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT", "https://cosmosdb-7.documents.azure.com:443/")
COSMOS_KEY = os.getenv("COSMOS_KEY", "------------")
DATABASE_ID = os.getenv("DATABASE_ID", "ToDoList")
CONTAINER_ID = os.getenv("CONTAINER_ID", "Items")