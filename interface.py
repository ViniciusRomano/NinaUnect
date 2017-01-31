# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from CrudNina import CrudNina
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

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(417, 203)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.radioButton = QtGui.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(270, 80, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(270, 110, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(200, 20, 20, 121))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 113, 25))
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setValidator(QIntValidator())
        self.lineEdit.setMaxLength(7)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setLineWidth(3)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 150, 85, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.insert)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        try:
            self.obj = CrudNina()
        except:
            QMessageBox.warning(self.Dialog, "Error", "Erro na conexão. Certifique que o computador está conectado com a internet.")

    def insert(self):

        state = "null"

        ra = self.lineEdit.text()

        if self.radioButton.isChecked():
            state = "Start"

        if self.radioButton_2.isChecked():
            state = "End"

        #connect with firebase
        if(state == "null"):
            QMessageBox.warning(self.Dialog, "Error", "Selecione uma das opções de estado da Permanência!")
        elif((ra.isdigit() == False) or (len(ra) != 7)):
            QMessageBox.warning(self.Dialog, "Error", "RA inválido!")
        else:
            try:
                self.obj.push(ra,state)
                QMessageBox.information(self.Dialog, "Success", "Envio realizado com sucesso")
            except:
                QMessageBox.warning(self.Dialog, "Error", "Erro no envio de dados. Certifique que o computador está conectado com a internet.")

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Nina - Unect", None))
        self.radioButton.setText(_translate("Dialog", "Inicio", None))
        self.radioButton_2.setText(_translate("Dialog", "Termino", None))
        self.label.setText(_translate("Dialog", "Utilize o leitor de codigo de\n"
" barras ou insira seu RA manualmente", None))
        self.label_2.setText(_translate("Dialog", "Estado da Permanencia", None))
        self.pushButton.setText(_translate("Dialog", "Ok", None))
