import sys
from PyQt4 import QtCore, QtGui, uic
from main_auto import *
import open_mod as o
import save_mod


class Main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL('triggered()'), self.open)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL('triggered()'), self.save)
        QtCore.QObject.connect(self.actionSave_As, QtCore.SIGNAL('triggered()'), self.saveas)
        self.t = None

    def saveas(self):
        s = save_mod.Save()
        s.show()
        s.exec_()
        self.t = s.get()
        self.save()

    def save(self):
        if self.t is not None:
            with open(str(self.t), "w") as f:
                f.write(str(self.te.toPlainText()))
            try:
                pass
            except Exception as e:
                QtGui.QMessageBox.warning(self, "Warning!", str(e))
        else:
            s = save_mod.Save()
            s.show()
            s.exec_()
            self.t = s.get()
            print(self.t)
            if self.t is None:
                return False
            self.save()

    def open(self):
        op = o.Open()
        op.show()
        op.exec_()
        self.t = op.get()
        try:
            if self.t == "":
                return False
            with open(str(self.t), "r") as f:
                self.te.setText(str(f.read()))
        except Exception as e:
            QtGui.QMessageBox.warning(self, "Warning!", str(e))

app = QtGui.QApplication(sys.argv)
myWindow = Main(None)
myWindow.show()
app.exec_() 
