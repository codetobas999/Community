from tkinter import *
from bookform import *
from borrowform import *
from returnform import *

def maindata():
    root1 = Tk()
    root1.title('โปรแกรมยืมคืนหนังสือ')
    root1.geometry('300x200')
    root1.option_add('*font', 'tahoma 11')
    app1 = Frame(root1)
    app1.pack()

    blanklabel = Label(app1)
    blanklabel.pack()

    def book():
        root1.destroy()
        bookdata()
        maindata()
    button1 = Button(app1, width=15, text='ข้อมูลหนังสือ', command=book)
    button1.pack()

    def borrow():
        root1.destroy()
        borrowdata()
        maindata()
    button2 = Button(app1, width=15, text='ทำรายการยืม', command=borrow)
    button2.pack()

    def returns():
        root1.destroy()
        returndata()
        maindata()
    button3 = Button(app1, width=15, text='ทำรายการคืน', command=returns)
    button3.pack()
    button4 = Button(app1, width=15, text='ออกจากระบบ', command=sys.exit)
    button4.pack()
    root1.mainloop()

maindata()
