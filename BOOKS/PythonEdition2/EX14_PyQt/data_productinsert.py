import os
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox, QFileDialog
from PyQt5 import QtGui
from class_product import *
import productinsertform


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = productinsertform.Ui_Form()
        self.ui.setupUi(self)
        self.ui.closebutton.clicked.connect(self.close)
        self.ui.savebutton.clicked.connect(self.savedata)
        self.ui.browsebutton.clicked.connect(self.getpic)
        self.getpdata()

    def getpdata(self):
        data = selectlastproductid()
        pid = 0
        if data != 0:
            pid = str(data)[1:]
        pid = str(int(pid) + 1)
        if len(pid) == 1:
            pid = 'P00' + pid
        if len(pid) == 2:
            pid = 'P0' + pid
        if len(pid) == 3:
            pid = 'P' + pid
        self.ui.itext.setText(pid)
        self.ui.ntext.clear()
        self.ui.qtext.clear()
        self.ui.ctext.clear()
        self.ui.pictext.clear()
        self.ui.piclabel.setPixmap(QtGui.QPixmap('None'))
        self.ui.piclabel.setText('Picture File')
        self.ui.ntext.setFocus()

    def getpic(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', 'pic/')
        filename = filename[0]
        start = filename.find("pic/", 1) + 4
        stop = len(filename)
        picname = filename[start:stop]
        self.ui.pictext.setText(picname)
        self.ui.piclabel.setPixmap(QtGui.QPixmap(filename))

    def savedata(self):
        pid = self.ui.itext.text()
        pname = self.ui.ntext.text()
        qtyA = self.ui.qtext.text()
        pcost = self.ui.ctext.text()
        ppic = self.ui.pictext.text()
        insertproduct(pid, pname, qtyA, pcost, ppic)
        QMessageBox.information(self, 'info', 'Data Inserted')
        self.getpdata()
