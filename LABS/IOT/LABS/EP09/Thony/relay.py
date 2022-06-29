from machine import Pin
import time
relay = Pin(23,Pin.OUT)
def relay_action(flag):
    if flag == 'DUAL' : 
        relay.off()
        print('Off')
        time.sleep(1)
        relay.on()
        print('On')
        time.sleep(1)
    elif flag == 'ON' :
        relay.on()
        print('On')
    else :
        relay.off()
        print('Off')  
    
for i in range(5) :
    relay_action('DUAL')
