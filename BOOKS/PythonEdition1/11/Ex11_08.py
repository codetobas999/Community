from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

class Product:
    def __init__(self, taxrate, deliveryrate):
        self.taxrate = taxrate
        self.deliveryrate = deliveryrate

    def cal_delivery(self, price, extra=None):
        if extra is None:
            return self.deliveryrate*price
        else:
            return self.deliveryrate*price + extra

    def cal_tax(self, price):
        return self.taxrate*price

class Prime(Product):
    pass

class Defect(Product):
    def cal_tax(self, price):
        return self.taxrate*price - 50

class Productform:
    @staticmethod
    def myproductform():
        root = Tk()
        root.title("ข้อมูลสินค้า")
        root.geometry('300x275')
        app = Frame(root)
        app.grid()

        blanklabel1 = Label(app, font=('tahoma', '11'), width=35)
        blanklabel1.grid(column=0,row=0, columnspan=2)
        pcombolabel = Label(app, font=('tahoma', '11'), text="ประเภทสินค้า", width=10, anchor=W)

        pcombolabel.grid(column=0, row=1, padx=5, pady=5)
        pcombo = Combobox(app, font=('tahoma', '11'), width=13, values=["Product Type", "Prime", "Defect"])

        pcombo.grid(column=1, row=1, padx=5, pady=5)
        pcombo.current(0)

        def pcombo_select(event):
            w = event.widget
            if w.get() == "Prime":
                extraentry.configure(state=NORMAL)
                pricetext.set('')
                extratext.set('')
                priceentry.focus_set()
            if w.get() == "Defect":
                extraentry.configure(state=DISABLED)
                pricetext.set('')
                extratext.set('0.0')
                priceentry.focus_set()
        pcombo.bind('<<ComboboxSelected>>', pcombo_select)

        pricelabel = Label(app, font=('tahoma', '11'), text="ราคาสินค้า", width=10, anchor=W)

        pricelabel.grid(column=0, row=2, padx=5, pady=5)
        pricetext = StringVar()
        priceentry = Entry(app, font=('tahoma', '11'),
                        textvariable=pricetext, bd=2, width=15)
        priceentry.grid(column=1, row=2, padx=5, pady=5)
        extralabel = Label(app, font=('tahoma', '11'),
                        text="เงินเพิ่ม", width=10, anchor=W)
        extralabel.grid(column=0, row=3, padx=5, pady=5)
        extratext = StringVar()
        extraentry = Entry(app, font=('tahoma', '11'),
                        textvariable=extratext, bd=2, width=15)
        extraentry.grid(column=1, row=3, padx=5, pady=5)
        blanklabel3 = Label(app, font=('tahoma', '11'), width=35)
        blanklabel3.grid(column=0, row=4, columnspan=2)
        calculatebutton = Button(app, font=('tahoma', '11'),
                             text="คำนวณ", width=10, command=lambda: setcalculatedata())

        calculatebutton.grid(column=0,row=5)
        clearbutton = Button(app, font=('tahoma', '11'),
                            text="ล้างข้อมูล", width=10, command=lambda: setcleardata())

        clearbutton.grid(column=1, row=5)
        blanklabel4 = Label(app, font=('tahoma', '11'), width=35)
        blanklabel4.grid(column=0, row=6, columnspan=2)
        taxlabel = Label(app, font=('tahoma', '10', 'bold'), width=30,
                     fg='blue', bg='yellow')
        taxlabel.grid(column=0, row=7, columnspan=2)
        dellabel = Label(app, font=('tahoma', '10', 'bold'), width=30,
                     fg='blue', bg='silver')
        dellabel.grid(column=0, row=8, columnspan=2)

        def setcalculatedata():
            try:
                if pcombo.get() == "Product Type":
                    messagebox.showinfo("แจ้งเตือน", "เลือกประเภทวิชาก่อน")
                    pcombo.focus_set()
                else:
                    price = float(priceentry.get())
                    extra = float(extraentry.get())
            except ValueError:
                messagebox.showinfo("แจ้งเตือน", "ไม่สามารถเปลี่ยนข้อมูลเป็นจำนวนทศนิยม")

                extraentry.focus_set()
            else:
                if pcombo.get() == 'Prime':
                    pr = Prime(0.07, 0.10)
                    tax = pr.cal_tax(price)
                    delivery = pr.cal_delivery(price, extra)
                if pcombo.get() == 'Defect':
                    df = Defect(0.03, 0.05)
                    tax = df.cal_tax(price)
                    delivery = df.cal_delivery(price)
                taxlabel['text'] = "ค่าภาษี = " + \
                                   '{0:,.2f}'.format(tax) + " บาท"
                dellabel['text'] = "ค่าขนส่ง = " + \
                                   '{0:,.2f}'.format(delivery) + " บาท"
                calculatebutton.focus_set()

        def setcleardata():
            pcombo.current(0)
            pricetext.set('')
            extratext.set('')
            taxlabel['text'] = ''
            dellabel['text'] = ''
            pcombo.focus_set()

        root.mainloop()

product_f = Productform()
product_f.myproductform()
