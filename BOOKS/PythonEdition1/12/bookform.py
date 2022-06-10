from tkinter import messagebox
from tkinter import *
from bookfile import *

def bookdata():
    root2 = Tk()
    root2.title('ข้อมูลหนังสือ')
    root2.geometry('375x175')
    root2.option_add('*font', 'tahoma 10')
    app2 = Frame(root2)
    app2.grid(column=0, row=0)

    blanklabel1 = Label(app2, width=5)
    blanklabel1.grid(column=0, row=0, rowspan=4)
    blanklabel2 = Label(app2, width=30)
    blanklabel2.grid(column=1, row=0, columnspan=3)
    idlabel = Label(app2, width=10, text="รหัสหนังสือ", anchor=W)
    idlabel.grid(column=1, row=1)
    blanklabel3 = Label(app2, width=5)
    blanklabel3.grid(column=2, row=1)
    idtext = StringVar()
    identry =Entry(app2, width=25, textvariable=idtext)
    identry.grid(column=3, row=1)
    namelabel = Label(app2,  width=10, text="ชื่อหนังสือ", anchor=W)
    namelabel.grid(column=1, row=2)
    blanklabel4 = Label(app2, width=5)
    blanklabel4.grid(column=2, row=2)
    nametext = StringVar()
    nameentry = Entry(app2, width=25, textvariable=nametext)
    nameentry.grid(column=3, row=2)
    blanklabel5 = Label(app2, width=30)
    blanklabel5.grid(column=1, row=3, columnspan=3)

    def writebook():
        bookid = identry.get()
        bookname = nameentry.get()
        if bookid == '' or bookname == '':
            messagebox.showinfo("แจ้งเตือน", "ป้อนข้อมูลรหัสหรือชื่อหนังสือด้วย")
            identry.focus_set()
            return False
        booksdata = []
        booksdata.append(bookid)
        booksdata.append(bookname)
        result = searchbookdata(booksdata)
        if result:
            messagebox.showinfo("แจ้งเตือน", "มีข้อมูลหนังสือนี้แล้ว")
            return False
        data = bookid + ";" + bookname + ";" + "1" + "\n"
        result = writebookfile(data)
        if result:
            messagebox.showinfo("แจ้งเตือน", "เพิ่มรายการหนังสือสำเร็จ")
    savebutton = Button(app2, width=10, text='บันทึก', command=writebook)
    savebutton.grid(column=1, row=4)
    blanklabel6 = Label(app2, width=5)
    blanklabel6.grid(column=2, row=4)

    def root2exit():
        root2.destroy()

    backbutton = Button(app2, width=10, text='กลับ', command=root2exit)
    backbutton.grid(column=3, row=4)

    root2.mainloop()
