# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
###import run

###run.start()

from i2c_lcd import I2cLcd
from machine import Pin,SoftI2C
import utime as time 

i2c = SoftI2C(scl=Pin(22),sda=Pin(21),freq=100000)
#print(i2c.scan()) #Return Number of Address
#print('Address :' , hex(i2c.scan()[0])) #Convert Address to Hex

lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.clear()
lcd.putstr('Hello Somsak')

'''
#Char from ROM 
lcd.clear()
lcd.putchar(chr(247))
'''



#Custom Char 0-7
arrow = bytearray([0x00,0x1F,0x1F,0x04,0x04,0x1F,0x0E,0x04])
smile = bytearray([0x1F,0x11,0x0A,0x00,0x11,0x0A,0x04,0x00])

B = bytearray([0x00,0x19,0x09,0x09,0x09,0x09,0x09,0x0F])
A = bytearray([0x00,0x1F,0x01,0x01,0x01,0x01,0x01,0x01])
S = bytearray([0x01,0x1F,0x01,0x01,0x1F,0x11,0x11,0x19])

lcd.custom_char(0, B)
lcd.custom_char(1, A)
lcd.custom_char(2, S)
lcd.custom_char(3, arrow)
lcd.custom_char(4, smile)

lcd.clear()
lcd.putchar(chr(0))
#lcd.move_to(2,0) #Move Point to Col[0-15] , Row[0-1]
lcd.putchar(chr(1))
#lcd.move_to(4,0) #Move Point to Col[0-15] , Row[0-1]
lcd.putchar(chr(2))
#lcd.putchar(chr(3))


for i in range(10):
    lcd.move_to(9,0)
    lcd.putstr('No. {}'.format(i+1))
    time.sleep(1)
lcd.move_to(5,1)
lcd.putchar(chr(4))
time.sleep(3)


'''
#Option backlight
lcd.backlight_on()
time.sleep(3)
lcd.backlight_off()
'''
'''
#Option backlight
lcd.blink_cursor_on()
time.sleep(3)
lcd.blink_cursor_off()
'''
'''
#Option display
lcd.display_off()
time.sleep(3)
lcd.display_on()
'''
