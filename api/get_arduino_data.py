'''
Script description: Get temperature and humidity from DTH11 via Arduino
Date: 07/10/2024
Dev: Harold Zambrano
'''

# Import Libraries 
import serial
import time

# Port configuration
arduino_port = 'COM8'
arduino_bau = 9600

# Initialize serial communication
service = serial.Serial(
    arduino_port,
    arduino_bau,
    timeout=1
)

# Wait for the connection to establish
time.sleep(1)

# Read data from Arduino
while True:
    # Read and decode data from the serial port
    data = service.readline().decode('utf-8').rstrip()

    if data:

        print(data)

        '''temp = data.split(",")

        print(f"Temperature: {temp} °C")
        print(f"Humidity: {hum} %")
'''
    
            

    # Pause for 1 second before reading again
    time.sleep(1)
