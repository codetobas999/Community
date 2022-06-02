import network
import utime as time
import socket
import ubinascii
import time
from machine import Pin
#####################
serverip = '192.168.1.104'  #IP Server Scocket
port = 9009                 #Port Server Scocket   
#####################
def led_demo(msg):
    led = Pin(5,Pin.OUT)
    send_data('LED : ' + msg)
    if msg == 'ON':
        led.on()
    elif msg == 'OFF':
        led.off()
    else :
        for i in range(10):
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(1)
        
def send_data(data): 
    print('port : ' + str(port))
    server = socket.socket() 
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) 
    server.connect((serverip,port)) 
    server.send(data.encode('utf-8')) 
    data_server = server.recv(1024).decode('utf-8')
    print('Server:' , data_server)
    server.close()
    
def connect_wifi( wifi_cfg, max_retries=10 ):
    wifi_sta = network.WLAN( network.STA_IF ) # use WiFi in station mode (not AP)
    wifi_sta.active(True)                     # activate the WiFi interface (up)
    wifi_sta.connect( wifi_cfg['ssid'], wifi_cfg['pwd'] ) # connect to the specified WiFi AP
    retries = 0
    while not wifi_sta.isconnected():
        retries = retries + 1
        if retries >= max_retries:
            return None
        time.sleep_ms(500)
    return wifi_sta

WIFI_CFG = { 'ssid': "Home Bas_2.4G", 'pwd': "S@msak8192" } # Specify the SSID and password of your WiFi network

wifi = connect_wifi( WIFI_CFG , 30 ) # try to connect the network
if wifi is None:
    print( 'WiFi connection failed' )
else:
    ipaddr, netmask, gateway, dns = wifi.ifconfig()
    mac = wifi.config('mac')      # get the interface's MAC address
    macaddr = ubinascii.hexlify(mac,':').decode() #decode MAC address 
    print("============================")
    print("IP address  :", ipaddr)
    print("Net mask    :", netmask)
    print("Gateway     :", gateway)
    print("DNS server  :", dns)
    print("Mac address :", macaddr)
    print("----------------------------")
    