from botbuilder.core import BotFrameworkAdapter
import os

# Configuración del adaptador del bot para Azure
adapter = BotFrameworkAdapter(
    app_id=os.getenv("MICROSOFT_APP_ID"),
    app_password=os.getenv("MICROSOFT_APP_PASSWORD"),
)
