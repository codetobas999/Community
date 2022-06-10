from PyQt5.QtWidgets import QWidget, QMainWindow
from class_product import *
import productqryform


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = productqryform.Ui_Form()
        self.ui.setupUi(self)
        self.ui.closebutton.clicked.connect(self.close)
        self.loaddata()

    def loaddata(self):
        data = selectallproduct(1)
        msg = printproductqry(data)
        self.ui.showlist.setText(msg)
