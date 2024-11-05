from botbuilder.core import TurnContext, ActivityHandler
from chatbot.cosmodb_client import obtener_humedad
from chatbot.openai_client import generar_respuesta, moderar_contenido

class RiegoBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        try:
            humedad = obtener_humedad()
            if humedad is not None:
                prompt = f"La humedad actual es del {humedad}%. ¿Necesitas ayuda con el riego?"
                respuesta = generar_respuesta(prompt)
                if 1 == 1:#moderar_contenido(respuesta):
                    await turn_context.send_activity(respuesta)
                else:
                    await turn_context.send_activity("El contenido generado no es seguro y no se puede mostrar.")
            else:
                await turn_context.send_activity("No pude obtener el nivel de humedad.")
        except Exception as e:
            print(f"Error en la actividad de mensaje del bot: {e}")
            await turn_context.send_activity("Ocurrió un error al procesar tu solicitud.")

    async def on_turn(self, turn_context: TurnContext):
        await self.on_message_activity(turn_context)