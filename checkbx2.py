# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkbx2.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.checkBoxPizza = QtGui.QCheckBox(Dialog)
        self.checkBoxPizza.setGeometry(QtCore.QRect(110, 70, 85, 18))
        self.checkBoxPizza.setObjectName(_fromUtf8("checkBoxPizza"))
        self.checkBoxHotDog = QtGui.QCheckBox(Dialog)
        self.checkBoxHotDog.setGeometry(QtCore.QRect(110, 100, 91, 18))
        self.checkBoxHotDog.setObjectName(_fromUtf8("checkBoxHotDog"))
        self.checkBoxFries = QtGui.QCheckBox(Dialog)
        self.checkBoxFries.setGeometry(QtCore.QRect(110, 130, 85, 18))
        self.checkBoxFries.setObjectName(_fromUtf8("checkBoxFries"))
        self.checkBoxChickeBurger = QtGui.QCheckBox(Dialog)
        self.checkBoxChickeBurger.setGeometry(QtCore.QRect(110, 160, 141, 18))
        self.checkBoxChickeBurger.setObjectName(_fromUtf8("checkBoxChickeBurger"))
        self.lineEditAmount = QtGui.QLineEdit(Dialog)
        self.lineEditAmount.setGeometry(QtCore.QRect(120, 210, 191, 21))
        self.lineEditAmount.setObjectName(_fromUtf8("lineEditAmount"))
        self.labelHeading = QtGui.QLabel(Dialog)
        self.labelHeading.setGeometry(QtCore.QRect(100, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelHeading.setFont(font)
        self.labelHeading.setObjectName(_fromUtf8("labelHeading"))
        self.labelAmount = QtGui.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(30, 220, 81, 20))
        self.labelAmount.setObjectName(_fromUtf8("labelAmount"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.checkBoxPizza.setText(_translate("Dialog", "Pizza $20", None))
        self.checkBoxHotDog.setText(_translate("Dialog", "Hot Dog $5", None))
        self.checkBoxFries.setText(_translate("Dialog", "Fries $10", None))
        self.checkBoxChickeBurger.setText(_translate("Dialog", "Chicken Burger $15", None))
        self.labelHeading.setText(_translate("Dialog", "XYS Food Corner", None))
        self.labelAmount.setText(_translate("Dialog", "Total Amount", None))

