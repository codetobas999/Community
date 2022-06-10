from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import memberform
import sys


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = memberform.Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mapp = MyApp()
    mapp.show()
    sys.exit(app.exec_())
