from PyQt5.QtWidgets import QWidget, QMainWindow
from module_emp import *
import employeeqryform


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = employeeqryform.Ui_Form()
        self.ui.setupUi(self)
        self.ui.closebutton.clicked.connect(self.close)
        self.load_data()

    def load_data(self):
        data = selectallemployee(1)
        msg = printempqry(data)
        self.ui.showlist.setText(msg)
