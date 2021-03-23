from machine import Pin, PWM
import time

buzzer  = Pin(26, Pin.OUT)
#pwm = PWM(buzzer)
#print(pwm.freq())

while True:
    #pwm.duty(500)
    #pwm.freq(800)
    buzzer.on()
    time.sleep(0.25)
    buzzer.off()
    time.sleep(0.25)

