from machine import Pin 
led14 = Pin(14,Pin.OUT)
led13 = Pin(13,Pin.OUT)
led12 = Pin(12,Pin.OUT)
from machine import Pin
import time

led14 = Pin(14,Pin.OUT)
led13 = Pin(13,Pin.OUT)
led12 = Pin(12,Pin.OUT)
for i in range(1000):
    led14.on()
    led13.off()
    led12.off()
    time.sleep(0.5)
    led14.off()
    led13.on()
    led12.off()
    time.sleep(0.5) 
    led14.off()
    led13.off()
    led12.on()
    time.sleep(0.5) 