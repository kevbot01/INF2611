import sys
from spinner import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pushButtonAdd, QtCore.SIGNAL('clicked()'), self.calculate)

    @QtCore.pyqtSlot()
    def calculate(self):
        firstint = int(self.ui.spinBoxFirstValue.value())
        secondint = int(self.ui.doubleSpinBoxSecondValue.value())
        sumint = firstint + secondint
        self.ui.lineEditFirstValue.setText(str(sumint))
        firstfloat = float(self.ui.spinBoxFirstValue.value())
        secondfloat = float(self.ui.doubleSpinBoxSecondValue.value())
        sumfloat = firstfloat + secondfloat
        self.ui.lineEditSecondValue.setText(str(sumfloat))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())