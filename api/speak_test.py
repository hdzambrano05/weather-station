import serial
import requests
import time

# Configuración de ThingSpeak
API_KEY = "FPME7DN2YVPHRB98"  # Reemplaza con tu clave de escritura de ThingSpeak
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Configuración del puerto serial
SERIAL_PORT = 'COM4'  # Cambia esto al puerto donde está conectado tu Arduino (e.g., COM3 en Windows o /dev/ttyUSB0 en Linux)
BAUD_RATE = 9600

# Conecta al puerto serial
arduino = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)  # Espera para que se estabilice la conexión serial

# Función para enviar datos a ThingSpeak
def send_data_to_thingspeak(humidity, temperature):
    data = {
        'api_key': API_KEY,
        'field1': humidity,
        'field2': temperature
    }
    response = requests.post(THINGSPEAK_URL, data=data)
    if response.status_code == 200:
        print(f"Datos enviados correctamente: Humedad={humidity}, Temperatura={temperature}")
    else:
        print("Error al enviar datos:", response.status_code, response.text)

# Bucle principal para leer datos del Arduino y enviarlos a ThingSpeak
while True:
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        if "temperatura" in line:
            # Extrae la temperatura de la línea
            temperature = float(line.split(":")[1].strip())
        elif "Humendad" in line:
            # Extrae la humedad de la línea y envía ambos datos
            humidity = float(line.split(":")[1].strip())
            send_data_to_thingspeak(humidity, temperature)
    
    # Espera 15 segundos antes de la próxima lectura y envío
    time.sleep(2)
