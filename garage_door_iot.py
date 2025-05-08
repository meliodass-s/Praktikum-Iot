from gpio import *

MOTION_SENSOR_PIN = 0
GARAGE_DOOR_PIN = 1
LIGHT_PIN = 2

def setup():
    pinMode(MOTION_SENSOR_PIN, INPUT)
    pinMode(GARAGE_DOOR_PIN, OUTPUT)
    pinMode(LIGHT_PIN, OUTPUT)

def loop():
    motion = digitalRead(MOTION_SENSOR_PIN)
    if motion == HIGH:
        digitalWrite(GARAGE_DOOR_PIN, HIGH)
        digitalWrite(LIGHT_PIN, HIGH)
    else:
        digitalWrite(GARAGE_DOOR_PIN, LOW)
        digitalWrite(LIGHT_PIN, LOW)

setup()

while True:
    loop()