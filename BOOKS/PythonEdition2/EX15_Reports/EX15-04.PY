from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from tkinter import *
import pymysql

def openfile():
    host = "localhost"
    user = "root"
    pw = ""
    dbname = "cakesDB"
    conn = pymysql.connect(host, user, pw, dbname)
    cur = conn.cursor()
    sql = "SELECT * FROM product"
    try:
        cur.execute(sql)
        data = cur.fetchall()
        result = []
        for row in data:
            result.append(str(row[0]) + ';' + row[1] + ';' + str(row[2]) + "\n")
        return result
    except Exception as e:
        print(e)
    conn.close()

def opens():
    data = openfile()
    text1.delete(1.0, END)
    text1.insert(END, "=================\n")
    text1.insert(END, "ID;NAME;QUANTITY\n")
    text1.insert(END, "=================\n")
    for msg in data:
        text1.insert(END, msg)
    text1.insert(END, "=================\n")
    return data

def printpdf():
    pdfmetrics.registerFont(TTFont('Times', 'times.ttf'))
    doc = SimpleDocTemplate("GrFile.pdf", pagesize=A4)
    flowables = []
    tdata = []
    hdata = []
    bdata = []
    fdata = []
    tdata.clear()
    hdata.clear()
    bdata.clear()
    fdata.clear()
    tdata.append(["CAKE INVENTORY QUANTITY REPORT", '', ''])
    t = Table(tdata, colWidths=120, rowHeights=20)
    t.setStyle(TableStyle([('TEXTCOLOR', (0,0), (-1,-1),colors.navy),
                                    ('BACKGROUND',(0,0),(-1,-1),colors.yellow),
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
                                    ('ALIGN',(0,0),(-1,-1),'CENTER')]))
    flowables.append(t)
    t = Table(bdata, colWidths=120, rowHeights=20, spaceBefore=10)
    t.setStyle(TableStyle([('TEXTCOLOR', (0,0), (-1,-1), colors.navy),
                                    ('ALIGN',(0,0),(-1,-1),'CENTER')]))
    flowables.append(t)
    fdata.append(["",'',''])
    t = Table(fdata, colWidths=120, rowHeights=5, spaceBefore=10, spaceAfter=20)

    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.grey)]))
    flowables.append(t)
    d1 = Drawing(400, 200)
    pc = Pie()
    pc.x = 150
    pc.y = 50
    pc.width = 120
    pc.height = 100
    pc.simpleLabels = 1
    pc.sideLabels = 1
    pc.data.clear()
    data1 = []
    msg = str(text1.get(1.0, END))
    data = msg.split("\n")
    for msg in data:
        if msg[0:2] == "ID":
            hdata.append(msg.split(';', 3))
        else:
            if msg != "" and msg[0] != "=":
                bmsg = msg.split(';', 3)
                bdata.append(bmsg)
                data1.append(bmsg[1])
                data2 = int(bmsg[2])
                pc.labels = data1
                pc.data.append(data2)
    data = [pc.labels, pc.data]
    t = Table(data)
    t.setStyle(TableStyle([
                        ('FONTNAME', (0,0), (-1,-1), 'Times'),
                        ('FONTSIZE', (0,0), (-1,-1), 12),
                        ('ALIGN',(0,0),(-1,-1),'CENTER'),
                        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
                        ('BOX', (0,0), (-1,-1), 0.25, colors.black)]))
    flowables.append(t)
    d1.add(pc)
    flowables.append(d1)
    d2 = Drawing(400, 200)
    bc = VerticalBarChart()
    bc.data.clear()
    data1 = []
    data2 = []

    msg = str(text1.get(4.0, END))
    data = msg.split("\n")
    for msg in data:
            if msg != "" and msg[0] != "=":
                umsg = msg.split(';', 3)
                data1.append(umsg[1])
                data2.append(int(umsg[2]))
    data = list()
    data.append(tuple(data2))
    bc.data = data
    bc.x = 25
    bc.y = 25
    bc.height = 200
    bc.width = 400
    bc.valueAxis.valueMin = 0
    bc.valueAxis.valueMax = 50
    bc.valueAxis.valueStep = 10
    bc.categoryAxis.labels.boxAnchor = 'ne'
    bc.categoryAxis.labels.dx = 8
    bc.categoryAxis.labels.dy = 1
    bc.barLabels.fontSize = 8
    bc.barLabels.fillColor = colors.black
    bc.barLabelFormat = '%d'
    bc.barLabels.nudge = 7
    bc.barWidth = 5
    bc.categoryAxis.labels.angle = 30
    bc.categoryAxis.categoryNames = data1
    for i in range (0, len(data2)):
        if i%3 == 0:
            bc.bars[(0, i)].fillColor = colors.blue
        if i%3 == 1:
            bc.bars[(0, i)].fillColor = colors.green
        if i%3 == 2:
            bc.bars[(0, i)].fillColor = colors.red
    d2.add(bc)
    flowables.append(d2)
    doc.build(flowables)

root = Tk()
root.title("Graph Report Example")
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
