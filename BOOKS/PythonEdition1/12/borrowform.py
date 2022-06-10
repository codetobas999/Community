from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import *
from bookfile import *
import datetime

def borrowdata():
    root3 = Tk()
    root3.title('ทำรายการยืม')
    root3.geometry('700x350')
    root3.option_add('*font', 'tahoma 10')
    app3 = Frame(root3)
    app3.grid()

    blanklabel1 = Label(app3, width=5)
    blanklabel1.grid(column=0, row=0, rowspan=7)
    blanklabel2 = Label(app3, width=5)
    blanklabel2.grid(column=1, row=0, columnspan=6)
    mcombo = Combobox(app3, width=25)
    mcombo.grid(column=1, row=1, sticky=W)
    blanklabel3 = Label(app3, width=5)
    blanklabel3.grid(column=3, row=1, rowspan=6)
    sliplabel = Label(app3, width=10, text="เลขที่การยืม ", anchor=W)
    sliplabel.grid(column=4, row=1)
    slipentry = Label(app3, width=10, anchor=W)
    slipentry.grid(column=6, row=1, sticky=W)
    listboxlabel = Label(app3, width=30, text="เลือกหนังสือที่ต้องการ", anchor=W)
    listboxlabel.grid(column=1, row=2)
    datelabel = Label(app3, width=10, text="วันที่ทำการยืม ", anchor=W)
    datelabel.grid(column=4, row=2)
    dateentry = Label(app3, width=10, anchor=W)
    dateentry.grid(column=6, row=2, sticky=W)
    listbox1 = Listbox(app3, height=10, width=30)
    listbox1.grid(column=1, row=4, rowspan=2)
    scrolly = Scrollbar(app3, orient=VERTICAL, command=listbox1.yview)
    scrolly.grid(column=2, row=4, rowspan=2, sticky=NW+SW)
    listbox1.config(yscrollcommand=scrolly.set)

    def addborrow(i):
        data1 = listbox1.get(i)
        data2 = 'รายชื่อหนังสือ'
        try:
            idx = listbox2.get(0, "end").index(data1)
        except ValueError:
            idx = -1
        if idx == -1 and data1 != 'รหัสหนังสือ;ชื่อหนังสือ':
            if data1 != data2:
                listbox2.insert(END, listbox1.get(i))
            else:
                messagebox.showinfo("แจ้งเตือน", "คุณได้เลือกหนังสือเล่มนี้แล้ว")
        blist = []
        for x in range(1, listbox2.size()):
            blist.append(listbox2.get(x))
            blist.sort()
        listbox2.delete(1, END)
        for x in range(0, len(blist)):
            listbox2.insert(END, blist[x])

    addbutton = Button(app3, width=5, text=">",  command=lambda: addborrow(ACTIVE))

    addbutton.grid(column=4, row=4)
    blanklabel4 = Label(app3, width=5)
    blanklabel4.grid(column=5, row=4, rowspan=3)
    listbox2 = Listbox(app3, height=10, width=30)
    listbox2.grid(column=6, row=4, rowspan=2)

    def removeborrow(i):
        if listbox2.get(i) != 'รายการหนังสือที่ยืม':
            listbox2.delete(i, i)

    removebutton = Button(app3, width=5, text="<", command=lambda: removeborrow(ACTIVE))

    removebutton.grid(column=4, row=5)
    blanklabel5 = Label(app3, width=5)
    blanklabel5.grid(column=1, row=6, columnspan=6)

    def getslipno():
        result = searchslipno()
        if not result:
            sno = 'SL001'
        else:
            sno = result[2:5]
            sno = int(sno)+1
            if len(str(sno)) == 1:
                sno = 'SL00' + str(sno)
            if len(str(sno)) == 2:
                sno = 'SL0' + str(sno)
            if len(str(sno)) == 3:
                sno = 'SL' + str(sno)
        slipentry['text'] = sno

    def gettoday():
        tday = datetime.datetime.now()
        tday = tday.strftime("%d/%m/%Y")
        dateentry['text'] = tday

    def getmemberlist():
        result = searchmember()
        if result:
            mcombo['values'] = result
            mcombo.current(0)

    def getbooklist():
        result = searchbooklist()
        if result:
            listbox1.delete(0, END)
            listbox2.delete(0, END)
            for item in result:
                listbox1.insert(END, item)
            listbox2.insert(END, 'รายการหนังสือที่ยืม')

    def newborrow():
        getslipno()
        gettoday()
        getmemberlist()
        getbooklist()

    def writeborrow():
        if mcombo.get() != 'รายชื่อสมาชิก':
            mno = mcombo.get()[0:4]
            for i in range(1, listbox2.size()):
                data = slipentry['text'] + ";" + mno + ";" + listbox2.get(i) + ';0\n'\

                result = writeborrowfile(data)
                if result:
                    data = listbox2.get(i)
                    bookid = data[0:4]
                    status = 1
                    result = updatebookfile(bookid, status)
                    if result:
                        save = True
                    else:
                        save = False
            if save:
                messagebox.showinfo("แจ้งเตือน", "ทำรายการยืมสำเร็จ")
                newborrow()
        else:
            messagebox.showinfo("แจ้งเตือน", "ไม่มีข้อมูลสมาชิก")
            mcombo.focus_set()

    savebutton = Button(app3, width=10,
                    text='บันทึก', command=writeborrow)
    savebutton.grid(column=1, row=7, sticky=E)

    def root3exit():
        root3.destroy()

    backbutton = Button(app3, width=10,
                    text='กลับ', command=root3exit)
    backbutton.grid(column=6, row=7, sticky=W)

    newborrow()
    root3.mainloop()
