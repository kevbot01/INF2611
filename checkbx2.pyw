import sys
from checkbx2 import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.checkBoxPizza, QtCore.SIGNAL('clicked()'), self.calculate)
        QtCore.QObject.connect(self.ui.checkBoxHotDog, QtCore.SIGNAL('clicked()'), self.calculate)
        QtCore.QObject.connect(self.ui.checkBoxFries, QtCore.SIGNAL('clicked()'), self.calculate)
        QtCore.QObject.connect(self.ui.checkBoxChickeBurger, QtCore.SIGNAL('clicked()'), self.calculate)

    @QtCore.pyqtSlot()
    def calculate(self):
        total = 0

        if self.ui.checkBoxPizza.isChecked():
            total += 20
        if self.ui.checkBoxHotDog.isChecked():
            total += 5
        if self.ui.checkBoxFries.isChecked():
            total += 10
        if self.ui.checkBoxChickeBurger.isChecked():
            total += 15

        self.ui.lineEditAmount.setText(str(total))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
