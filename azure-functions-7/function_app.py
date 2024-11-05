"""
import azure.functions as func
from http.http_trigger import app as http_app
from timer.timer_trigger import app as timer_app
from queue.queue_trigger import app as queue_app
from blob.blob_trigger import app as blob_app
from eventgrid.eventgrid_trigger import app as eventgrid_app
"""

import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
from azure.cosmos import CosmosClient
import json

app = func.FunctionApp()

# Inicializa clientes de Blob y Cosmos DB
blob_service_client = BlobServiceClient.from_connection_string("tu_cadena_de_conexion_blob")
cosmos_client = CosmosClient("tu_cadena_de_conexion_cosmos", credential="tu_clave")

def read_blob_data(container_name: str, blob_name: str) -> dict:
    """Lee datos de un blob y devuelve el contenido como diccionario."""
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_data = blob_client.download_blob().readall()
    return json.loads(blob_data)

def store_data_in_cosmos(database_name: str, container_name: str, data: dict):
    """Almacena los datos en Cosmos DB."""
    container = cosmos_client.get_database_client(database_name).get_container_client(container_name)
    container.upsert_item(data)

def process_event_and_store_data(event_body: dict):
    """Procesa el evento y almacena datos en Cosmos DB."""
    # Asumiendo que el evento contiene la información necesaria para acceder al blob
    container_name = event_body.get("data", {}).get("container_name")
    blob_name = event_body.get("data", {}).get("blob_name")
    
    if container_name and blob_name:
        # Leer datos del blob y almacenarlos en Cosmos DB
        data = read_blob_data(container_name, blob_name)
        database_name = 'tu_base_de_datos'
        store_data_in_cosmos(database_name, 'tu_contenedor', data)
    else:
        logging.error("El evento no contiene información válida sobre el blob.")

@app.function_name(name="HttpTriggerBlobToCosmos")
@app.route(route="transfer")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing HTTP request to transfer data from Blob to Cosmos DB')
    
    blob_name = req.params.get("blob_name")
    container_name = req.params.get("container_name")
    
    if not blob_name or not container_name:
        return func.HttpResponse(
            "Please pass both blob_name and container_name in the query string.",
            status_code=400
        )
    
    try:
        # Leer el blob
        data = read_blob_data(container_name, blob_name)

        # Procesar y almacenar en Cosmos DB
        database_name = 'tu_base_de_datos'
        store_data_in_cosmos(database_name, 'tu_contenedor', data)

        return func.HttpResponse("Data transferred successfully!", status_code=200)
    
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse("An error occurred while processing the request.", status_code=500)

@app.function_name(name="EventGridTrigger1")
@app.event_grid_trigger(arg_name="azeventgrid")
def event_grid_trigger(azeventgrid: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')
    
    try:
        req_body = azeventgrid.get_json()
        # Procesar el evento y almacenar datos en Cosmos DB
        process_event_and_store_data(req_body)
        
        logging.info("Datos procesados y almacenados en Cosmos DB")
    except Exception as e:
        logging.error(f"Error al procesar el evento: {str(e)}")

"""

app = func.FunctionApp()

# Registrar las aplicaciones de los triggers
app.register_functions(http_app)
app.register_functions(timer_app)
app.register_functions(queue_app)
app.register_functions(blob_app)
app.register_functions(eventgrid_app)  # Registrar el Event Grid Trigger

"""
