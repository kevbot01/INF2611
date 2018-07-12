# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spinner.ui'
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
        self.labelFirstValue = QtGui.QLabel(Dialog)
        self.labelFirstValue.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.labelFirstValue.setObjectName(_fromUtf8("labelFirstValue"))
        self.labelSecondValue = QtGui.QLabel(Dialog)
        self.labelSecondValue.setGeometry(QtCore.QRect(10, 120, 121, 16))
        self.labelSecondValue.setObjectName(_fromUtf8("labelSecondValue"))
        self.spinBoxFirstValue = QtGui.QSpinBox(Dialog)
        self.spinBoxFirstValue.setGeometry(QtCore.QRect(140, 50, 53, 24))
        self.spinBoxFirstValue.setObjectName(_fromUtf8("spinBoxFirstValue"))
        self.doubleSpinBoxSecondValue = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxSecondValue.setGeometry(QtCore.QRect(140, 110, 62, 24))
        self.doubleSpinBoxSecondValue.setObjectName(_fromUtf8("doubleSpinBoxSecondValue"))
        self.lineEditFirstValue = QtGui.QLineEdit(Dialog)
        self.lineEditFirstValue.setGeometry(QtCore.QRect(270, 50, 113, 21))
        self.lineEditFirstValue.setObjectName(_fromUtf8("lineEditFirstValue"))
        self.lineEditSecondValue = QtGui.QLineEdit(Dialog)
        self.lineEditSecondValue.setGeometry(QtCore.QRect(270, 110, 113, 21))
        self.lineEditSecondValue.setObjectName(_fromUtf8("lineEditSecondValue"))
        self.pushButtonAdd = QtGui.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(140, 210, 110, 32))
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelFirstValue.setText(_translate("Dialog", "Select first value", None))
        self.labelSecondValue.setText(_translate("Dialog", "Select second value", None))
        self.pushButtonAdd.setText(_translate("Dialog", "Add", None))

