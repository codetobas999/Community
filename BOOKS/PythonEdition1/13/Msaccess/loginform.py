from tkinter import *
from tkinter import messagebox
from signupDB import *

def logindata():

    def setlogindata():
        user = userentry.get()
        password = pwentry.get()
        result = selectsignup(user, password)
        if not result:
            messagebox.showinfo("แจ้งเตือน", "ข้อมูลไม่ถูกต้อง")
        else:
            messagebox.showinfo("แจ้งเตือน", "เข้าสู่ระบบสำเร็จ")
            usertext.set('')
            pwtext.set('')
        userentry.focus_set()

    def root3exit():
        root3.destroy()

    root3 = Tk()
    root3.title("เข้าสู่ระบบ")
    root3.geometry('250x150')
    root3.option_add('*foreground', 'navy')
    root3.option_add('*font', 'tahoma 9 bold')
    app3 = Frame(root3)
    app3.grid()

    userlabel = Label(app3, text="ชื่อผู้ใช้", width=10, anchor=W)
    userlabel.grid(column=0, row=0, padx=5, pady=5)
    usertext = StringVar()
    userentry = Entry(app3, textvariable=usertext,
                      bd=2, width=10)
    userentry.grid(column=1, row=0, padx=5, pady=5)
    pwlabel = Label(app3, text="รหัสผ่าน", width=10, anchor=W)
    pwlabel.grid(column=0, row=1, padx=5, pady=5)
    pwtext = StringVar()
    pwentry = Entry(app3, show="*", textvariable=pwtext,
                    bd=2, width=10)
    pwentry.grid(column=1, row=1, padx=5, pady=5)
    loginbutton = Button(app3, text="เข้าสู่ระบบ", width=10,
                         command=setlogindata)
    loginbutton.grid(column=0,row=2, padx=5, pady=5)
    backbutton = Button(app3,text="กลับ", width=10,
                        command=root3exit)
    backbutton.grid(column=1,row=2, padx=5, pady=5)

    root3.mainloop()
