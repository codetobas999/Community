from tkinter import *
from tkinter import messagebox
from productDB import *

def productdata(root1):
    root1.destroy()
    root2 = Tk()
    root2.title('ข้อมูลสินค้า')
    root2.geometry('350x250')
    app2 = Frame(root2)
    app2.grid()

    blanklabel1 = Label(app2, width=5)
    blanklabel2 = Label(app2, width=30)
    blanklabel3 = Label(app2, width=5)
    blanklabel4 = Label(app2, width=5)
    blanklabel5 = Label(app2, width=5)
    blanklabel6 = Label(app2, width=5)
    blanklabel7 = Label(app2, width=30)
    blanklabel8 = Label(app2, width=5)
    idlabel = Label(app2, text="รหัสสินค้า", font=('tahoma', '11', 'bold'), width=15, anchor=W)

    identry = Label(app2, fg="#fff", bg="blue", font=('tahoma', '11', 'bold'), width=10, anchor=W)

    namelabel = Label(app2, text="ชื่อสินค้า", font=('tahoma', '11', 'bold'), width=15,  anchor=W)

    nametext = StringVar()
    nameentry = Entry(app2, textvariable=nametext, font=('tahoma', '11', 'bold'), width=10)

    alabel = Label(app2, text="จำนวนสินค้าคลัง A", font=('tahoma', '11', 'bold'), width=15, anchor=W)

    atext = StringVar()
    aentry = Entry(app2, textvariable=atext, font=('tahoma', '11', 'bold'), width=10)

    blabel = Label(app2, text="จำนวนสินค้าคลัง B", font=('tahoma', '11', 'bold'), width=15, anchor=W)

    btext = StringVar()
    bentry = Entry(app2, textvariable=btext, font=('tahoma', '11', 'bold'), width=10)

    savebutton = Button(app2, text='บันทึก', font=('tahoma', '11', 'bold'), width=10,
                        command=lambda: insertproduct())
    backbutton = Button(app2, text='กลับ', font=('tahoma', '11', 'bold'), width=10,
                        command=lambda: root2exit())
    blanklabel1.grid(column=0, row=0, rowspan=4)
    blanklabel2.grid(column=1, row=0, columnspan=3)
    idlabel.grid(column=1, row=1)
    blanklabel3.grid(column=2, row=1)
    identry.grid(column=3, row=1)
    namelabel.grid(column=1, row=2)
    blanklabel4.grid(column=2, row=2)
    nameentry.grid(column=3, row=2)
    alabel.grid(column=1, row=3)
    blanklabel5.grid(column=2, row=3)
    aentry.grid(column=3, row=3)
    blabel.grid(column=1, row=4)
    blanklabel6.grid(column=2, row=4)
    bentry.grid(column=3, row=4)
    blanklabel7.grid(column=1, row=5, columnspan=3)
    savebutton.grid(column=1, row=6)
    blanklabel8.grid(column=2, row=6)
    backbutton.grid(column=3, row=6)

    def getproductid():
        productid = selectproductid()
        if not productid:
            pid = 'P001'
        else:
            pid = productid[1:4]
            pid = int(pid)+1
        if len(str(pid)) == 1:
            pid = 'P00' + str(pid)
        if len(str(pid)) == 2:
            pid = 'P0' + str(pid)
        if len(str(pid)) == 3:
            pid = 'P' + str(pid)
        identry['text'] = pid

    def insertproduct():
        pid = identry['text']
        pname = nameentry.get()
        total_a = int(aentry.get())
        total_b = int(bentry.get())
        productname = selectproductname(pname)
        if productname:
            messagebox.showinfo("แจ้งเตือน", "ชื่อสินค้านี้มีอยู่แล้ว")
            nameentry.focus_set()
        else:
            result = insertproducttable(pid, pname, total_a, total_b)
            if result:
                messagebox.showinfo("แจ้งเตือน", "บันทึกข้อมูลสำเร็จ")
                getproductid()
                nametext.set('')
                atext.set('')
                btext.set('')
                nameentry.focus_set()

    def root2exit():
        root2.destroy()
        maindata()

    getproductid()
    root2.mainloop()

def transferdata(root1):
    root1.destroy()
    root3 = Tk()
    root3.title('ทำรายการโอนย้าย')
    root3.geometry('450x400')
    app3 = Frame(root3)
    app3.grid()

    blanklabel1 = Label(app3, width=5)
    blanklabel2 = Label(app3, width=30)
    blanklabel3 = Label(app3, width=30)
    blanklabel4 = Label(app3, width=30)
    idlabel = Label(app3, text="รหัสหนังสือ", font=('tahoma', '11', 'bold'), width=15, anchor=W)

    identry = Label(app3, bg="yellow", font=('tahoma', '11', 'bold'), width=15)
    namelabel = Label(app3, text="ชื่อหนังสือ", font=('tahoma', '11', 'bold'), width=15, anchor=W)

    nameentry = Label(app3, bg="silver", font=('tahoma', '11', 'bold'), width=15)
    alabel = Label(app3, text="จำนวนสินค้าคลัง A", font=('tahoma', '11', 'bold'), width=15, anchor=W)

    aentry = Label(app3, bg="yellow", font=('tahoma', '11', 'bold'), width=15)
    blabel = Label(app3, text="จำนวนสินค้าคลัง B", font=('tahoma', '11', 'bold'), width=15, anchor=W)

    bentry = Label(app3, bg="silver", font=('tahoma', '11', 'bold'), width=15)
    var = IntVar()
    r1 = Radiobutton(app3, text="A -> B", font=('tahoma', '11', 'bold'), variable=var, value=1,
                     command=lambda: gettransferid())
    r2 = Radiobutton(app3, text="B -> A", font=('tahoma', '11', 'bold'), variable=var, value=2,
                     command=lambda: gettransferid())
    tidlabel = Label(app3, text="เลขที่การ่โอนย้าย", font=('tahoma', '11', 'bold'), width=15, anchor=W)

    tidtext = StringVar()
    tidentry = Entry(app3, textvariable=tidtext, fg="#fff", bg="blue", font=('tahoma', '11', 'bold'), width=15)

    transfertext = StringVar()
    transferlabel = Label(app3, text="จำนวนที่โอนย้าย", font=('tahoma', '11', 'bold'), width=15, anchor=W)

    transferentry = Entry(app3, textvariable=transfertext, font=('tahoma', '11', 'bold'), width=15)

    listbox1 = Listbox(app3, font=('tahoma', '11', 'bold'), height=5, width=30)
    addbutton = Button(app3, text='...', font=('tahoma', '11', 'bold'), width=5,
                       command=lambda: displayproduct(ACTIVE))
    savebutton = Button(app3, text='บันทึก', font=('tahoma', '11', 'bold'), width=5,
                        command=lambda: inserttransfer(ACTIVE))
    backbutton = Button(app3, text='กลับ', font=('tahoma', '11', 'bold'), width=10,
                        command=lambda: root3exit())
    blanklabel1.grid(column=0, row=0, rowspan=4)
    blanklabel2.grid(column=1, row=0, columnspan=5)
    idlabel.grid(column=1, row=1)
    identry.grid(column=2, row=1)
    namelabel.grid(column=1, row=2)
    nameentry.grid(column=2, row=2)
    alabel.grid(column=1, row=3)
    aentry.grid(column=2, row=3)
    blabel.grid(column=1, row=4)
    bentry.grid(column=2, row=4)
    r1.grid(column=1, row=5)
    r2.grid(column=2, row=5)
    tidlabel.grid(column=1, row=6)
    tidentry.grid(column=2, row=6)
    transferlabel.grid(column=1, row=7)
    transferentry.grid(column=2, row=7)
    savebutton.grid(column=3, row=7)
    blanklabel3.grid(column=1, row=8, columnspan=3)
    listbox1.grid(column=1, row=9, rowspan=2, columnspan=2)
    addbutton.grid(column=3, row=10)
    blanklabel4.grid(column=1, row=11, columnspan=3)
    backbutton.grid(column=2, row=12)

    def getproductlist():
        result = selectproducttable()
        listbox1.delete(0, END)
        for item in result:
            listbox1.insert(END, item)
        listbox1.focus_set()

    def gettransferid():
        transferid = selecttransferid()
        if not transferid:
            tid = 'T001'
        else:
            tid = transferid[1:4]
            tid = int(tid)+1
        if len(str(tid)) == 1:
            tid = 'T00' + str(tid)
        if len(str(tid)) == 2:
            tid = 'T0' + str(tid)
        if len(str(tid)) == 3:
            tid = 'T' + str(tid)
        if var.get() == 1:
            tid = tid + "A"
        else:
            tid = tid + "B"
        tidtext.set(tid)

    def inserttransfer(i):
        data = listbox1.get(i)
        if data != 'รหัส:ชื่อ:สินค้าคลัง A:สินค้าคลัง B':
            data = data.split(":",4)
            pid = data[0]
            pname = data[1]
            total_a = int(data[2])
            total_b = int(data[3])
            tid = tidentry.get()
            pqty = int(transferentry.get())
            if var.get() == 1:
                if pqty > total_a:
                    messagebox.showinfo("แจ้งเตือน", "จำนวนโอนย้ายมากกว่าจำนวนที่มีอยู่ในคลัง A")

                    transferentry.focus_set()
                else:
                    total_a = total_a - pqty
                    total_b = total_b + pqty
            else:
                if pqty > total_b:
                    messagebox.showinfo("แจ้งเตือน", "จำนวนโอนย้ายมากกว่าจำนวนที่มีอยู่ในคลัง B")

                    transferentry.focus_set()
                else:
                    total_a = total_a + pqty
                    total_b = total_b - pqty
            inserttransfertable(tid, pid, pqty)
            updateproducttable(pid, pname, total_a, total_b)
            messagebox.showinfo("แจ้งเตือน", "บันทึกการโอนย้ายสำเร็จ")
            getproductlist()
            identry['text'] = ''
            nameentry['text'] = ''
            aentry['text'] = ''
            bentry['text'] = ''
            tidtext.set('')
            transfertext.set('')
            listbox1.focus_set()

    def displayproduct(i):
        data = listbox1.get(i)
        if data != 'รหัส:ชื่อ:สินค้าคลัง A:สินค้าคลัง B':
            data = data.split(":",4)
            identry['text'] = data[0]
            nameentry['text'] = data[1]
            aentry['text'] = data[2]
            bentry['text'] = data[3]

    def root3exit():
        root3.destroy()
        maindata()

    getproductlist()
    root3.mainloop()

def transferlist(root1):
    root1.destroy()
    root4 = Tk()
    root4.title('ข้อมูลการโอนย้าย')
    root4.geometry('450x450')
    app4 = Frame(root4)
    app4.grid()

    blanklabel1 = Label(app4, width=5)
    blanklabel2 = Label(app4, width=30)
    blanklabel3 = Label(app4, width=30)
    var = IntVar()
    r1 = Radiobutton(app4, text="คลัง A", font=('tahoma', '11', 'bold'), variable=var, value=1,
                     command=lambda: gettransferlist())
    r2 = Radiobutton(app4, text="คลัง B", font=('tahoma', '11', 'bold'), variable=var, value=2,
                     command=lambda: gettransferlist())
    listbox1 = Listbox(app4, font=('tahoma', '11', 'bold'), height=15, width=45)
    backbutton = Button(app4, text='กลับ', font=('tahoma', '11', 'bold'), width=10,
                        command=lambda: root4exit())
    blanklabel1.grid(column=0, row=0)
    r1.grid(column=1, row=1)
    r2.grid(column=2, row=1)
    blanklabel2.grid(column=1, row=2)
    listbox1.grid(column=1, row=3, columnspan=3)
    blanklabel3.grid(column=1, row=4)
    backbutton.grid(column=2, row=5)

    def gettransferlist():
        result = ''
        if var.get() == 1:
            result = selecttransfertable("A")
        if var.get() == 2:
            result = selecttransfertable("B")
        listbox1.delete(0, END)
        for item in result:
            listbox1.insert(END, item)
        listbox1.focus_set()

    def root4exit():
        root4.destroy()
        maindata()

    root4.mainloop()

def maindata():
    root1 = Tk()
    root1.title('หน้าแรก')
    root1.geometry('275x200')
    root1.grid()
    app1 = Frame(root1)
    app1.pack()
    blanklabel = Label(app1, height=1)
    blanklabel.pack()
    button1 = Button(app1, font=('tahoma', '11', 'bold', 'bold'), text='ข้อมูลสินค้า', height=1, width=20,
                     command=lambda: productdata(root1))
    button1.pack()
    button2 = Button(app1, font=('tahoma', '11', 'bold'), text='ทำรายการโอนย้าย', height=1, width=20,
                     command=lambda: transferdata(root1))
    button2.pack()
    button3 = Button(app1, font=('tahoma', '11', 'bold'), text='ข้อมูลการโอนย้าย', height=1, width=20,
                     command=lambda: transferlist(root1))
    button3.pack()
    button4 = Button(app1, font=('tahoma', '11', 'bold'), text='ออกจากระบบ', height=1, width=20,
                     command=sys.exit)
    button4.pack()
    root1.mainloop()

createtable()
maindata()
