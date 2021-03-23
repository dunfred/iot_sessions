from machine import Pin
import time

btn = Pin(22, Pin.IN, Pin.PULL_UP)
led = Pin(19, Pin.OUT)
while True:
    print(btn.value())
    if btn.value() == 0:
        led.on()
    else:
        led.off()
        
