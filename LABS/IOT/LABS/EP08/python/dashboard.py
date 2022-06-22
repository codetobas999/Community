from tkinter import *
from webbrowser import BackgroundBrowser
from PIL import Image , ImageTk  # เกี่ยวกับรูป
from threading import Thread
import time

#Install Paclage
#pip install pillow
'''
https://www.tutorialspoint.com/how-to-make-a-tkinter-canvas-rectangle-transparent?fbclid=IwAR2noqGcrbmZonskGcYRR1GzxbNT_FzmrFK8w8u4QqMrU9sjcGGzP_ITW6w
# Define a function to make the transparent rectangle

# Store newly created image
images=[]
def create_rectangle(x,y,a,b,**options):
   if 'alpha' in options:
      # Calculate the alpha transparency for every color(RGB)
      alpha = int(options.pop('alpha') * 255)
      # Use the fill variable to fill the shape with transparent color
      fill = options.pop('fill')
      fill = win.winfo_rgb(fill) + (alpha,)
      image = Image.new('RGBA', (a-x, b-y), fill)
      images.append(ImageTk.PhotoImage(image))
      canvas.create_image(x, y, image=images[-1], anchor='nw')
      canvas.create_rectangle(x, y,a,b, **options)
'''

GUI = Tk()
# กำหนดค่าเริ่มต้นให้กับ Form
#GUI.geometry('1000x900') #Size 900* 600
GUI.state('zoomed') # Full Screen
GUI.title('Dashboard ระบบควบคุม Smart IOT')

#canvas คือกระดานวาดภาพ
canvas = Canvas(GUI,width=1500,height=900)
canvas.place(x=0,y=0) 

#ใส่ Background 
background = ImageTk.PhotoImage(Image.open(r'./imgs/farm.png')) #r คือเอาไว้ใช้ป้องกันติดอักขระขึ้นบรรทัดใหม่
canvas.create_image(300,200,anchor=NW,image=background)    #พิกัด Location ของ Image 

#-------------- ประตู --------------
#วาดรูปสี่เหลี่ยม  tags คือ เป็นการ Gruop รวม Canvas ทำให้สามารถทำทำงานเป็นกลุ่มได้
canvas.create_polygon([630,426,675,450,675,495,629,470],fill='#0ff717', width=1, outline=None  , tags='d1')
#ใส่ข้อความ
canvas.create_text(300,300,text='ประตูฟาร์มเปิดอยู่',fill='green',font=('Tohama',20,'bold'), tags='d1')
#ใส่ Line
canvas.create_line(425,320,640,455,fill='blue',width=3, tags='d1')
#canvas.create_line(150,0,100,50,50,0,0,50,smooth=1) ให้เส้นเป็นแบบมนๆ

door_state = True #สถานะประตู
def DoorOnOff(event):
    global door_state #ตัวแปรที่อ้างอิงนอกฟังก์ชันด้
    door_state = not door_state #สลับสถานะของประตู
    canvas.delete('d1') #Delete กลุ่มของ D1
    if door_state ==True :
        canvas.create_polygon([630,426,675,450,675,495,629,470],fill='#0ff717', width=1, outline=None  , tags='d1')
        canvas.create_text(300,300,text='ประตูฟาร์มเปิดอยู่',fill='green',font=('Tohama',20,'bold'), tags='d1')
        canvas.create_line(425,320,640,455,fill='blue',width=3, tags='d1')
    else :
        canvas.create_polygon([630,426,675,450,675,495,629,470],fill='red', width=1, outline=None  , tags='d1')
        canvas.create_text(300,300,text='ประตูฟาร์มปิดอยู่',fill='red',font=('Tohama',20,'bold'), tags='d1')
        canvas.create_line(425,320,640,455,fill='blue',width=3, tags='d1')        


#การทำใบพัดหมุน
fan = ImageTk.PhotoImage(Image.open(r'./imgs/fan2.png')) 
canvas.create_image(1063,461,image=fan,tags='img3',anchor=CENTER)

angle = 0 #องศาของพัดลม

def run_fan(event=None):
	# fan = ImageTk.PhotoImage(resize_image('fan-icon.png',100))
	global angle
	while True:	
		if angle != 0:
			canvas.delete('img3')
			fan = ImageTk.PhotoImage(image = Image.open(r'./imgs/fan2.png').rotate(angle)) 
			canvas.create_image(1063,461,image=fan,tags='img3',anchor=CENTER)
		angle += 20
		if angle >= 360:
			angle = 0
		time.sleep(0.1)

task = Thread(target=run_fan)
task.start()


GUI.bind('<Return>',DoorOnOff) #<Return คือ Enter>

GUI.mainloop()