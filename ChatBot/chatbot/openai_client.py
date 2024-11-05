import openai
import asyncio # Para manejo asíncrono
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeTextOptions
from config import ENDPOINT_URL, AZURE_OPENAI_API_KEY, SEARCH_ENDPOINT, SEARCH_KEY, SEARCH_INDEX_NAME, AZURE_CONTENT_SAFETY_ENDPOINT, AZURE_CONTENT_SAFETY_API_KEY

# Inicializa OpenAI
openai.api_type = "azure"  # Especifica el tipo de API para Azure OpenAI
openai.api_base = ENDPOINT_URL  # Establece la URL del endpoint de Azure
openai.api_version = "2023-05-15"  # Usa la versión adecuada de la API
openai.api_key = AZURE_OPENAI_API_KEY

# Inicializa Azure Search
search_client = SearchClient(endpoint=SEARCH_ENDPOINT, index_name=SEARCH_INDEX_NAME, credential=AzureKeyCredential(SEARCH_KEY))

# Inicializa Azure Content Safety
content_safety_client = ContentSafetyClient(AZURE_CONTENT_SAFETY_ENDPOINT, AzureKeyCredential(AZURE_CONTENT_SAFETY_API_KEY))

async def generar_respuesta(prompt):
    try:
        # Para un manejo asíncrono (no bloqueante), aunque la librería openai no lo soporte directamente
        loop = asyncio.get_event_loop()
        completion = await loop.run_in_executor(None, lambda: openai.ChatCompletion.create(
            engine="gpt-35-turbo",  # Reemplaza con tu nombre de deployment
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0
        ))
        return completion.choices[0].message['content'].strip()
    except openai.OpenAIError as e:
        print(f"Error de OpenAI: {e}")
        return "Error al contactar con el servicio de OpenAI."
    except Exception as e:
        print(f"Error inesperado al generar respuesta: {e}")
        return "Hubo un problema al generar la respuesta."

async def moderar_contenido(texto):
    try:
        analyze_text_options = AnalyzeTextOptions(text=texto)

        # Llamada asíncrona a Content Safety
        response = await content_safety_client.analyze_text(analyze_text_options)


        # Imprime la respuesta para verificar la estructura
        print("Respuesta de Content Safety:", response)


        # Accede a las categorías bloqueadas (ajusta según la estructura real)
        categorias_bloqueadas = response.categories

        # Verifica si alguna categoría está bloqueada
        for categoria in categorias_bloqueadas:
            if categoria.severity == "block": # O el valor que indica "bloqueado" en la respuesta
                return False # El contenido NO es seguro


        return True #  Si no hay ninguna categoría bloqueada, el contenido es seguro

    except Exception as e:
        print(f"Error en la moderación de contenido: {e}")
        return False # En caso de error, asume que no es seguro