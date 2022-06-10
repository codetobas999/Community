from tkinter import *
from cakeDB import *

def adddata():

    def updateproduct(i):
        data = listbox1.get(i)
        if data != 'รหัส:ชื่อ:`จำนวนสินค้าคลัง':
            data = data.split(":",3)
            identry['text'] = data[0]
            pid = int(data[0])
            nameentry['text'] = data[1]
            qtyentry['text'] = data[2]
            pqty = int(data[2])
            addentry.focus_set()
            pqty = pqty + int(addentry.get())
            updateproducttable(pid, pqty)
            getproductlist()
            identry['text'] = ""
            nameentry['text'] = ""
            qtyentry['text'] = ""
            addtext.set("")
            listbox1.focus_set()

    def getproductlist():
        result = selectproducttable(0)
        listbox1.delete(0, END)
        for item in result:
            listbox1.insert(END, item)

    def displayproduct(i):
        data = listbox1.get(i)
        if data != 'รหัส:ชื่อ:`จำนวนสินค้าคลัง':
            data = data.split(":", 3)
            identry['text'] = data[0]
            nameentry['text'] = data[1]
            qtyentry['text'] = data[2]
            addentry.focus_set()

    def root3exit():
        root3.destroy()

    root3 = Tk()
    root3.title('เพิ่มจำนวนสินค้า')
    root3.geometry('525x450')
    root3.option_add('*font','tahoma 12')
    app3 = Frame(root3)
    app3.grid()

    blanklabel1 = Label(app3, width=5)
    blanklabel1.grid(column=0, row=0, rowspan=4)
    blanklabel2 = Label(app3, width=45)
    blanklabel2.grid(column=1, row=0, columnspan=5)
    idlabel = Label(app3, text="รหัส", width=15, anchor=W)
    idlabel.grid(column=1, row=1)
    identry = Label(app3, bg="yellow", width=15, anchor=W)
    identry.grid(column=2, row=1)
    namelabel = Label(app3, text="ชื่อ", width=15, anchor=W)
    namelabel.grid(column=1, row=2)
    nameentry = Label(app3, bg="silver", width=15, anchor=W)
    nameentry.grid(column=2, row=2)
    qtylabel = Label(app3, text="จำนวนสินค้าเดิม", width=15, anchor=W)
    qtylabel.grid(column=1, row=3)
    qtyentry = Label(app3, bg="yellow", width=15, anchor=W)
    qtyentry.grid(column=2, row=3)
    addtext = StringVar()
    addlabel = Label(app3, text="จำนวนที่เพิ่ม"
                          , width=15, anchor=W)
    addlabel.grid(column=1, row=5)
    addentry = Entry(app3,
                          textvariable=addtext,
                          width=15)
    addentry.grid(column=2, row=5)
    blanklabel3 = Label(app3, width=30)
    blanklabel3.grid(column=1, row=6, columnspan=3)
    listbox1 = Listbox(app3, height=10, width=32)
    listbox1.grid(column=1, row=7, rowspan=3, columnspan=2)
    scrolly = Scrollbar(app3, orient=VERTICAL,
                        command=listbox1.yview)
    scrolly.grid(column=3, row=7, rowspan=3, sticky=NW+SW)
    listbox1.config(yscrollcommand=scrolly.set)
    savebutton = Button(app3, text='บันทึก', width=7,
                        command=lambda: updateproduct(ACTIVE))
    savebutton.grid(column=4, row=5, sticky=NE)
    addbutton = Button(app3, text='เพิ่ม', width=7,
                       command=lambda: displayproduct(ACTIVE))
    addbutton.grid(column=4, row=7, sticky=NE)
    backbutton = Button(app3, text='กลับ', width=7,
                        command=lambda: root3exit())
    backbutton.grid(column=4, row=9, sticky=SE)

    getproductlist()
    root3.mainloop()
