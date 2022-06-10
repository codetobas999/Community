from class_create import *
from class_emp import *
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
import data_menus
import data_empinsert
import loginform
import sys


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = loginform.Ui_Form()
        self.ui.setupUi(self)

        self.ui.usertext.setText('E001')
        self.ui.pwtext.setText('6502')
        self.ui.loginbutton.clicked.connect(self.get_main_form)
        self.ui.closebutton.clicked.connect(self.close)
        self.get_emp_data()

    def get_emp_data(self):
        data = selectallemployee(1)
        if  len(data) == 4:
            QMessageBox.information(self, 'info', 'Add user data first')
            empinsert_app = data_empinsert.MyApp(self)
            empinsert_app.ui.tlabel.setVisible(False)
            empinsert_app.ui.tcombo.setVisible(False)
            empinsert_app.show()

    def get_main_form(self):
            empid = self.ui.usertext.text()
            emppw = self.ui.pwtext.text()
            data = selectemployee(empid, emppw)
            if not data:
                QMessageBox.information(self, 'info', 'Log in Fail')
                self.ui.usertext.setFocus()
            else:
                menu_app = data_menus.MyApp(self)
                empid = menu_app.windowTitle() + " by " + empid
                menu_app.setWindowTitle(empid)
                emptype = 0
                for row in data:
                    emptype = row[2]
                if emptype == 1:
                    menu_app.ui.empinsertbutton.setEnabled(True)
                    menu_app.ui.empqrybutton.setEnabled(True)
                    menu_app.ui.actionemployee.setEnabled(True)
                else:
                    menu_app.ui.empinsertbutton.setEnabled(False)
                    menu_app.ui.empqrybutton.setEnabled(False)
                    menu_app.ui.actionemployee.setEnabled(False)
                menu_app.show()


if __name__ == '__main__':
    createTable()
    app = QApplication(sys.argv)
    login_app = MyApp()
    login_app.show()
    sys.exit(app.exec_())
