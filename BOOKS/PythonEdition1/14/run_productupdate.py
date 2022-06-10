from PyQt5.QtWidgets import QWidget, QMainWindow,  QMessageBox, QFileDialog
from PyQt5 import QtGui
from module_product import *
import productupdateform


class MyApp(QMainWindow):
    idx = 0
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = productupdateform.Ui_Form()
        self.ui.setupUi(self)

        self.ui.closebutton.clicked.connect(self.close)
        self.ui.savebutton.clicked.connect(self.save_data)
        self.ui.browsebutton.clicked.connect(self.getpic)
        self.ui.datalist.itemSelectionChanged.connect(self.show_p_data)
        self.get_p_data()

    def get_p_data(self):
        data = selectallproduct(2)
        self.ui.datalist.clear()
        count = 1
        for row in data:
            if count > 3:
                if count < len(data) - 3:
                    self.ui.datalist.insertItem(count, str(row))
            count = count + 1
        self.ui.datalist.setCurrentRow(MyApp.idx)

    def getpic(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', 'pic/')
        filename = filename[0]
        start = filename.find("pic/", 1) + 4
        stop = len(filename)
        picname = filename[start:stop]
        self.ui.pictext.setText(picname)
        self.ui.piclabel.setPixmap(QtGui.QPixmap(filename))

    def show_p_data(self):
        msg = ""
        data = self.ui.datalist.selectedItems()
        for row in data:
            msg = row.text()

        data = msg.split(' ', 6)
        data0 = data[0][1:len(data[0])-1]
        data1 = data[1][1:len(data[1])-1]
        data2 = data[2][1:len(data[2])-1].replace(',', '')
        data3 = data[3][1:len(data[3])-1]
        data4 = data[4][1:len(data[4])-1]
        filename = "pic/" + data4
        self.ui.piclabel.setPixmap(QtGui.QPixmap(filename))
        self.ui.pictext.setText(data4)
        self.ui.itext.setText(data0)
        self.ui.ntext.setText(data1)
        self.ui.qtext.setText(data2)
        self.ui.ctext.setText(data3)

    def save_data(self):
        pid = self.ui.itext.text()
        pname = self.ui.ntext.text()
        pqty = self.ui.qtext.text()
        pcost = self.ui.ctext.text()
        ppic = self.ui.pictext.text()
        updateproduct(pid, pname, pqty, pcost, ppic)
        QMessageBox.information(self, 'info', 'Data Updated')
        MyApp.idx = self.ui.datalist.currentRow()
        self.close()
        MyApp(self).show()

