import logging
import azure.functions as func
from cosmos.cosmos_client import CosmosDBClient

app = func.FunctionApp()
cosmos_client = CosmosDBClient()

@app.function_name(name="EventGridTrigger1")
@app.event_grid_trigger(arg_name="azeventgrid")
def event_grid_trigger(azeventgrid: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')
    
    try:
        req_body = azeventgrid.get_json()
        cosmos_client.store_event(req_body)
        logging.info("Datos procesados y almacenados en Cosmos DB")
    except Exception as e:
        logging.error(f"Error al procesar el evento: {str(e)}")


""" import logging
import azure.functions as func
import os
from azure.cosmos import CosmosClient, PartitionKey
import uuid

# Configuración de Cosmos DB
cosmos_endpoint = os.getenv("CosmosDBEndpoint")
cosmos_key = os.getenv("CosmosDBKey")
database_name = "sustentabilidad-grupo7"
container_name = "ToDoList"

# Conexión a Cosmos DB
def get_cosmos_client():
    return CosmosClient(cosmos_endpoint, cosmos_key)

def get_container():
    cosmos_client = get_cosmos_client()
    database = cosmos_client.get_database_client(database_name)
    
    try:
        container = database.get_container_client(container_name)
        container.read()
    except Exception as e:
        logging.info(f"Container not found, creating a new one: {str(e)}")
        container = database.create_container(
            id=container_name,
            partition_key=PartitionKey(path="/id"),
            offer_throughput=400
        )
    return container

app = func.FunctionApp()

@app.event_grid_trigger(arg_name="azeventgrid")
def main(azeventgrid: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')
    
    try:
        req_body = azeventgrid.get_json()
        store_event(req_body)
        logging.info("Datos almacenados en Cosmos DB")
    except Exception as e:
        logging.error(f"Error: {str(e)}")

def store_event(req_body):
    container = get_container()  # Obtener el contenedor aquí
    
    # Validar el req_body
    if not isinstance(req_body, dict):
        logging.error("El cuerpo de la solicitud no es un diccionario.")
        return

    if 'id' not in req_body:
        req_body['id'] = str(uuid.uuid4())
    
    container.upsert_item(req_body)
 """