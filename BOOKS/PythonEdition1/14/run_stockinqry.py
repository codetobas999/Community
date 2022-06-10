from PyQt5.QtWidgets import QWidget, QMainWindow
from module_stockin import *
import stockinqryform


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = stockinqryform.Ui_Form()
        self.ui.setupUi(self)
        self.ui.closebutton.clicked.connect(self.close)
        self.load_data()

    def load_data(self):
        data = selectallstockin()
        msg = printstockinqry(data)
        self.ui.showlist.setText(msg)
