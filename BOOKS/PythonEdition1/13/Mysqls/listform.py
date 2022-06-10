from tkinter import *
from cakeDB import *

def listdata():

    def getlist():
        result = selectproducttable(1)
        listbox1.delete(0, END)
        for item in result:
            listbox1.insert(END, item)

    def root4exit():
        root4.destroy()

    root4 = Tk()
    root4.title('รายงานสินค้า')
    root4.geometry('475x450')
    root4.option_add('*font','tahoma 12')
    app4 = Frame(root4)
    app4.grid()

    blanklabel1 = Label(app4, width=5, height=1)
    blanklabel1.grid(column=0, row=0)
    blanklabel2 = Label(app4, width=30)
    blanklabel2.grid(column=1, row=0)
    listbox1 = Listbox(app4, height=15, width=40)
    listbox1.grid(column=1, row=1)
    scrolly = Scrollbar(app4, orient=VERTICAL,
                        command=listbox1.yview)
    scrolly.grid(column=2, row=1, sticky=NW+SW)
    listbox1.config(yscrollcommand=scrolly.set)
    blanklabel2 = Label(app4, width=30)
    blanklabel2.grid(column=1, row=2)
    backbutton = Button(app4, text='กลับ', width=10,
                        command=lambda: root4exit())
    backbutton.grid(column=1, row=3, sticky=E)

    getlist()
    root4.mainloop()
