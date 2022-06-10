from PyQt5.QtWidgets import QWidget, QMainWindow
from module_product import *
import productqryform


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = productqryform.Ui_Form()
        self.ui.setupUi(self)
        self.ui.closebutton.clicked.connect(self.close)
        self.load_data()

    def load_data(self):
        data = selectallproduct(1)
        msg = printproductqry(data)
        self.ui.showlist.setText(msg)
