import sys
from open_auto import *
import os
 

class Open(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent)
        self.text = ""
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        self.load()
        QtCore.QObject.connect(self.ui.pb_ok, QtCore.SIGNAL('clicked()'), self.ok)
        QtCore.QObject.connect(self.ui.dot, QtCore.SIGNAL('clicked()'), self.dot)

    def dot(self):
        os.chdir("..")
        self.load()

    def load(self):
        self.ui.lw.clear()
        for x in os.listdir(os.getcwd()):
            self.ui.lw.addItem(x)

    def ok(self):
        t = self.ui.lw.currentItem().text()
        try:
            os.chdir(str(t))
            self.load()
            return False
        except Exception as e:
            pass

        self.text = t if t is not '' else None
        self.close()

    def get(self):
        return self.text

if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=Open()
    myapp.show()
    sys.exit(app.exec_()) 
