from PyQt5.QtWidgets import QWidget, QMainWindow
from class_stockin import *
import stockinqryform


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = stockinqryform.Ui_Form()
        self.ui.setupUi(self)
        self.ui.closebutton.clicked.connect(self.close)
        self.loaddata()

    def loaddata(self):
        data = selectallstockin(1)
        msg = printstockinqry(data)
        self.ui.showlist.setText(msg)
