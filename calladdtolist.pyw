import sys
from addtolist import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pushButtonAdd, QtCore.SIGNAL('clicked()'), self.addtolist)
        QtCore.QObject.connect(self.ui.pushButtonRemove, QtCore.SIGNAL('clicked()'), self.removefromlist)

    @QtCore.pyqtSlot()
    def addtolist(self):
        self.ui.listWidget.addItem(self.ui.lineEditCountry.text())
        self.ui.lineEditCountry.clear()
        self.ui.lineEditCountry.setFocus()

    @QtCore.pyqtSlot()
    def removefromlist(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())