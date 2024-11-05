from quart import Quart, request, render_template, jsonify
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext, ActivityHandler, MessageFactory # Importa MessageFactory
from botbuilder.schema import Activity
from chatbot.cosmodb_client import obtener_humedad
from chatbot.openai_client import generar_respuesta, moderar_contenido
import os
import uuid
from config import BOT_APP_ID, BOT_APP_PASSWORD

app = Quart(__name__)

adapter_settings = BotFrameworkAdapterSettings(BOT_APP_ID, BOT_APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)

class RiegoBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        try:
            humedad = obtener_humedad()
            if humedad is not None:
                prompt = f"La humedad actual es del {humedad}%. ¿Necesitas ayuda con el riego?"
                respuesta = await generar_respuesta(prompt)  # await si es necesario
                if await moderar_contenido(respuesta): # await si es necesario
                    await turn_context.send_activity(MessageFactory.text(respuesta)) # Usar MessageFactory
                else:
                    await turn_context.send_activity(MessageFactory.text("El contenido generado no es seguro."))
            else:
                await turn_context.send_activity(MessageFactory.text("No pude obtener el nivel de humedad."))
        except Exception as e:
            print(f"Error en on_message_activity: {e}")
            await turn_context.send_activity(MessageFactory.text("Error al procesar la solicitud."))


@app.route("/")
async def index():
    return await render_template("index.html")

@app.route("/api/messages", methods=["POST"])
async def messages():
    try:
        body = await request.get_json()
        activity = Activity().deserialize(body)
        auth_header = request.headers.get("Authorization", "")
        await adapter.process_activity(activity, auth_header, bot.on_turn)
        return "ok"
    except Exception as e:
        print(f"Error en el endpoint de mensajes: {e}")
        return jsonify({"error": "Error al procesar el mensaje."}), 500

@app.route("/chat", methods=["POST"])
async def chat():
    try:
        user_message = (await request.get_json()).get("message")
        # Genera un ID de conversación único o déjalo en blanco
        conversation_id = str(uuid.uuid4())
        activity = Activity().deserialize({
            "text": user_message,
            "type": "message",
            "conversation": {"id": conversation_id}  # ID dinámico
        })
        turn_context = TurnContext(adapter, activity)
        await bot.on_turn(turn_context) #  El bot maneja la respuesta
        return "ok" #  Devuelve "ok" ya que el bot envía la respuesta en on_turn

    except Exception as e:
        print(f"Error en el endpoint de chat: {e}")
        return jsonify({"error": "Error al procesar tu solicitud."}), 500

if __name__ == "__main__":
    # from chatbot.bot import RiegoBot # Mover la instanciación aquí
    bot = RiegoBot() # Instanciar el bot después de definir la clase
    app.run(port=3978, debug=True)