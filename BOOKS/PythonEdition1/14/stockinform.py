# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stockinform.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(914, 514)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        self.plist = QtWidgets.QListWidget(Form)
        self.plist.setGeometry(QtCore.QRect(490, 50, 391, 381))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.plist.setFont(font)
        self.plist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plist.setObjectName("plist")
        self.plabel = QtWidgets.QLabel(Form)
        self.plabel.setGeometry(QtCore.QRect(490, 30, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.plabel.setFont(font)
        self.plabel.setObjectName("plabel")
        self.ilabel = QtWidgets.QLabel(Form)
        self.ilabel.setGeometry(QtCore.QRect(30, 40, 50, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ilabel.setFont(font)
        self.ilabel.setObjectName("ilabel")
        self.blabel = QtWidgets.QLabel(Form)
        self.blabel.setGeometry(QtCore.QRect(270, 110, 50, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.blabel.setFont(font)
        self.blabel.setObjectName("blabel")
        self.btext = QtWidgets.QTextBrowser(Form)
        self.btext.setEnabled(False)
        self.btext.setGeometry(QtCore.QRect(330, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btext.setFont(font)
        self.btext.setReadOnly(False)
        self.btext.setObjectName("btext")
        self.alabel = QtWidgets.QLabel(Form)
        self.alabel.setGeometry(QtCore.QRect(30, 110, 50, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.alabel.setFont(font)
        self.alabel.setObjectName("alabel")
        self.tlabel = QtWidgets.QLabel(Form)
        self.tlabel.setGeometry(QtCore.QRect(30, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tlabel.setFont(font)
        self.tlabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tlabel.setWordWrap(False)
        self.tlabel.setObjectName("tlabel")
        self.atext = QtWidgets.QTextBrowser(Form)
        self.atext.setEnabled(False)
        self.atext.setGeometry(QtCore.QRect(110, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.atext.setFont(font)
        self.atext.setReadOnly(False)
        self.atext.setObjectName("atext")
        self.ntext = QtWidgets.QTextBrowser(Form)
        self.ntext.setEnabled(False)
        self.ntext.setGeometry(QtCore.QRect(330, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ntext.setFont(font)
        self.ntext.setReadOnly(False)
        self.ntext.setObjectName("ntext")
        self.itext = QtWidgets.QTextBrowser(Form)
        self.itext.setEnabled(False)
        self.itext.setGeometry(QtCore.QRect(110, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.itext.setFont(font)
        self.itext.setReadOnly(False)
        self.itext.setObjectName("itext")
        self.nlabel = QtWidgets.QLabel(Form)
        self.nlabel.setGeometry(QtCore.QRect(270, 40, 50, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.nlabel.setFont(font)
        self.nlabel.setObjectName("nlabel")
        self.savebutton = QtWidgets.QPushButton(Form)
        self.savebutton.setGeometry(QtCore.QRect(250, 390, 93, 41))
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
        self.closebutton.setGeometry(QtCore.QRect(360, 390, 93, 41))
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
        self.r1 = QtWidgets.QRadioButton(Form)
        self.r1.setGeometry(QtCore.QRect(130, 400, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.r1.setFont(font)
        self.r1.setObjectName("r1")
        self.r2 = QtWidgets.QRadioButton(Form)
        self.r2.setGeometry(QtCore.QRect(190, 400, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.r2.setFont(font)
        self.r2.setObjectName("r2")
        self.qlabel = QtWidgets.QLabel(Form)
        self.qlabel.setGeometry(QtCore.QRect(30, 250, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.qlabel.setFont(font)
        self.qlabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.qlabel.setObjectName("qlabel")
        self.qtext = QtWidgets.QTextBrowser(Form)
        self.qtext.setGeometry(QtCore.QRect(110, 240, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.qtext.setFont(font)
        self.qtext.setReadOnly(False)
        self.qtext.setObjectName("qtext")
        self.typelabel = QtWidgets.QLabel(Form)
        self.typelabel.setGeometry(QtCore.QRect(30, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.typelabel.setFont(font)
        self.typelabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.typelabel.setWordWrap(False)
        self.typelabel.setObjectName("typelabel")
        self.piclabel = QtWidgets.QLabel(Form)
        self.piclabel.setGeometry(QtCore.QRect(270, 170, 191, 191))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.piclabel.setFont(font)
        self.piclabel.setStyleSheet("background-color:rgb(227, 227, 227);")
        self.piclabel.setScaledContents(True)
        self.piclabel.setAlignment(QtCore.Qt.AlignCenter)
        self.piclabel.setObjectName("piclabel")
        self.idate = QtWidgets.QDateEdit(Form)
        self.idate.setGeometry(QtCore.QRect(109, 170, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.idate.setFont(font)
        self.idate.setTimeSpec(QtCore.Qt.LocalTime)
        self.idate.setObjectName("idate")
        self.clabel = QtWidgets.QLabel(Form)
        self.clabel.setGeometry(QtCore.QRect(30, 320, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.clabel.setFont(font)
        self.clabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.clabel.setObjectName("clabel")
        self.ctext = QtWidgets.QTextBrowser(Form)
        self.ctext.setGeometry(QtCore.QRect(110, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ctext.setFont(font)
        self.ctext.setReadOnly(False)
        self.ctext.setObjectName("ctext")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Product Form: stock in"))
        self.plabel.setText(_translate("Form", "Product List"))
        self.ilabel.setText(_translate("Form", "ID"))
        self.blabel.setText(_translate("Form", "@B"))
        self.alabel.setText(_translate("Form", "@A"))
        self.tlabel.setText(_translate("Form", "in date"))
        self.nlabel.setText(_translate("Form", "Name"))
        self.savebutton.setText(_translate("Form", "Save"))
        self.savebutton.setShortcut(_translate("Form", "Enter"))
        self.closebutton.setText(_translate("Form", "Close"))
        self.r1.setText(_translate("Form", "A"))
        self.r2.setText(_translate("Form", "B"))
        self.qlabel.setText(_translate("Form", "quantity"))
        self.typelabel.setText(_translate("Form", "stock in =>"))
        self.piclabel.setText(_translate("Form", "Picture File"))
        self.idate.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.clabel.setText(_translate("Form", "cost"))
