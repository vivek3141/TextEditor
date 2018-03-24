import sys
from save_auto import *
import os
 

class Save(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self) 
        QtCore.QObject.connect(self.ui.pb_save, QtCore.SIGNAL('clicked()'), self.save)
        QtCore.QObject.connect(self.ui.dot, QtCore.SIGNAL('clicked()'), self.dot)
        self.t = None
        self.load()

    def save(self):
        try:
            t = self.ui.lw.currentItem().text()
            os.chdir(str(t))
            self.load()
            return False
        except Exception as e:
            pass
        self.t = self.ui.le.text()
        self.close()

    def load(self):
        self.ui.lw.clear()
        for x in os.listdir(os.getcwd()):
            self.ui.lw.addItem(x)

    def get(self):
        return self.t

    def dot(self):
        os.chdir("..")
        self.load()

         
if __name__=="__main__": 
    app = QtGui.QApplication(sys.argv)
    myapp = Save()
    myapp.show()
    sys.exit(app.exec_()) 
