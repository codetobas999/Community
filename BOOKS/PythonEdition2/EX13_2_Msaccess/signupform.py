from tkinter import *
from tkinter import messagebox
from signupDB import *

def signupdata():

    def checksignup():
        user = userentry.get()
        pw = pwentry.get()
        cpw = cpwentry.get()
        if not selectuname(user):
            if pw != cpw:
                messagebox.showinfo("แจ้งเตือน", "ข้อมูลรหัสผ่านไม่ตรงกัน")
                pwentry.focus_set()
            else:
                result = insertsignup(user, pw)
                if result:
                    messagebox.showinfo("แจ้งเตือน", "บันทึกข้อมูลสำเร็จ")
                    usertext.set('')
                    pwtext.set('')
                    cpwtext.set('')
                    userentry.focus_set()
        else:
            messagebox.showinfo("แจ้งเตือน", "ชื่อผู้ใช้มีอยู่แล้ว")
            userentry.focus_set()

    def root2exit():
        root2.destroy()

    root2 = Tk()
    root2.title("สมัครสมาชิก")
    root2.geometry('225x150')
    root2.attributes('-topmost', 1)
    root2.option_add('*foreground', 'navy')
    root2.option_add('*font', 'tahoma 9 bold')
    app2 = Frame(root2)
    app2.grid()

    userlabel = Label(app2, text="ชื่อผู้ใช้", width=10, anchor=W)
    userlabel.grid(column=0, row=0, padx=5, pady=5)
    usertext = StringVar()
    userentry = Entry(app2, textvariable=usertext,
                      bd=2, width=10)
    userentry.grid(column=1, row=0, padx=5, pady=5)

    pwlabel = Label(app2, text="รหัสผ่าน", width=10, anchor=W)
    pwlabel.grid(column=0, row=1, padx=5, pady=5)
    pwtext = StringVar()
    pwentry = Entry(app2, show="*", textvariable=pwtext,
                    bd=2, width=10)
    pwentry.grid(column=1, row=1, padx=5, pady=5)

    cpwlabel = Label(app2, text="ยืนยันรหัสผ่าน", width=10, anchor=W)
    cpwlabel.grid(column=0, row=2, padx=5, pady=5)
    cpwtext = StringVar()
    cpwentry = Entry(app2, show="*", textvariable=cpwtext,
                     bd=2, width=10)
    cpwentry.grid(column=1, row=2, padx=5, pady=5)
    registerbutton = Button(app2,text="สมัครสมาชิก", width=10,
                            command=checksignup)
    registerbutton.grid(column=0,row=3, padx=5, pady=5)
    backbutton = Button(app2,text="กลับ", width=10,
                        command=root2exit)
    backbutton.grid(column=1,row=3, padx=5, pady=5)

    root2.mainloop()
