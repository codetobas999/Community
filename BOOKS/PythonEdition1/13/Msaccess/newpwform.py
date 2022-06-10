from tkinter import *
from tkinter import messagebox
from signupDB import *

def newpwdata():

    def checkpw():
        user = userentry.get()
        opw = opwentry.get()
        npw = npwentry.get()
        cpw = cpwentry.get()
        if selectsignup(user, opw):
            if npw != cpw:
                messagebox.showinfo("แจ้งเตือน", "ข้อมูลรหัสผ่านไม่ตรงกัน")
                npwentry.focus_set()
            else:
                result = updatesignup(user, npw)
                if result:
                    messagebox.showinfo("แจ้งเตือน", "บันทึกข้อมูลสำเร็จ")
                    usertext.set('')
                    opwtext.set('')
                    npwtext.set('')
                    cpwtext.set('')
                    userentry.focus_set()
        else:
            messagebox.showinfo("แจ้งเตือน", "ไม่พบชื่อผู้ใช้")
            userentry.focus_set()

    def root4exit():
        root4.destroy()

    root4 = Tk()
    root4.title("เปลี่ยนรหัสผ่าน")
    root4.geometry('250x175')
    root4.option_add('*foreground', 'navy')
    root4.option_add('*font', 'tahoma 9 bold')
    app4 = Frame(root4)
    app4.grid()

    userlabel = Label(app4, text="ชื่อผู้ใช้", width=10, anchor=W)
    userlabel.grid(column=0, row=0, padx=5, pady=5)
    usertext = StringVar()
    userentry = Entry(app4, textvariable=usertext,
                      bd=2, width=10)
    userentry.grid(column=1, row=0, padx=5, pady=5)
    opwlabel = Label(app4, text="รหัสผ่าน", width=10, anchor=W)
    opwlabel.grid(column=0, row=1, padx=5, pady=5)
    opwtext = StringVar()
    opwentry = Entry(app4, show="*", textvariable=opwtext,
                     bd=2, width=10)
    opwentry.grid(column=1, row=1, padx=5, pady=5)
    npwlabel = Label(app4, text="รหัสผ่าน", width=10, anchor=W)
    npwlabel.grid(column=0, row=2, padx=5, pady=5)
    npwtext = StringVar()
    npwentry = Entry(app4, show="*", textvariable=npwtext,
                     bd=2, width=10)
    npwentry.grid(column=1, row=2, padx=5, pady=5)
    cpwlabel = Label(app4, text="ยืนยันรหัสผ่าน", width=10)
    cpwlabel.grid(column=0, row=3, padx=5, pady=5)
    cpwtext = StringVar()
    cpwentry = Entry(app4, show="*", textvariable=cpwtext,
                     bd=2, width=10)
    cpwentry.grid(column=1, row=3, padx=5, pady=5)
    confirmbutton = Button(app4, text="ยืนยัน", width=10,
                           command=checkpw)
    confirmbutton.grid(column=0,row=4, padx=5, pady=5)
    backbutton = Button(app4, text="กลับ", width=10,
                        command=root4exit)
    backbutton.grid(column=1,row=4, padx=5, pady=5)

    root4.mainloop()
