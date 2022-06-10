from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from class_emp import *
import employeeupdateform


class MyApp(QMainWindow):
    idx = 0
    active = 1

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = employeeupdateform.Ui_Form()
        self.ui.setupUi(self)

        self.ui.datalist.itemSelectionChanged.connect(self.showmdata)
        self.ui.datalist.doubleClicked.connect(self.deletedata)
        self.ui.savebutton.clicked.connect(self.savedata)
        self.ui.closebutton.clicked.connect(self.close)
        self.getmdata()

    def getmdata(self):
        data = selectallemployee(0)
        self.ui.datalist.clear()
        count = 1
        for row in data:
            if count > 3:
                if count < len(data)-3:
                    self.ui.datalist.insertItem(count, str(row))
            count = count + 1
        self.ui.tcombo.clear()
        self.ui.tcombo.addItem('admin')
        self.ui.tcombo.addItem('user')
        self.ui.datalist.setCurrentRow(MyApp.idx)

    def showmdata(self):
        msg = ""
        data = self.ui.datalist.selectedItems()
        for row in data:
            msg = row.text()

        data = msg.split(' ', 4)
        data0 = data[0][1:len(data[0])-1]
        data1 = data[1][1:len(data[1])-1]
        data2 = data[2][1:len(data[2])-1]
        MyApp.active = data[3][1:len(data[3])-1]

        self.ui.utext.setText(data0)
        self.ui.ptext.setText(data1)
        self.ui.tcombo.setCurrentText(data2)

    def deletedata(self):
        empid = self.ui.utext.text()
        if MyApp.active == 'active':
            msg = 'Delete '
            active = 1
        else:
            msg = 'Delete inactive '
            active = 0

        resp = QMessageBox.question(self, 'confirm', msg + 'Data ?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resp == QMessageBox.Yes:
            deleteemployee(empid, active)
            self.close()
            MyApp.idx = self.ui.datalist.currentRow()
            MyApp(self).show()

    def savedata(self):
        empid = self.ui.utext.text()
        emppw = self.ui.ptext.text()
        emptype = self.ui.tcombo.currentIndex()
        updateemployee(empid, emppw, (emptype+1))
        QMessageBox.information(self, 'info', 'Data Updated')
        self.close()
        MyApp.idx = self.ui.datalist.currentRow()
        MyApp(self).show()
