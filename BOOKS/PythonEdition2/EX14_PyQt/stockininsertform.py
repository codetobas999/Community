# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stockininsertform.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(809, 385)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        self.savebutton = QtWidgets.QPushButton(Form)
        self.savebutton.setGeometry(QtCore.QRect(210, 310, 97, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.savebutton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.savebutton.setIcon(icon)
        self.savebutton.setIconSize(QtCore.QSize(16, 16))
        self.savebutton.setObjectName("savebutton")
        self.closebutton = QtWidgets.QPushButton(Form)
        self.closebutton.setGeometry(QtCore.QRect(320, 310, 97, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.closebutton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebutton.setIcon(icon1)
        self.closebutton.setIconSize(QtCore.QSize(16, 16))
        self.closebutton.setObjectName("closebutton")
        self.qlabel = QtWidgets.QLabel(Form)
        self.qlabel.setGeometry(QtCore.QRect(30, 240, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.qlabel.setFont(font)
        self.qlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.qlabel.setWordWrap(True)
        self.qlabel.setObjectName("qlabel")
        self.datalist = QtWidgets.QListWidget(Form)
        self.datalist.setGeometry(QtCore.QRect(440, 40, 341, 311))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.datalist.setFont(font)
        self.datalist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.datalist.setObjectName("datalist")
        self.datalabel = QtWidgets.QLabel(Form)
        self.datalabel.setGeometry(QtCore.QRect(440, 20, 361, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.datalabel.setFont(font)
        self.datalabel.setObjectName("datalabel")
        self.vline2 = QtWidgets.QFrame(Form)
        self.vline2.setGeometry(QtCore.QRect(30, 210, 381, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.vline2.setFont(font)
        self.vline2.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline2.setObjectName("vline2")
        self.qtext = QtWidgets.QLineEdit(Form)
        self.qtext.setGeometry(QtCore.QRect(100, 250, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.qtext.setFont(font)
        self.qtext.setObjectName("qtext")
        self.costtext = QtWidgets.QLineEdit(Form)
        self.costtext.setGeometry(QtCore.QRect(290, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.costtext.setFont(font)
        self.costtext.setObjectName("costtext")
        self.costlabel = QtWidgets.QLabel(Form)
        self.costlabel.setGeometry(QtCore.QRect(220, 240, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.costlabel.setFont(font)
        self.costlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.costlabel.setWordWrap(True)
        self.costlabel.setObjectName("costlabel")
        self.datelabel = QtWidgets.QLabel(Form)
        self.datelabel.setGeometry(QtCore.QRect(240, 45, 50, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.datelabel.setFont(font)
        self.datelabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.datelabel.setWordWrap(False)
        self.datelabel.setObjectName("datelabel")
        self.datetext = QtWidgets.QDateEdit(Form)
        self.datetext.setGeometry(QtCore.QRect(300, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.datetext.setFont(font)
        self.datetext.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.datetext.setTimeSpec(QtCore.Qt.LocalTime)
        self.datetext.setObjectName("datetext")
        self.pclabel = QtWidgets.QLabel(Form)
        self.pclabel.setGeometry(QtCore.QRect(230, 170, 50, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pclabel.setFont(font)
        self.pclabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.pclabel.setObjectName("pclabel")
        self.plabel = QtWidgets.QLabel(Form)
        self.plabel.setGeometry(QtCore.QRect(30, 80, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.plabel.setFont(font)
        self.plabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.plabel.setObjectName("plabel")
        self.pqlabel = QtWidgets.QLabel(Form)
        self.pqlabel.setGeometry(QtCore.QRect(40, 170, 50, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pqlabel.setFont(font)
        self.pqlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pqlabel.setObjectName("pqlabel")
        self.pitext = QtWidgets.QLineEdit(Form)
        self.pitext.setEnabled(False)
        self.pitext.setGeometry(QtCore.QRect(100, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.pitext.setFont(font)
        self.pitext.setObjectName("pitext")
        self.pctext = QtWidgets.QLineEdit(Form)
        self.pctext.setEnabled(False)
        self.pctext.setGeometry(QtCore.QRect(290, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.pctext.setFont(font)
        self.pctext.setObjectName("pctext")
        self.pnlabel = QtWidgets.QLabel(Form)
        self.pnlabel.setGeometry(QtCore.QRect(230, 130, 50, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pnlabel.setFont(font)
        self.pnlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.pnlabel.setObjectName("pnlabel")
        self.pntext = QtWidgets.QLineEdit(Form)
        self.pntext.setEnabled(False)
        self.pntext.setGeometry(QtCore.QRect(290, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.pntext.setFont(font)
        self.pntext.setObjectName("pntext")
        self.pilabel = QtWidgets.QLabel(Form)
        self.pilabel.setGeometry(QtCore.QRect(10, 130, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pilabel.setFont(font)
        self.pilabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pilabel.setObjectName("pilabel")
        self.vline1 = QtWidgets.QFrame(Form)
        self.vline1.setGeometry(QtCore.QRect(30, 100, 381, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.vline1.setFont(font)
        self.vline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline1.setObjectName("vline1")
        self.pqtext = QtWidgets.QLineEdit(Form)
        self.pqtext.setEnabled(False)
        self.pqtext.setGeometry(QtCore.QRect(100, 170, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.pqtext.setFont(font)
        self.pqtext.setObjectName("pqtext")
        self.emptext = QtWidgets.QLineEdit(Form)
        self.emptext.setEnabled(False)
        self.emptext.setGeometry(QtCore.QRect(140, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.emptext.setFont(font)
        self.emptext.setObjectName("emptext")
        self.emplabel = QtWidgets.QLabel(Form)
        self.emplabel.setGeometry(QtCore.QRect(10, 40, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.emplabel.setFont(font)
        self.emplabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.emplabel.setObjectName("emplabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stock in Form: insert"))
        self.savebutton.setText(_translate("Form", "Save"))
        self.savebutton.setShortcut(_translate("Form", "Enter"))
        self.closebutton.setText(_translate("Form", "Close"))
        self.qlabel.setText(_translate("Form", "Stock In Q\'ty"))
        self.datalabel.setText(_translate("Form", "Product List"))
        self.costlabel.setText(_translate("Form", "Stock In Cost"))
        self.datelabel.setText(_translate("Form", "Date"))
        self.datetext.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.pclabel.setText(_translate("Form", "Cost"))
        self.plabel.setText(_translate("Form", "Product Information"))
        self.pqlabel.setText(_translate("Form", "Q\'ty"))
        self.pnlabel.setText(_translate("Form", "Name"))
        self.pilabel.setText(_translate("Form", "ID"))
        self.emplabel.setText(_translate("Form", "Employee ID"))
