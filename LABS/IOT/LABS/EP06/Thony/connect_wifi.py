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
      



            
            


