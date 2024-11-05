import logging
import azure.functions as func
from cosmos.cosmos_client import CosmosDBClient
from azure.storage.blob import BlobServiceClient

# Inicializar el cliente de Blob Service
def create_blob_service_client(connection_string: str) -> BlobServiceClient:
    try:
        return BlobServiceClient.from_connection_string(connection_string)
    except Exception as e:
        logging.error(f"Error creating BlobServiceClient: {str(e)}")
        raise

# Uso del cliente
connection_string = "<YOUR_BLOB_CONNECTION_STRING>"
blob_service_client = create_blob_service_client(connection_string)

app = func.FunctionApp()

@app.function_name(name="BlobTriggerExample")
@app.blob_trigger(arg_name="myblob", blob_path="container-name/{name}", connection="AzureWebJobsStorage")
def main(myblob: func.InputStream, name: str):
    logging.info(f"Processing blob: {name}, Size: {myblob.length} bytes")

    # Leer el contenido del blob
    blob_content = myblob.read().decode('utf-8')

    # Procesar los datos (puedes aplicar transformaciones aquí)
    # processed_data = process_blob_data(blob_content)

    # Almacenar los datos en CosmosDB
    try:
        cosmos_client.store_event(blob_content)
        logging.info("Data stored in CosmosDB.")
    except Exception as e:
        logging.error(f"Error storing data in CosmosDB: {str(e)}")

"""
def process_blob_data(data: str) -> dict:
    # Lógica para transformar los datos según sea necesario
    # Por ejemplo, podrías convertir el contenido a un diccionario
    return {"data": data}

"""
""" import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="BlobTrigger1")
@app.blob_trigger(arg_name="myblob", path="samples/{name}", connection="AzureWebJobsStorage")
def blob_trigger(myblob: func.InputStream) -> None:
    logging.info(f'Blob trigger processed blob: {myblob.name}, Size: {myblob.length} bytes') """