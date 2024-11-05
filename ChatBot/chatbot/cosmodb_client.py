from azure.cosmos import CosmosClient
from config import COSMOS_ENDPOINT, COSMOS_KEY, DATABASE_ID, CONTAINER_ID

# Inicializar cliente y contenedor de Cosmos DB una sola vez para mejorar el rendimiento
client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.get_database_client(DATABASE_ID)
container = database.get_container_client(CONTAINER_ID)

def obtener_humedad():
    try:
        query = "SELECT TOP 1 c.humedad FROM c ORDER BY c._ts DESC"
        items = list(container.query_items(query, enable_cross_partition_query=True))
        return items[0]['humedad'] if items else None
    except Exception as e:
        print(f"Error al obtener humedad: {e}")
        return None