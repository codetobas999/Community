from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from PyQt5 import QtCore
from module_product import *
from module_stockin import *
import stockininsertform


class MyApp(QMainWindow):
    idx = 0    
    ppic = ''
    empid = ''
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = stockininsertform.Ui_Form()
        self.ui.setupUi(self)

        self.ui.closebutton.clicked.connect(self.close)
        self.ui.savebutton.clicked.connect(self.save_data)
        self.ui.datalist.itemSelectionChanged.connect(self.show_p_data)
        self.get_st_date()
        self.get_p_data()

    def get_st_date(self):
        if self.ui.emptext.setText(MyApp.empid) == '':
            self.ui.emptext.setText(MyApp.empid)
        self.ui.datetext.setDateTime(QtCore.QDateTime.currentDateTime())

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

    def show_p_data(self):
        data = self.ui.datalist.selectedItems()
        msg = ''
        for row in data:
            msg = row.text()

        data = msg.split(' ', 5)
        data0 = data[0][1:len(data[0])-1]
        data1 = data[1][1:len(data[1])-1]
        data2 = data[2][1:len(data[2])-1].replace(',', '')
        data3 = data[3][1:len(data[3])-1]
        data4 = data[4][1:len(data[4])-1]

        MyApp.ppic = data4
        self.ui.pitext.setText(data0)
        self.ui.pntext.setText(data1)
        self.ui.pqtext.setText(str(data2))
        self.ui.pctext.setText(str(data3))
        self.ui.qtext.setFocus()

    def save_data(self):
        MyApp.empid = self.ui.emptext.text()
        indate = self.ui.datetext.text()
        pid = self.ui.pitext.text()
        pname = self.ui.pntext.text()
        pqty = int(self.ui.pqtext.text())
        pcost = float(self.ui.pctext.text())

        stqty = int(self.ui.qtext.text())
        stcost = float(self.ui.costtext.text())

        newcost = ((pqty * pcost) + (stqty * stcost)) / (pqty + stqty)
        pqty = pqty + stqty

        insertstockin(indate, pid, MyApp.empid, stqty, stcost)
        updateproduct(pid, pname, pqty, newcost, MyApp.ppic)
        QMessageBox.information(self, 'info', 'Data Inserted')
        MyApp.idx = self.ui.datalist.currentRow()
        self.close()
        MyApp(self).show()
