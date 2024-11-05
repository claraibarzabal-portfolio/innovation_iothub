import requests
import asyncio

# Configura tu endpoint y clave
endpoint = 'https://<your-endpoint>/contentmoderator/moderate'
subscription_key = '<your-subscription-key>'

async def check_content(content: str):
    """Verifica el contenido usando el servicio Content Moderator de Azure."""
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, lambda: requests.post(
            endpoint,
            json={"data": content},
            headers={
                'Content-Type': 'application/json',
                'Ocp-Apim-Subscription-Key': subscription_key,
            }
        ))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print('Error checking content:', error)
        return None
