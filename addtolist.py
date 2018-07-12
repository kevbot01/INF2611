# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtolist.ui'
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
        self.labelEnterCountry = QtGui.QLabel(Dialog)
        self.labelEnterCountry.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.labelEnterCountry.setObjectName(_fromUtf8("labelEnterCountry"))
        self.lineEditCountry = QtGui.QLineEdit(Dialog)
        self.lineEditCountry.setGeometry(QtCore.QRect(100, 10, 113, 21))
        self.lineEditCountry.setObjectName(_fromUtf8("lineEditCountry"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(220, 10, 171, 281))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButtonAdd = QtGui.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(50, 60, 110, 32))
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.pushButtonRemove = QtGui.QPushButton(Dialog)
        self.pushButtonRemove.setGeometry(QtCore.QRect(50, 110, 121, 32))
        self.pushButtonRemove.setObjectName(_fromUtf8("pushButtonRemove"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelEnterCountry.setText(_translate("Dialog", "Enter Country", None))
        self.pushButtonAdd.setText(_translate("Dialog", "Add Country", None))
        self.pushButtonRemove.setText(_translate("Dialog", "Remove Country", None))

