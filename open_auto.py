# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Dialog.resize(447, 312)
        self.lw = QtGui.QListWidget(Dialog)
        self.lw.setGeometry(QtCore.QRect(0, 0, 391, 261))
        self.lw.setObjectName(_fromUtf8("lw"))
        self.dot = QtGui.QToolButton(Dialog)
        self.dot.setGeometry(QtCore.QRect(410, 10, 32, 27))
        self.dot.setObjectName(_fromUtf8("dot"))
        self.pb_ok = QtGui.QPushButton(Dialog)
        self.pb_ok.setGeometry(QtCore.QRect(190, 270, 112, 34))
        self.pb_ok.setObjectName(_fromUtf8("pb_ok"))
        self.pb_cancel = QtGui.QPushButton(Dialog)
        self.pb_cancel.setGeometry(QtCore.QRect(310, 270, 112, 34))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pb_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Open", None))
        self.dot.setText(_translate("Dialog", "...", None))
        self.pb_ok.setText(_translate("Dialog", "OK", None))
        self.pb_cancel.setText(_translate("Dialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

