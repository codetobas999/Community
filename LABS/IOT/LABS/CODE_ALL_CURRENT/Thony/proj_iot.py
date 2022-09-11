import sys 
sys.path.append("/libs") 
from machine import Pin
from mylib_main import Mylibs
import time
import _thread 
import dht
   
global mylib
global my_lcd 
global my_wifi
 
global led_status
#wifi_cfg = { 'ssid': "Home Bas_2.4G", 'pwd': "S@msak8192" }


# LED
led = Pin(18, Pin.OUT)
led.on()

# RELAY    
relay = Pin(25, Pin.OUT)
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
    global mylib
    global my_lcd
    global my_wifi
    
    mylib = Mylibs
    my_lcd = mylib.led_connect() 
    mylib.led_display(my_lcd,'Connect WIfi Start..') 
    my_wifi = mylib.wifi_connect('HOME-BKK') # 'HOME-BKK' , 'HOME-CHAINAT'
    if my_wifi["ip"] is None:
       mylib.led_display(my_lcd,'Connect Error !!!')
    else :
        time.sleep(2)
        mylib.led_display(my_lcd,my_wifi["ip"])  
        time.sleep(2)
        mylib.led_display(my_lcd,'Connected') 
 

def runserver():
    global mylib
    global led_status
    global my_wifi
    print("runserver : Start")
    print("Open on Browser...")
    print("http://" + my_wifi["ip"] +"/?LED=ON")
    print("http://" + my_wifi["ip"] +"/?LED=OFF") 
    
    host = ''
    port = 80   
    s = mylib.socket_connect(host,port) 
     
    led_status = 'OFF'
    html_on = mylib.draw_html('html_on')
    html_off = mylib.draw_html('html_off')
    while True:
        data, client = mylib.socket_get_data(s) 
        print([data])
        
        checkpc = data.split('|')[0]
        if checkpc == 'PC':
            print('From PC')
            text = '{:.1f}_{:.1f}'.format(t,h)
            client.send(text.encode('utf-8'))
            client.close()
        else:
            print('-------Web-------')
            try:
                check = data.split()[1].replace('/','').replace('?','')
                print('CHECK:',check)
                
                if check != '':
                    led_name, led_value = check.split('=')
                    if led_value == 'ON':
                        print('TURN ON LED')
                        led.on()
                        client.send(html_on)
                        client.close()
                        mylib.led_display(my_lcd,'{}: ON'.format(led_name))  
                        led_status = 'ON'
                    elif led_value == 'OFF':
                        print('TURN OFF LED')
                        led.off()
                        client.send(html_off)
                        client.close()
                        mylib.led_display(my_lcd,'{}: OFF'.format(led_name)) 
                        led_status = 'OFF'
                else:
                    if led_status == 'OFF':
                        client.send(html_off)
                    else:
                        client.send(html_on)
            except:
                pass
        
    
def loop_led():
    global mylib
    global led_status
    print("loop_led : Start")
    led_name = 'LED'
    for i in range(50):
        led.on()
        mylib.led_display(my_lcd,'{}: ON (AUTO)'.format(led_name))  
        led_status = 'ON'
        time.sleep(10)
        led.off()
        mylib.led_display(my_lcd,'{}: OFF (AUTO)'.format(led_name))  
        led_status = 'OFF'
        time.sleep(10)
    print("loop_led : End")
init_app()
#runserver()
#getTemperature()
#loop_led()
_thread.start_new_thread(runserver,())
_thread.start_new_thread(loop_led,())
