import json
import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    cosmos_client = CosmosClient("<tu_endpoint>", "<tu_key>")
    database = cosmos_client.get_database_client("nombre_base_datos")
    container = database.get_container_client("nombre_contenedor")

    items = list(container.read_all_items())
    return func.HttpResponse(json.dumps(items), status_code=200)
  
#Ejemplo de Función POST/PUT:

import json
import azure.functions as func
from azure.cosmos import CosmosClient
import uuid

def main(req: func.HttpRequest) -> func.HttpResponse:
    cosmos_client = CosmosClient("<tu_endpoint>", "<tu_key>")
    database = cosmos_client.get_database_client("nombre_base_datos")
    container = database.get_container_client("nombre_contenedor")

    req_body = req.get_json()
    if 'id' not in req_body:
        req_body['id'] = str(uuid.uuid4())

    container.upsert_item(req_body)
    return func.HttpResponse("Datos almacenados en Cosmos DB", status_code=201)
