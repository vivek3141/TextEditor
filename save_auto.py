# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save.ui'
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
        Dialog.resize(505, 427)
        self.pb_cancel = QtGui.QPushButton(Dialog)
        self.pb_cancel.setGeometry(QtCore.QRect(330, 370, 112, 34))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.lw = QtGui.QListWidget(Dialog)
        self.lw.setGeometry(QtCore.QRect(30, 20, 411, 301))
        self.lw.setObjectName(_fromUtf8("lw"))
        self.dot = QtGui.QToolButton(Dialog)
        self.dot.setGeometry(QtCore.QRect(460, 20, 32, 27))
        self.dot.setObjectName(_fromUtf8("dot"))
        self.le = QtGui.QLineEdit(Dialog)
        self.le.setGeometry(QtCore.QRect(31, 334, 281, 27))
        self.le.setObjectName(_fromUtf8("le"))
        self.pb_save = QtGui.QPushButton(Dialog)
        self.pb_save.setGeometry(QtCore.QRect(328, 331, 112, 34))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pb_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Save As", None))
        self.pb_cancel.setText(_translate("Dialog", "Cancel", None))
        self.dot.setText(_translate("Dialog", "...", None))
        self.pb_save.setText(_translate("Dialog", "OK", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

