# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employeeinsertform.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 218)
        self.plabel = QtWidgets.QLabel(Form)
        self.plabel.setGeometry(QtCore.QRect(40, 80, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.plabel.setFont(font)
        self.plabel.setObjectName("plabel")
        self.tlabel = QtWidgets.QLabel(Form)
        self.tlabel.setGeometry(QtCore.QRect(260, 25, 37, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tlabel.setFont(font)
        self.tlabel.setObjectName("tlabel")
        self.ulabel = QtWidgets.QLabel(Form)
        self.ulabel.setGeometry(QtCore.QRect(40, 25, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ulabel.setFont(font)
        self.ulabel.setObjectName("ulabel")
        self.tcombo = QtWidgets.QComboBox(Form)
        self.tcombo.setGeometry(QtCore.QRect(310, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tcombo.setFont(font)
        self.tcombo.setObjectName("tcombo")
        self.ptext = QtWidgets.QLineEdit(Form)
        self.ptext.setGeometry(QtCore.QRect(130, 70, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.ptext.setFont(font)
        self.ptext.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ptext.setObjectName("ptext")
        self.closebutton = QtWidgets.QPushButton(Form)
        self.closebutton.setGeometry(QtCore.QRect(330, 120, 87, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.closebutton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebutton.setIcon(icon)
        self.closebutton.setIconSize(QtCore.QSize(16, 16))
        self.closebutton.setObjectName("closebutton")
        self.savebutton = QtWidgets.QPushButton(Form)
        self.savebutton.setGeometry(QtCore.QRect(230, 120, 87, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.savebutton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.savebutton.setIcon(icon1)
        self.savebutton.setIconSize(QtCore.QSize(16, 16))
        self.savebutton.setObjectName("savebutton")
        self.utext = QtWidgets.QLineEdit(Form)
        self.utext.setEnabled(False)
        self.utext.setGeometry(QtCore.QRect(130, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.utext.setFont(font)
        self.utext.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.utext.setObjectName("utext")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Employee Form: insert"))
        self.plabel.setText(_translate("Form", "password"))
        self.tlabel.setText(_translate("Form", "Type"))
        self.ulabel.setText(_translate("Form", "username"))
        self.closebutton.setText(_translate("Form", "Close"))
        self.savebutton.setText(_translate("Form", "Save"))
        self.savebutton.setShortcut(_translate("Form", "Enter"))
