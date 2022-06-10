from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from tkinter import *
from tkinter import simpledialog

def openfile():
    filename = 'borrow.txt'
    try:
        with open(filename, 'r') as file:
            result = file.readlines()
        return result
    except IOError as e:
        print(e)
        file.close()
        return False

def opens():
        data = openfile()
        text1.delete(1.0, END)
        text1.insert(END, "=============================\n")
        text1.insert(END, "slipNo;memberID;bookID;bookName\n")
        text1.insert(END, "=============================\n")
        for msg in data:
            text1.insert(END, msg[0:len(msg)-3] + "\n")
        text1.insert(END, "=============================\n")

def printpdf(sno):
    pdfmetrics.registerFont(TTFont('THSarabun', 'THSarabunNew.ttf'))
    c = canvas.Canvas('Cvasfile.pdf', pagesize=A4)
    c.setFont("THSarabun", 14)

    c.drawString(100, 750, "เลขที่การยืม")
    c.drawString(180, 750, sno)

    bdata = [["รหัสหนังสือ", "ชื่อหนังสือ"]]
    msg = str(text1.get(4.0, END))
    data = msg.split("\n")
    mno = ''
    for msg in data:
            umsg = msg.split(';', 4)
            if umsg[0] == sno:
                umsg = [umsg[2], umsg[3]]
                bdata.append(umsg)
                mno = msg[6:10]

    c.drawString(100, 730, "รหัสสมาชิก")
    c.drawString(180, 730, mno)

    c.line( 80, 765, 250, 765)
    c.line( 80, 765,  80, 725)
    c.line( 80, 725, 250, 725)
    c.line(250, 765, 250, 725)

    i = 700
    for msg in bdata:
        c.drawString(90, i, msg[0])
        c.drawString(180, i, msg[1])
        i = i - 20

    c.line(80, i, 250, i)
    c.line(80, i+2, 250, i+2)
    c.line( 80, 725, 80, i)
    c.line(250, 725, 250, i)

    c.save()

def prints():
    sno = simpledialog.askstring('คำค้น', 'คำค้น')
    printpdf(sno)

root = Tk()
root.title("Canvas Report Example")
root.geometry("450x350")
root.option_add('*font', 'tahoma 12 bold')
frame = Frame(root)
frame.pack()
text1 = Text(frame, height=10)
text1.pack(padx=30, pady=30)
button1 = Button(frame, width= 20, text="LOAD", command=opens)
button1.pack(padx=10, pady=10)
button2 = Button(frame, width= 20, text="PRINT", command=prints)
button2.pack(padx=10, pady=10)
root.mainloop()
