# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IotApp-BAS.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyApp(object):
    def setupUi(self, MyApp):
        MyApp.setObjectName("MyApp")
        MyApp.setEnabled(True)
        MyApp.resize(581, 486)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/basketball-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MyApp.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MyApp)
        self.centralwidget.setObjectName("centralwidget")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(340, 50, 93, 28))
        self.btnStart.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.btnStart.setObjectName("btnStart")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 41, 16))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 561, 361))
        self.groupBox.setObjectName("groupBox")
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setGeometry(QtCore.QRect(0, 20, 551, 371))
        self.listView.setObjectName("listView")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 161, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 41, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 50, 51, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.btnEnd = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnd.setGeometry(QtCore.QRect(450, 50, 93, 28))
        self.btnEnd.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.btnEnd.setObjectName("btnEnd")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 0, 211, 31))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        MyApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menubar.setObjectName("menubar")
        MyApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MyApp)
        self.statusbar.setObjectName("statusbar")
        MyApp.setStatusBar(self.statusbar)

        self.retranslateUi(MyApp)
        QtCore.QMetaObject.connectSlotsByName(MyApp)

    def retranslateUi(self, MyApp):
        _translate = QtCore.QCoreApplication.translate
        MyApp.setWindowTitle(_translate("MyApp", "IOT-GUI(BAS)"))
        self.btnStart.setText(_translate("MyApp", "เริ่ม"))
        self.label.setText(_translate("MyApp", "IP : "))
        self.groupBox.setTitle(_translate("MyApp", "รายการที่เรียกเข้ามา"))
        self.label_2.setText(_translate("MyApp", "Port : "))
        self.btnEnd.setText(_translate("MyApp", "จบ"))
        self.label_3.setText(_translate("MyApp", "<html><head/><body><p><span style=\" font-size:18pt;\">Socket Listener</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyApp = QtWidgets.QMainWindow()
    ui = Ui_MyApp()
    ui.setupUi(MyApp)
    MyApp.show()
    sys.exit(app.exec_())
