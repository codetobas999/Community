import connect_wifi
import socket_send
import ubinascii
import time
from machine import Pin

#####################
socket_serverip = '192.168.1.136'  #IP Server Scocket
socket_port = 9009                 #Port Server Scocket
WIFI_CFG = { 'ssid': "Home Bas_2.4G", 'pwd': "S@msak8192" } # Specify the SSID and password of your WiFi network
#####################

def start():
    wifi_connect = connect_wifi.connect_wifi( WIFI_CFG , 30 ) # try to connect the network
    if connect_wifi is None:
        print( 'WiFi connection failed' )
    else:
        ipaddr, netmask, gateway, dns = wifi_connect.ifconfig()
        mac = wifi_connect.config('mac')      # get the interface's MAC address
        macaddr = ubinascii.hexlify(mac,':').decode() #decode MAC address 
        print("============================")
        print("IP address  :", ipaddr)
        print("Net mask    :", netmask)
        print("Gateway     :", gateway)
        print("DNS server  :", dns)
        print("Mac address :", macaddr)
        print("----------------------------")
        
        led = Pin(23,Pin.OUT)
        for i in range(5):
            led.on()
            socket_send.send_data(socket_serverip,socket_port,'LED1:ON')
            time.sleep(5)
            
            led.off()
            socket_send.send_data(socket_serverip,socket_port,'LED1:OFF')
            time.sleep(5)
        