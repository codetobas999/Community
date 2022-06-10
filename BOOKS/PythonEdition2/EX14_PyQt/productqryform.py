# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productqryform.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 550)
        self.showlist = QtWidgets.QTextBrowser(Form)
        self.showlist.setGeometry(QtCore.QRect(30, 20, 491, 481))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.showlist.setFont(font)
        self.showlist.setObjectName("showlist")
        self.closebutton = QtWidgets.QPushButton(Form)
        self.closebutton.setGeometry(QtCore.QRect(495, 510, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.closebutton.setFont(font)
        self.closebutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebutton.setIcon(icon)
        self.closebutton.setIconSize(QtCore.QSize(25, 25))
        self.closebutton.setObjectName("closebutton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Product List"))
