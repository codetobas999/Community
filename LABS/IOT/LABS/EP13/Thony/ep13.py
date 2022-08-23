from machine import Pin, SoftI2C
import network
import time
import _thread 
import dht

global led_status
global lcd    
global mylib

#wifi_cfg = { 'ssid': "Home Bas_2.4G", 'pwd': "S@msak8192" }


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
    text = 'IP:{}'.format(ip)
    lcd.putstr(text)
    time.sleep(2)
    lcd.clear()
    lcd.putstr('Connected')
else:
    lcd.clear()
    lcd.putstr('WiFi: disconnected')

html_on = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.84.0">
    <title>ESP32 - Status</title>
    <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/pricing/">
  <link href="https://getbootstrap.com/docs/5.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  </head>
  <body>
  <div class="container">
  <form>
    <center>
      <img src="https://raw.githubusercontent.com/UncleEngineer/MicroPython-IoT/main/light-bulb-on.png" width="300">
     <h3>LED 1: ON</h3>
          <button  class="btn btn-primary" name="LED" value="ON" type="submit">ON</button>&nbsp;
        <button  class="btn btn-danger" name="LED" value="OFF" type="submit">OFF</button>
    </center>
   </form>
  </div>
    
  </body>
</html>
'''

html_off = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.84.0">
    <title>ESP32 - Status</title>
    <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/pricing/">
  <link href="https://getbootstrap.com/docs/5.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  </head>
  <body>
  <div class="container">
  <form>
    <center>
      <img src="https://raw.githubusercontent.com/UncleEngineer/MicroPython-IoT/main/light-bulb-off.png" width="300">
     <h3>LED 1: OFF</h3>
          <button  class="btn btn-primary" name="LED" value="ON" type="submit">ON</button>&nbsp;
        <button  class="btn btn-danger" name="LED" value="OFF" type="submit">OFF</button>
    </center>
   </form>
  </div>
    
  </body>
</html>
'''
global led_status
led_status = 'OFF'

def runserver():
    global led_status
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 80
    s.bind((host,port))
    s.listen(5)


    led_status = 'OFF'

    while True:
        client, addr = s.accept()
        print('connection from: ', addr)
        data = client.recv(1024).decode('utf-8')
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
                        lcd.clear()
                        lcd.putstr('{}: ON'.format(led_name))
                        led_status = 'ON'
                    elif led_value == 'OFF':
                        print('TURN OFF LED')
                        led.off()
                        client.send(html_off)
                        client.close()
                        lcd.clear()
                        lcd.putstr('{}: OFF'.format(led_name))
                        led_status = 'OFF'
                else:
                    if led_status == 'OFF':
                        client.send(html_off)
                    else:
                        client.send(html_on)
            except:
                pass
        
    
def loop_led():
    global led_status
    
    led_name = 'LED'
    for i in range(100):
        led.on()
        lcd.clear()
        lcd.putstr('{}: ON (AUTO)'.format(led_name))
        led_status = 'ON'
        time.sleep(10)
        led.off()
        lcd.clear()
        lcd.putstr('{}: OFF (AUTO)'.format(led_name))
        led_status = 'OFF'
        time.sleep(10)


_thread.start_new_thread(runserver,())
_thread.start_new_thread(check_temp,())
