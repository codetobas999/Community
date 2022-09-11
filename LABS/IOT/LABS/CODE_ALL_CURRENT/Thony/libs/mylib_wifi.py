import network
import time
#####################

#####################
def connect_wifi( wifi_cfg, max_retries=10 ):
    wifi_sta = network.WLAN( network.STA_IF ) # use WiFi in station mode (not AP)
    if not wifi_sta.isconnected():        
        wifi_sta.active(True)                     # activate the WiFi interface (up)
        wifi_sta.connect( wifi_cfg['ssid'], wifi_cfg['pwd'] ) # connect to the specified WiFi AP
        retries = 0
        while not wifi_sta.isconnected():
            retries = retries + 1
            if retries >= max_retries:
                return None
            time.sleep_ms(500)          
    return wifi_sta

'''
--Example Call WIFI
import mylib_wifi
import ubinascii
##################### 
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
'''        