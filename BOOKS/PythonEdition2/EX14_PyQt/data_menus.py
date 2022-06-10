import sys

from PyQt5.QtWidgets import QWidget, QMainWindow
import menusform
import data_productinsert
import data_productupdate
import data_productqry
import data_stockininsert
import data_stockinqry
import data_empinsert
import data_empqry
import data_empupdate


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = menusform.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.closebutton.clicked.connect(self.exits)
        self.ui.pinsertbutton.clicked.connect(self.get_productinsert_form)
        self.ui.pqrybutton.clicked.connect(self.get_productqry_form)
        self.ui.stinsertbutton.clicked.connect(self.get_stockininsert_form)
        self.ui.stqrybutton.clicked.connect(self.get_stockinqry_form)
        self.ui.empinsertbutton.clicked.connect(self.get_empinsert_form)
        self.ui.empqrybutton.clicked.connect(self.get_empqry_form)
        self.ui.actionproduct.triggered.connect(self.get_productupdate_form)
        self.ui.actionemployee.triggered.connect(self.get_empupdate_form)

    def get_windowtitle(self):
        mid = MyApp.windowTitle(self)
        mid = mid.split(' by ', 2)
        return mid[1]

    def get_productinsert_form(self):
        productinsert_app = data_productinsert.MyApp(self)
        productinsert_app.show()

    def get_productqry_form(self):
        productqry_app = data_productqry.MyApp(self)
        productqry_app.show()

    def get_stockininsert_form(self):
        stockininsert_app = data_stockininsert.MyApp(self)
        empid = self.get_windowtitle()
        stockininsert_app.ui.emptext.setText(empid)
        stockininsert_app.show()

    def get_stockinqry_form(self):
        stockinqry_app = data_stockinqry.MyApp(self)
        stockinqry_app.show()

    def get_empinsert_form(self):
        empinsert_app = data_empinsert.MyApp(self)
        empinsert_app.show()

    def get_empqry_form(self):
        empqry_app = data_empqry.MyApp(self)
        empqry_app.show()

    def get_productupdate_form(self):
        productupdate_app = data_productupdate.MyApp(self)
        productupdate_app.show()

    def get_empupdate_form(self):
        empupdate_app = data_empupdate.MyApp(self)
        empupdate_app.show()

    @staticmethod
    def exits():
        sys.exit(0)
