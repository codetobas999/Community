from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
from bookfile import *


def returndata():
    root4 = Tk()
    root4.title('ทำรายการคืน')
    root4.geometry('450x400')
    root4.option_add('*font','tahoma 10')
    app4 = Frame(root4)
    app4.grid()

    blanklabel = Label(app4, width=10, text='ค้นหาด้วย', anchor=W)
    blanklabel.grid(column=0, row=0, columnspan=2)

    def getborrowlist():
        result = ''
        if var.get() == 1:
            result = searchborrow(1, searchname)
        if var.get() == 2:
            result = searchborrow(2, searchname)

        if not result or len(result) == 1:
            messagebox.showinfo('แจ้งเตือน', 'ไม่พบข้อมูลที่ต้องการค้นหา')
            var.set(None)
            r1.focus_set()
            return False

        listbox1.delete(0, END)
        for item in result:
            listbox1.insert(END, item)
        listbox1.focus_set()

    def getword():
        global searchname
        searchname = simpledialog.askstring('คำค้น', 'คำค้น')
        getborrowlist()

    var = IntVar()
    global r1
    r1 = Radiobutton(app4, text="รหัสสมาชิก",
                     variable=var, value=1, command=getword)
    r1.grid(column=1, row=1)
    r2 = Radiobutton(app4, text="เลขที่การยืม",
                     variable=var, value=2, command=getword)
    r2.grid(column=2, row=1)

    listbox1 = Listbox(app4, width=45, height=15)
    listbox1.grid(column=1, row=2, columnspan=2)
    scrolly = Scrollbar(app4, orient=VERTICAL,
                    command=listbox1.yview)
    scrolly.grid(column=3, row=2, sticky=NW+SW)
    listbox1.config(yscrollcommand=scrolly.set)

    def listbox1_select(event):
        w = event.widget
        data = int(w.curselection()[0])
        if data > 0:
            data = w.get(data)
            msg = str(data)
            msg = msg.split(';', 4)
            sno = msg[0]
            bookid = msg[2]
            status = 2
            msgbox = messagebox.askquestion('แจ้งเตือน', 'ต้องการคืนหนังสือรหัส ' + msg[2])

            if msgbox == 'yes':
                result = updatebookfile(bookid, status)
                if result:
                    result = updateborrowfile(sno, bookid)
                    if result:
                        messagebox.showinfo("แจ้งเตือน", "ทำรายการคืนสำเร็จ")
                        getborrowlist()

    listbox1.bind('<<ListboxSelect>>', listbox1_select)

    def root4exit():
        root4.destroy()

    backbutton = Button(app4, width=5, text='กลับ',
                    command=lambda: root4exit())
    backbutton.grid(column=4, row=2, sticky=S)

    root4.mainloop()






