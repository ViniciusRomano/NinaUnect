# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from CrudNina import CrudNina
import sys
import interface

class ExampleApp(QtGui.QMainWindow, interface.Ui_Dialog):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = interface.Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
