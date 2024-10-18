/*
Date: 19-09-2024
Developer: Harold Zambrano
Sketch: Get temperature and humidity from DHT11 Sensor
*/

#include "DHT.h"

#define DHTTYPE DHT11
#define DHTPIN 7

float temp = 0;
float hum = 0;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  dht.begin();
  Serial.begin(9600);
}

void loop() {
  temp = dht.readTemperature();
  hum = dht.readHumidity();

  Serial.print("Temeratura: ");
  Serial.print("\xB0");
  Serial.print("C");
  Serial.println(temp);
  Serial.print("Humedad: ");
  Serial.println(hum);

  delay(2000); 
  }
