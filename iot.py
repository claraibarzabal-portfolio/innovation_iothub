import json
import random
import time
from azure.iot.device import IoTHubDeviceClient, Message
import requests
from requests.auth import HTTPBasicAuth

# Configuración de la conexión
connection_string = '[Your IoT hub device connection string]'
latitude = '47.4245'  # Cambia por tu latitud
longitude = '9.3767'  # Cambia por tu longitud
api_username = '[Your API Username]'
api_password = '[Your API Password]'

# Función para obtener datos históricos y pronósticos
def get_weather_data():
    today = time.strftime('%Y-%m-%d')
    historical_date = (time.time() - 15 * 86400)  # 15 días atrás
    historical_date_str = time.strftime('%Y-%m-%d', time.localtime(historical_date))

    historical_url = f"https://api.meteomatics.com/{historical_date_str}T00:00:00ZP1D:PT1H/precip_1h:mm,wind_speed_10m:ms/{latitude},{longitude}/json?model=mix"
    forecast_url = f"https://api.meteomatics.com/{today}T00:00:00ZP1D:PT1H/precip_1h:mm,wind_speed_10m:ms/{latitude},{longitude}/json?model=mix"

    historical_response = requests.get(historical_url, auth=HTTPBasicAuth(api_username, api_password))
    forecast_response = requests.get(forecast_url, auth=HTTPBasicAuth(api_username, api_password))

    return historical_response.json(), forecast_response.json()

# Función para generar datos simulados
def get_simulated_sensor_data():
    return {
        "temperatura_suelo": round(15 + random.uniform(0, 20), 2),
        "humedad_suelo": round(10 + random.uniform(0, 90), 2),
        "humedad_relativa": round(20 + random.uniform(0, 80), 2),
        "temperatura_ambiente": round(10 + random.uniform(0, 25), 2)
    }

# Función para enviar datos a IoT Hub
def send_weather_data(client):
    historical_data, forecast_data = get_weather_data()
    sensor_data = get_simulated_sensor_data()

    message_content = json.dumps({
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        **sensor_data,
        "historical": historical_data,
        "forecast": forecast_data,
    })

    message = Message(message_content)
    print("Sending message: " + message_content)
    client.send_message(message)
    print("Message sent to Azure IoT Hub")

# Crear cliente y conectar al IoT Hub
client = IoTHubDeviceClient.create_from_connection_string(connection_string)
client.connect()

try:
    while True:
        send_weather_data(client)
        time.sleep(3600)  # Enviar datos cada hora
finally:
    client.shutdown()
