from tkinter import *
from tkinter import messagebox
from cakeDB import *

def cakedata():

    def insertproduct():
        pname = nameentry.get()
        pqty = int(qtyentry.get())
        if var1.get() == 0:
            check1 = 'N'
        else:
            check1 = 'Y'
        if var2.get() == 0:
            check2 = 'N'
        else:
            check2 = 'Y'
        if var3.get() == 0:
            check3 = 'N'
        else:
            check3 = 'Y'
        productname = selectproductname(pname)
        if productname:
            messagebox.showinfo("แจ้งเตือน", "ชื่อสินค้านี้มีอยู่แล้ว")
            nameentry.focus_set()
        else:
            result = insertproducttable(pname, pqty, check1, check2, check3)
            
            if result:
                messagebox.showinfo("แจ้งเตือน", "บันทึกข้อมูลสำเร็จ")
                cleardata()

    def cleardata():
        nametext.set("")
        qtytext.set("")
        var1.set("0")
        var2.set("0")
        var3.set("0")
        nameentry.focus_set()

    def root2exit():
        root2.destroy()

    root2 = Tk()
    root2.title('เพิ่มรายการสินค้า')
    root2.geometry('425x250')
    root2.option_add('*font','tahoma 12')
    app2 = Frame(root2)
    app2.grid()

    blanklabel1 = Label(app2, width=5)
    blanklabel1.grid(column=0, row=0, rowspan=4)
    blanklabel2 = Label(app2, width=30)
    blanklabel2.grid(column=1, row=0, columnspan=3)
    namelabel = Label(app2, text="ชื่อ", width=7, anchor=W)
    namelabel.grid(column=1, row=2, sticky=W)
    nametext = StringVar()
    nameentry = Entry(app2, width=20, textvariable=nametext)
    nameentry.grid(column=2, row=2, columnspan=2, sticky=W)
    qtylabel = Label(app2, text="จำนวน", width=7, anchor=W)
    qtylabel.grid(column=1, row=3, sticky=W)
    qtytext = StringVar()
    qtyentry = Entry(app2, width=20, textvariable=qtytext)
    qtyentry.grid(column=2, row=3, columnspan=2, sticky=W)
    blanklabel3 = Label(app2, width=45)
    blanklabel3.grid(column=1, row=4, columnspan=5)
    var1 = IntVar()
    r1 = Checkbutton(app2, text="นม", variable=var1,
                     command="")
    r1.grid(column=1, row=5, sticky=W)
    var2 = IntVar()
    r2 = Checkbutton(app2, text="เนย", variable=var2,
                     command="")
    r2.grid(column=2, row=5, sticky=W)
    var3 = IntVar()
    r3 = Checkbutton(app2, text="ถั่ว", variable=var3,
                     command="")
    r3.grid(column=3, row=5, sticky=W)
    blanklabel3 = Label(app2, width=30)
    blanklabel3.grid(column=1, row=6, columnspan=3)
    savebutton = Button(app2, text='บันทึก', width=7,
                        command=insertproduct)
    savebutton.grid(column=1, row=7, sticky=W)
    clearbutton = Button(app2, text='ล้างข้อมูล', width=10,
                        command=cleardata)
    clearbutton.grid(column=2, row=7, sticky=W)
    backbutton = Button(app2, text='กลับ', width=7,
                        command=root2exit)
    backbutton.grid(column=3, row=7, sticky=W)

    root2.mainloop()
