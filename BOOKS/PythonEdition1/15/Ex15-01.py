from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from tkinter import *

def printpdf():
    pdfmetrics.registerFont(TTFont('THSarabun', 'THSarabunNew.ttf'))
    mydoc = SimpleDocTemplate('Parafile.pdf', pagesize=A4)
    flowables = []
    sample_style_sheet = getSampleStyleSheet()
    head_style = sample_style_sheet['Heading1']
    head_style.fontName = 'THSarabun'
    head_style.fontSize = 24
    body_style = sample_style_sheet['BodyText']
    body_style.fontName = 'THSarabun'
    body_style.fontSize = 16
    Headparagraph = Paragraph("mailto: python",  head_style)
    flowables.append(Headparagraph)
    msg = str(text1.get(1.0, END))
    data = msg.split("\n")
    flowables.append(Paragraph("="*30, body_style))
    flowables.append(Paragraph("\n", body_style))
    for i in range(0, len(data)-1):
        flowables.append(Paragraph(data[i], body_style))
    flowables.append(Paragraph("="*30, body_style))
    mydoc.build(flowables)

root = Tk()
root.title("Paragraph Report Example")
root.geometry("300x300")
root.option_add('*font', 'tahoma 10 bold')
frame = Frame(root)
frame.pack()
text1 = Text(frame, height=10)
text1.pack(padx=30, pady=30)
button1 = Button(frame, width= 20, text="PRINT", command=printpdf)
button1.pack(padx=10, pady=10)
root.mainloop()
