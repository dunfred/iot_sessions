import neopixel,machine,time
import random as rd

sen = machine.Pin(26,machine.Pin.OUT)
np = neopixel.NeoPixel(sen,7)

while True:
    for i in range(0,7):
        r,g,b = rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)
        np[i]= (r,g,b)
        np.write()
        time.sleep(1)
        
    for i in range(0,7):
        np[i]= (0,0,0)
        np.write()
        
    
