from cakeform import *
from addform import *
from listform import *


def maindata():

    def cake():
        root1.destroy()
        cakedata()
        maindata()

    def adds():
        root1.destroy()
        adddata()
        maindata()

    def lists():
        root1.destroy()
        listdata()
        maindata()

    root1 = Tk()
    root1.title('หน้าแรก')
    root1.geometry('275x200')
    root1.grid()
    app1 = Frame(root1)
    app1.pack()
    blanklabel = Label(app1, height=1)
    blanklabel.pack()
    button1 = Button(app1, font=('tahoma', '12', 'bold'), text='เพิ่มรายการสินค้า',
                     height=1, width=20, command=cake)
    button1.pack()
    button2 = Button(app1, font=('tahoma', '12', 'bold'), text='เพิ่มจำนวนสินค้า',
                     height=1, width=20, command=adds)
    button2.pack()
    button3 = Button(app1, font=('tahoma', '12', 'bold'), text='รายงานสินค้า',
                     height=1, width=20, command=lists)
    button3.pack()
    button4 = Button(app1, font=('tahoma', '12', 'bold'), text='ออกจากระบบ',
                     height=1, width=20, command=sys.exit)
    button4.pack()
    root1.mainloop()


createdatabase()
createtable()
maindata()
