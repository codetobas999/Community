from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets,QtGui
import sys

def window() :
    app=QApplication(sys.argv)
    window=QMainWindow()
    window.setGeometry(200,200,400,300)
    window.setWindowTitle("โปรแกรม Iot สำหรับ BAS")
    window.setMinimumSize(346,223)
    window.setMaximumSize(800,600)
    window.setWindowIcon(QtGui.QIcon("D:\\Forks\\github\\codetobas999\\Community\\LABS\\IOT\\LABS\\GUI\\imgs\\basketball-icon.png"))
    window.show()
    sys.exit(app.exec_())

window()

