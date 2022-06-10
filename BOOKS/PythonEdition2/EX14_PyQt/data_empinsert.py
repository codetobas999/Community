from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from class_emp import *
import random
import employeeinsertform


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = employeeinsertform.Ui_Form()
        self.ui.setupUi(self)
        self.ui.closebutton.clicked.connect(self.close)
        self.ui.savebutton.clicked.connect(self.savedata)
        self.getempdata()

    def getempdata(self):
        data = selectemployeeid()
        empid = 0
        if data != 0:
            empid = str(data)[1:]
        empid = str(int(empid) + 1)
        if len(empid) == 1:
            empid = 'E00' + empid
        if len(empid) == 2:
            empid = 'E0' + empid
        if len(empid) == 3:
            empid = 'E' + empid
        self.ui.utext.setText(empid)
        self.ui.tcombo.clear()
        self.ui.tcombo.addItem('admin')
        self.ui.tcombo.addItem('user')
        self.ui.tcombo.currentText = 'admin'
        pw = random.randrange(1000, 9999)
        self.ui.ptext.setText(str(pw))

    def savedata(self):
        empid = self.ui.utext.text()
        emppw = self.ui.ptext.text()
        emptype = self.ui.tcombo.currentIndex() + 1
        insertemployee(empid, emppw, emptype)
        QMessageBox.information(self, 'info', 'Data Inserted')
        self.close()
        data = selectallemployee(1)
        if len(data) > 8:
            self.show()
            self.getempdata()
        else:
            QMessageBox.information(self, 'info',
                                    'login data is ' + empid + ';' + emppw)
