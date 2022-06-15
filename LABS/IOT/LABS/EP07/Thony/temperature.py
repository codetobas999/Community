from machine import Pin
import senddata
import time
import dht
d = dht.DHT22(Pin(23))
def getTemperature():
    d.measure()
    time.sleep(1)
    print("temperature  :", d.temperature())
    print("humidity  :", d.humidity())
    return [d.temperature(), d.humidity()]; 
    
for i in range(5):
    print("Loop #" , i)
    listTemperature = getTemperature()
    #print(listTemperature[0])
    print("temperature  :", listTemperature[0])
    print("humidity  :", listTemperature[1])
    result = 'TEMP{}:{}|HUMI:{}'.format(i,listTemperature[0],listTemperature[1])
    senddata.message_send(result) #str(listTemperature[0])
    time.sleep(3) 
    print("-------------------------------------")
    time.sleep(5)

