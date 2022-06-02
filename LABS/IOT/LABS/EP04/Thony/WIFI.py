import network

sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)

sta_if.scan() 

sta_if.connect("Home Bas_2.4G", "S@msak8192") 

sta_if.isconnected()  
