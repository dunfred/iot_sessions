from machine import Pin, DAC
from time import sleep_ms

dac = DAC(Pin(26))
print("Running a triangular wave from a freq of ~1Hz on PIn 26")
while True:
    for i in range(256):
        dac.write(i)
        sleep_ms(2)
        
    for i in range(256):
        dac.write(256+i)
        sleep_ms(2)