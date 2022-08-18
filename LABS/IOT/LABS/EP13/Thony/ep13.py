import sys 
sys.path.append("/libs") 
from machine import Pin
from mylib_main import Mylibs 
#import mylib_main 
import time
import _thread 
import dht

global led_status
global lcd    
global mylib

#wifi_cfg = { 'ssid': "Home Bas_2.4G", 'pwd': "S@msak8192" }



mylib = Mylibs
led_status = 'OFF'
# LED
led18 = Pin(18, Pin.OUT)
led18.on()

# RELAY    
relay = Pin(26, Pin.OUT)
relay.off()

# DHT22
d = dht.DHT22(Pin(19))

def getTemperature():
    d.measure()
    time.sleep(1)
    print("temperature  :", d.temperature())
    print("humidity  :", d.humidity())
    return [d.temperature(), d.humidity()]; 


def init_app():
    global lcd
    global mylib
    
    lcd = mylib.led_connect()
    lcd.clear()
    lcd.putstr('Connect WIfi Start..')
    mylib.wifi_connect()
    time.sleep(2)
    lcd.clear()
    lcd.putstr('Connect WIfi Success')

def led_play(action,status,socket_client):
    global mylib
    global led_status
    global lcd
    html_on = mylib.read_file_to_text('/html/led_on.txt')  
    html_off = mylib.read_file_to_text('/html/led_off.txt') 
    
    #print('status : ',status)
    if status == 'ON' :
        print('Turn ON')
        if socket_client != None:
            socket_client.send(html_on)
            socket_client.close()
        relay.on()
        lcd.clear()
        lcd.putstr('Turn ON : ' + action)
        led_status = 'ON'
    elif status == 'OFF' :
        print('Turn OFF')
        if socket_client != None:
            socket_client.send(html_off)
            socket_client.close()
        relay.off()
        lcd.clear()
        lcd.putstr('Turn OFF : ' + action)
        led_status = 'OFF'    
    
def runserver():
    global mylib
    global led_status 
    s = mylib.socket_connect('',80) 
    while True :
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
        socket_data , socket_client = mylib.socket_get_data(s) 
        try:
            check = socket_data.split()[1].replace('/','').replace('?','')
            print('CHECK:',check) 
            if check != 'LED=ON' or check != 'LED=OFF':
                led_value = check.split('=')[1] 
                led_play('Manual',led_value,socket_client) 
            else: 
                if led_status != '' : 
                   led_play('Manual',led_status,socket_client) 
        except : 
            pass 
        
def loop_led():
    global mylib
    global led_status
    global lcd
    time.sleep(5)
    led_name = 'LED'
    for i in range(100):
        led_status = 'ON'
        led_play('Auto',led_status,None)  
        
        time.sleep(30)
        led_status = 'OFF'
        led_play('Auto',led_status,None) 
        time.sleep(30)
     
init_app()
#loop_led()
runserver()
#_thread.start_new_thread(runserver,())
#_thread.start_new_thread(loop_led,())

