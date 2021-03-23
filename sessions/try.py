from machine import Pin, PWM
import time

pin = Pin(19)
led_pwm = PWM(pin)

print(led_pwm.duty())
print(led_pwm.freq())

led_pwm.freq(1000)
led_pwm.duty(32)

time.sleep(5)

def run(t):
    for i in range(3):
        pin.on()
        time.sleep(t)
        pin.off()
        time.sleep(t)
    if t != 1:
        time.sleep(1)

try:
    while True:
         [run(i) for i in [1,0.3,1]]
         time.sleep(4)
except KeyboardInterrupt:
    pin.off()
    
    
        
        
    