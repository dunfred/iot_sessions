from machine import Pin
import time

import dht

sensor = dht.DHT11(Pin(21))
led=Pin(19,Pin.OUT)
while True:

    sensor.measure()
    if sensor.temperature()>=25.0:
        led.on()
        time.sleep(1)
        led.off()
        print(sensor.temperature())
    else:    
        print("Temperature: %2.2f" % (sensor.temperature()))
        print("Humidity: %2.2f" % (sensor.humidity()))
        time.sleep_ms(1000)
