import sys 
sys.path.append("/libs")
from machine import Pin,SoftI2C
from mylib_i2c_lcd import I2cLcd 
import mylib_wifi
import mylib_file
import mylib_socket
import ubinascii
import time

class Mylibs:
    #wifi_cfg = { 'ssid': "Home Bas_2.4G", 'pwd': "S@msak8192" } # Specify the SSID and password of your WiFi network
    wifi_cfg = { 'ssid': "HOME-BAS-TRUE-2.4G", 'pwd': "S@msak8192" } # Specify the SSID and password of your WiFi network
    def __init__(self):
        #self.wifi_cfg = wifi_cfg
        print('ini')
        
    def socket_connect(host,port):
        socket = mylib_socket.open_socket(host,port)
        return socket     
        
    def socket_get_data(socket):
        socket_client , socket_addr = socket.accept()
        print('Connection from : ',socket_addr)
        socket_data = socket_client.recv(1024).decode('utf-8')
        #print([socket_data]) 
        return socket_data , socket_client

    def wifi_connect(cfg_wi_add):
        ##################### 
 
        if cfg_wi_add == 'HOME-BKK':
            print( 'Connect WiFi BKK' )
            WIFI_CFG = { 'ssid': "HOME-BAS-TRUE-2.4G", 'pwd': "S@msak8192" } # Specify the SSID and password of your WiFi network
        elif cfg_wi_add == 'HOME-CHAINAT':    
            print( 'Connect WiFi CHAINAT' )
            WIFI_CFG = { 'ssid': "Home Bas_2.4G", 'pwd': "S@msak8192" } # Specify the SSID and password of your WiFi network
        else :
            print( 'Connect WiFi CHAINAT(Default)' )
            WIFI_CFG = { 'ssid': "Home Bas_2.4G", 'pwd': "S@msak8192" } # Specify the SSID and password of your WiFi network
        #####################
        wifi_connect = mylib_wifi.connect_wifi( WIFI_CFG , 30 ) # try to connect the network
        if wifi_connect is None:
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
            return ipaddr, netmask, gateway, dns
        
    def led_connect():
        # DEFINE LCD 
        i2c = SoftI2C(scl=Pin(22),sda=Pin(21),freq=100000)
        #print(i2c.scan()) #Return Number of Address
        #print('Address :' , hex(i2c.scan()[0])) #Convert Address to Hex
        lcd = I2cLcd(i2c, 0x27, 2, 16)
        time.sleep(1)
        lcd.clear()
        return lcd

    def read_file_to_text(file_name): 
        return mylib_file.read_file(file_name)
