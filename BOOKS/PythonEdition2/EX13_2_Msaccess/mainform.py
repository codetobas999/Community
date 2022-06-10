from signupform import *
from loginform import *
from newpwform import *

def maindata():

    def signup():
        root1.destroy()
        signupdata()
        maindata()

    def login():
        root1.destroy()
        logindata()
        maindata()

    def newpw():
        root1.destroy()
        newpwdata()
        maindata()

    root1 = Tk()
    root1.title("หน้าแรก")
    root1.geometry('250x175')
    root1.option_add('*foreground', 'navy')
    root1.option_add('*font', 'tahoma 10 bold')
    app1 = Frame(root1)
    app1.pack()

    signupbutton = Button(app1, width=15, text="สมัครสมาชิก",
                          command=signup)
    signupbutton.pack(padx=10, pady=5)
    signinbutton = Button(app1, width=15, text="เข้าสู่ระบบ",
                          command=login)
    signinbutton.pack(padx=10, pady=5)
    newbutton = Button(app1, width=15, text="เปลี่ยนรหัสผ่าน",
                       command=newpw)
    newbutton.pack(padx=10, pady=5)
    exitbutton = Button(app1, width=15, text="จบการทำงาน",
                        command=lambda: sys.exit())
    exitbutton.pack(padx=10, pady=5)

    root1.mainloop()

createdatabase()
createtable()
maindata()
