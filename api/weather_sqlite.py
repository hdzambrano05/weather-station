'''
Dev Harold Zambrano
Script description: Send weather data (from Arduino DHT11) to SQLite3
Engine: SQLite3
Date: 09/09/2024
'''

import sqlite3
import serial
import time

# Configuración de la base de datos
DB_FILE = 'weather_station.db'
TABLE_NAME = 'sensores'

# Configuración del puerto serial
SERIAL_PORT = 'COM5'  # Cambia esto al puerto donde está conectado tu Arduino (ej.: COM3 para Windows o /dev/ttyUSB0 en Linux)
BAUD_RATE = 9600

# Conectar a SQLite3
def connect_db():
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        print("Conexión exitosa a la base de datos SQLite3.")
        return connection, cursor
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        exit()

# Insertar datos en la tabla sensores
def insert_data(cursor, connection, temperature, humidity):
    try:
        query = f"INSERT INTO {TABLE_NAME} (temperature, humidity) VALUES (?, ?)"
        cursor.execute(query, (temperature, humidity))
        connection.commit()
        print(f"Datos insertados: Temperatura={temperature}°C, Humedad={humidity}%")
    except sqlite3.Error as e:
        print(f"Error al insertar datos: {e}")

# Leer datos del Arduino y enviar a SQLite
def main():
    connection, cursor = connect_db()

    try:
        arduino = serial.Serial(SERIAL_PORT, BAUD_RATE)
        time.sleep(2)  # Espera para que se estabilice la conexión serial
        print(f"Conectado al puerto {SERIAL_PORT}")

        while True:
            if arduino.in_waiting > 0:
                line = arduino.readline().decode('utf-8').strip()

                if "temperatura" in line:
                    temperature = float(line.split(":")[1].strip())
                elif "Humendad" in line:
                    humidity = float(line.split(":")[1].strip())
                    # Insertar datos en la base de datos después de capturar ambos valores
                    insert_data(cursor, connection, temperature, humidity)

            time.sleep(2)  # Ajusta el tiempo según tu frecuencia de envío de datos

    except serial.SerialException as e:
        print(f"Error en el puerto serial: {e}")
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")
    finally:
        if 'arduino' in locals():
            arduino.close()
        cursor.close()
        connection.close()
        print("Conexiones cerradas. Salida.")

# Ejecutar el script
if __name__ == "__main__":
    main()
