from tkinter import *
from tkinter import messagebox

class OT:
    __rate = 300.0

    def getrate(self):
        return self.__rate

    def changerate(self, r):
        self.__rate = r

    def cal_ot(self, hour):
        return hour * self.__rate

class OTform:
    @staticmethod
    def myotform():
        root = Tk()
        root.title("ข้อมูลค่าล่วงเวลา")
        root.geometry('300x200')
        app = Frame(root)
        app.grid()

        blanklabel1 = Label(app, width=35)
        blanklabel1.grid(column=0,row=0, columnspan=2)

        hrlabel = Label(app, font=('tahoma', '11'), text="จำนวนชั่วโมง", width=10, anchor=W)

        hrlabel.grid(column=0, row=1)
        hrtext = StringVar()
        hrentry = Entry(app, font=('tahoma', '11'), textvariable=hrtext, bd=2, width=15)

        hrentry.grid(column=1, row=1)

        def hentry_keypress(event):
            w = event.widget
            if float(w.get()) < 40:
                rateentry.configure(state=NORMAL)
                ratetext.set('')
                anslabel['text'] = ''
                rateentry.focus_set()
            else:
                rateentry.configure(state=DISABLED)
                ratetext.set('0.0')
                calbutton.focus_set()
        hrentry.bind('<Return>', hentry_keypress)

        ratelabel = Label(app, font=('tahoma', '11'), text="ค่าแรงใหม่", width=10, anchor=W)

        ratelabel.grid(column=0, row=2)
        ratetext = StringVar()
        rateentry = Entry(app, font=('tahoma', '11'), textvariable=ratetext, state=DISABLED, bd=2, width=15)

        ratetext.set('0.0')
        rateentry.grid(column=1, row=2)

        def rateentry_keypress(event):
            w = event.widget
            if w.get() == '':
                messagebox.showinfo('แจ้งเตือน','ป้อนข้อมูลค่าแรงใหม่')
                w.focus_set()
            else:
                calbutton.focus_set()
        rateentry.bind('<Return>', rateentry_keypress)

        blanklabel3 = Label(app, font=('tahoma', '11'), width=35)
        blanklabel3.grid(column=0, row=3, columnspan=2)

        calbutton = Button(app, font=('tahoma', '11'), text="เข้าสู่ระบบ", width=10, command=lambda: setcaldata(calbutton))

        calbutton.grid(column=0,row=4)

        def calbutton_keypress(event):
            w = event.widget
            setcaldata(w)

        def setcaldata(w):
            o = OT()
            try:
                hr = float(hrentry.get())
                rate = float(rateentry.get())
            except ValueError:
                messagebox.showinfo("แจ้งเตือน", "ไม่สามารถเปลี่ยนข้อมูลเป็นจำนวนทศนิยม")

                rateentry.focus_set()
            else:
                if hr < 40 and rate != 0:
                    o.changerate(rate)
                ans = o.cal_ot(hr)
            anslabel['text'] = "รวมค่าแรง = " + '{0:,.2f}'.format(ans) + " บาท"

            w.focus_set()
        calbutton.bind('<Return>', calbutton_keypress)

        clearbutton = Button(app, font=('tahoma', '11'), text="ล้างข้อมูล", width=10, command=lambda: setcleardata())

        clearbutton.grid(column=1, row=4)
        blanklabel4 = Label(app, width=35)
        blanklabel4.grid(column=0, row=5, columnspan=2)
        anslabel = Label(app, font=('tahoma', '10', 'bold'), width=30, fg='blue', bg='yellow')

        anslabel.grid(column=0, row=6, columnspan=2)

        def setcleardata():
            hrtext.set('')
            ratetext.set('0.0')
            rateentry.configure(state=DISABLED)
            anslabel['text'] = ''
            hrentry.focus_set()

        root.mainloop()

ot_f = OTform()
ot_f.myotform()
