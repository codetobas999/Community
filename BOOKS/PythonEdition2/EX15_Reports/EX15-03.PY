from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table, TableStyle
from tkinter import *

def openflie():
    filename = 'book.txt'
    try:
        with open(filename, 'r') as file:
            result = file.readlines()
        return result
    except IOError as e:
        print(e)
        file.close()
        return False

def opens():
        data = openflie()
        text1.delete(1.0, END)
        text1.insert(END, "=======================\n")
        text1.insert(END, "ID;NAME;STATUS\n")
        text1.insert(END, "=======================\n")
        for msg in data:
            if msg[len(msg)-2] == "0":
                result = msg[0:len(msg)-2] + "Occupied\n"
            if msg[len(msg)-2] == "1":
                result = msg[0:len(msg)-2] + "Available\n"
            text1.insert(END, result)
        text1.insert(END, "=======================\n")

def printpdf():
    pdfmetrics.registerFont(TTFont('THSarabun', 'THSarabunNew.ttf'))
    my_doc = SimpleDocTemplate('Tblfile.pdf', pagesize=A4)
    flowables = []
    tdata = []
    hdata = []
    bdata = []
    fdata = []
    tdata.clear()
    hdata.clear()
    bdata.clear()
    fdata.clear()
    tdata.append(["BOOK STATUS REPORT",'',''])
    t = Table(tdata, colWidths=120, rowHeights=20)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.yellow),
                                    ('TEXTCOLOR', (0,0), (-1,-1), colors.navy),
                                    ('TEXTFONT', (0, 0), (-1, -1), 'THSarabun'),
                                    ('ALIGN',(0,0),(-1,-1),'CENTER'),
                                    ('SPAN', (0,0), (2,0))]))
    flowables.append(t)
    msg = str(text1.get(1.0, END))
    data = msg.split("\n")
    for msg in data:
        if msg[0:2] == "ID":
            hdata.append(msg.split(';', 3))
        else:
            if msg != "" and msg[0] != "=":
                bdata.append(msg.split(';', 3))
    t = Table(hdata, colWidths=120, rowHeights=20)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.cyan),
                                    ('TEXTCOLOR', (0,0), (-1,-1), colors.navy),
                                    ('TEXTFONT', (0, 0), (-1, -1), 'THSarabun'),
                                    ('ALIGN',(0,0),(-1,-1),'CENTER')]))
    flowables.append(t)
    t = Table(bdata, colWidths=120, rowHeights=20, spaceBefore=10)
    t.setStyle(TableStyle([('TEXTCOLOR', (0,0), (-1,-1), colors.navy),
                                    ('TEXTFONT', (0, 0), (-1, -1), 'THSarabun'),
                                    ('ALIGN',(0,0),(-1,-1),'CENTER')]))
    flowables.append(t)
    fdata.append(["",'',''])
    t = Table(fdata, colWidths=120, rowHeights=5, spaceBefore=10)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.grey)]))
    flowables.append(t)
    my_doc.build(flowables)

root = Tk()
root.title("Table Report Example")
root.geometry("450x350")
root.option_add('*font', 'tahoma 12 bold')
frame = Frame(root)
frame.pack()
text1 = Text(frame, height=10)
text1.pack(padx=30, pady=30)
button1 = Button(frame, width= 20, text="LOAD", command=opens)
button1.pack(padx=10, pady=10)
button2 = Button(frame, width= 20, text="PRINT", command=printpdf)
button2.pack(padx=10, pady=10)
root.mainloop()
