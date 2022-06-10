from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

root = Tk()
root.title("สมัครคอร์สเรียน")
root.geometry("650x450")
root.option_add('*font', 'tahoma 10')
frame = Frame(root)
frame.pack()

idlabel = Label(frame, text="ชื่อผู้ใช้", width=12, anchor=W)
idlabel.grid(column=0, row=0, padx=5, pady=10)
pwlabel = Label(frame, text="รหัสผ่าน", width=12, anchor=W)
pwlabel.grid(column=0, row=1, padx=5, pady=5)
cpwlabel = Label(frame, text="ยืนยันรหัสผ่าน", width=12, anchor=W)
cpwlabel.grid(column=0, row=2, padx=5, pady=5)
tellabel = Label(frame, text="เบอร์โทรติดต่อ", width=12, anchor=W)
tellabel.grid(column=0, row=6, padx=20, pady=20)

envar1 = StringVar(value="S0001")
entry1 = Entry(frame, textvariable=envar1, width=10, state=DISABLED);
entry1.grid(column=1, row=0, padx=5, pady=5)
envar2 = StringVar(value="12345")
entry2 = Entry(frame, textvariable=envar2, show="*", width=10);
entry2.grid(column=1, row=1, padx=5, pady=5)
envar3 = StringVar(value="12345")
entry3 = Entry(frame, textvariable=envar3, show="*", width=10);
entry3.grid(column=1, row=2, padx=5, pady=5)
envar4 = StringVar()
entry4 = Entry(frame, textvariable=envar4, width=20);
entry4.grid(column=1, row=6, padx=5, pady=5, columnspan=2)

def entry4_keypress(event):
    global tel
    tel = event.widget.get()
    checkdata()
    button1.focus_set()

entry4.bind('<Return>', entry4_keypress)

def getrvalue():
    global rtype
    varlist = {1:"ชาย", 2:"หญิง"}
    rtype = varlist[var.get()]

var = IntVar()
r1 = Radiobutton(frame, text="ชาย", width=10, variable=var, value=1, anchor=W, command=getrvalue)

r1.grid(column=0, row=3, padx=5, pady=5)
r2 = Radiobutton(frame, text="หญิง",  width=10, variable=var,  value=2, anchor=W, command=getrvalue)

r2.grid(column=1, row=3, padx=5, pady=5)

label4 = Label(frame, text="======= เลือกฟรี 1 รายการ =======", width=35)
label4.grid(column=0, row=4, columnspan=2, padx=5)
label4.config(font="tahoma 10 bold")
listbox1 = Listbox(frame, height=10, width=45)
listbox1.grid(column=0, row=5, columnspan=2)
scrolly1 = Scrollbar(frame, orient=VERTICAL, command=listbox1.yview)
scrolly1.grid(column=2, row=5, sticky=NW+SW)
listbox1.config(yscrollcommand=scrolly1.set)

def listbox1_select(event):
    w = event.widget
    data = int(w.curselection()[0])
    global freeitem
    freeitem = w.get(data)

listbox1.bind('<<ListboxSelect>>', listbox1_select)

courselist = ["ตกแต่งภาพสวย 10 ชั่วโมง", "ติดตั้งเซิร์ฟเวอร์ 5 ชั่วโมง", "โปรแกรมสำนักงาน 10 ชั่วโมง",
              "ออกแบบเว็บไซต์ 10 ชั่วโมง", "Excel ฉบับเร่งด่วน 15 ชั่วโมง", "ตัดต่อวีดีโอ 15 ชั่วโมง",
              "Facebook Fanpage 5 ชั่วโมง", "ออกแบบ Line Sticker 10 ชั่วโมง", "วาดภาพด้วย Illustrator 10 ชั่วโมง",
              "Basic mobile App 10 ชั่วโมง", "นำเสนอด้วย PowerPoint 5 ชั่วโมง", "Data on Cloud  5 ชั่วโมง"]


for item in courselist:
    listbox1.insert(END, item)

vlabel = Label(frame, width=1)
vlabel.grid(column=2, row=0, padx=5, pady=5, sticky=NW+SW)
typelabel = Label(frame, text="ประเภทสมาชิก", width=12, anchor=W)
typelabel.grid(column=3, row=0, padx=5, pady=5)
mcombo = Combobox(frame, width=10)
mcombo.grid(column=4, row=0, padx=5)
booklist = ["VIP", "EXTRA", "MEMBER"]
mcombo['values'] = booklist
mcombo.current(0)

def getcvalue():
    global coursetype
    varlist1 = {0:"", 1:"- Big Data\n"}
    varlist2 = {0:"", 1:"- Web Design\n"}
    varlist3 = {0:"", 1:"- Mobile App\n"}
    varlist4 = {0:"", 1:"- GUI Design\n"}
    coursetype = varlist1[var1.get()] + varlist2[var2.get()]  +  varlist3[var3.get()] + varlist4[var4.get()]


label2 = Label(frame, text="====== คอร์สเรียนที่สมัคร ======")
label2.grid(column=3, row=1, columnspan=2, padx=5)
var1 = IntVar()
c1 = Checkbutton(frame, text="Big Data", width=10, variable=var1, anchor=W, command=getcvalue)

c1.grid(column=3, row=2, padx=5, pady=5)
var2 = IntVar()
c2 = Checkbutton(frame, text="Web Design", width=10, variable=var2, anchor=W, command=getcvalue)

c2.grid(column=4, row=2, padx=5, pady=5)
var3 = IntVar()
c3 = Checkbutton(frame, text="Mobile App", width=10, variable=var3, anchor=W, command=getcvalue)

c3.grid(column=3, row=3, padx=5, pady=5)
var4 = IntVar()
c4 = Checkbutton(frame, text="GUI Design", width=10, variable=var4, anchor=W, command=getcvalue)

c4.grid(column=4, row=3, padx=5, pady=5)


label3 = Label(frame, text="====== ตรวจสอบข้อมูล ======", width=30)
label3.grid(column=3, row=4, columnspan=2, padx=5)
label3.config(font="tahoma 10 bold")
displaymsg = Text(frame, bg="white", height=10, width=35)
displaymsg.grid(column=3, row=5, columnspan=2, padx=5, sticky=E)
scrolly2 = Scrollbar(frame, orient=VERTICAL, command=displaymsg.yview)
scrolly2.grid(column=5, row=5, sticky=NW+SW)
displaymsg.config(yscrollcommand=scrolly2.set)

def checkdata():
    displaymsg.delete('1.0', END)
    msg = "1. ชื่อผู้ใช้: " + entry1.get() + "; "
    msg += "รหัสผ่าน: " + entry2.get() + "\n"
    msg += "2. เพศ: " + rtype + "; "
    msg += " ประเภทสมาชิก: " + mcombo.get() + "\n"
    msg += "3. คอร์สที่สมัคร:\n" + coursetype
    msg += "4. เลือกฟรี 1 รายการ:\n- " + freeitem + "\n"
    msg += "5. เบอร์โทรติดต่อ:  " + tel + "\n"
    displaymsg.insert(INSERT, msg)

def savedata():
    messagebox.showinfo("แจ้งเตือน", "บันทึกข้อมูลสำเร็จ")

image1 = PhotoImage(file="save.gif")
button1 = Button(frame, image=image1, text="บันทึก", width="100", height=30, compound="left", command=savedata)

button1.grid(column=3, row=6, padx=20, pady=20)

r1.focus_set()
root.mainloop()
