from machine import Pin, PWM
import time

pwn19 = PWM(Pin(19),freq=100)
print(pwn19.freq())

#print(pwn19.freq())

try:
    while True:
        for i in range(0,512,2):
            pwn19.duty(i)
            time.sleep_ms(5)
            
        for i in range(0,512,2)[::-1]:
            pwn19.duty(i)
            time.sleep_ms(5)
                        
        #pwn19.duty(200)

    
except KeyboardInterrupt:
    pwn19.deinit()
    pwn19.duty(0)
