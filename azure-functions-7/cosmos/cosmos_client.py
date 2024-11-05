import logging
import os
from azure.cosmos import CosmosClient, PartitionKey
import uuid

class CosmosDBClient:
    def __init__(self):
        self.endpoint = os.getenv("CosmosDBEndpoint")
        self.key = os.getenv("CosmosDBKey")
        self.database_name = "sustentabilidad-grupo7"
        self.container_name = "ToDoList"
        self.client = CosmosClient(self.endpoint, self.key)
        self.container = self.get_container()

    def get_container(self):
        database = self.client.get_database_client(self.database_name)
        
        try:
            container = database.get_container_client(self.container_name)
            container.read()  # Intentar leer el contenedor
        except Exception as e:
            logging.info(f"Container not found, creating a new one: {str(e)}")
            container = database.create_container(
                id=self.container_name,
                partition_key=PartitionKey(path="/id"),
                offer_throughput=400
            )
        return container

    def store_event(self, req_body):
        if not isinstance(req_body, dict):
            logging.error("El cuerpo de la solicitud no es un diccionario.")
            return

        if 'id' not in req_body:
            req_body['id'] = str(uuid.uuid4())

        self.container.upsert_item(req_body)
        logging.info("Datos almacenados en Cosmos DB")
