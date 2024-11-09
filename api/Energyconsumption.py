import random
import time
import requests

# Configuración de ThingSpeak para el canal de consumo eléctrico
THINGSPEAK_API_KEY = "GE3T8W3XQNWLKJ0L"  # Reemplaza con la clave de escritura de tu canal
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Configuración de los dispositivos y sus rangos de consumo eléctrico en watts
devices = {
    "Nevera": (100, 200),       # Rango de consumo típico de 100-200 W
    "Lavadora": (500, 1500),    # Rango de consumo típico de 500-1500 W durante el uso
    "Ducha": (3000, 5000),      # Rango de consumo típico de 3000-5000 W
    "Computadora": (100, 300),   # Rango de consumo típico de 100-300 W
    "Televisor": (50, 200),      # Rango de consumo típico de 50-200 W
}

while True:
    # Generar valores aleatorios de consumo para cada dispositivo
    data = {}
    for index, (device, (min_watt, max_watt)) in enumerate(devices.items(), start=1):
        consumption = random.uniform(min_watt, max_watt)
        data[f"field{index}"] = round(consumption, 2)
        print(f"{device}: {consumption:.2f} W")

    # Añadir la API Key al payload
    data["api_key"] = THINGSPEAK_API_KEY

    # Enviar datos a ThingSpeak
    response = requests.post(THINGSPEAK_URL, params=data)

    # Verificar si el envío fue exitoso
    if response.status_code == 200:
        print("Datos enviados exitosamente a ThingSpeak.")
    else:
        print("Error al enviar los datos a ThingSpeak:", response.status_code)

    # Esperar un intervalo antes de la siguiente medición (ej. cada 1 minutos)
    time.sleep(60)  
