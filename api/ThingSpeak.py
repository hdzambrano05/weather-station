import random
import time
import requests

# Configuración de ThingSpeak con tus claves
THINGSPEAK_API_KEY = "BT74XJ5VHKNU3HB9"  # Tu clave de escritura para ThingSpeak
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Variables iniciales para temperatura y humedad
last_temperature = random.uniform(-10, 100)
last_humidity = random.uniform(0, 100)

while True:
    # Generar valores aleatorios de temperatura y humedad
    new_temperature = random.uniform(-10, 100)
    new_humidity = random.uniform(0, 100)

    # Comprobar si el nuevo valor es mayor que el último registrado
    if new_temperature > last_temperature or new_humidity > last_humidity:
        # Actualizar los últimos valores registrados
        last_temperature = new_temperature
        last_humidity = new_humidity

        # Preparar los datos para enviar a ThingSpeak
        payload = {
            "api_key": THINGSPEAK_API_KEY,
            "field1": new_temperature,
            "field2": new_humidity
        }

        # Enviar datos a ThingSpeak
        response = requests.post(THINGSPEAK_URL, params=payload)

        # Comprobar si el envío fue exitoso
        if response.status_code == 200:
            print(f"Datos enviados: Temperatura = {new_temperature:.2f}°C, Humedad = {new_humidity:.2f}%")
        else:
            print("Error al enviar los datos a ThingSpeak:", response.status_code)

    # Esperar 3 segundos antes de la siguiente medición
    time.sleep(3)
