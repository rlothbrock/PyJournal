# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'old_session_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(364, 168)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(80, 130, 261, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 331, 31))
        font = QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.dateEditSession = QDateEdit(Dialog)
        self.dateEditSession.setObjectName(u"dateEditSession")
        self.dateEditSession.setGeometry(QRect(60, 80, 281, 26))
        self.dateEditSession.setMinimumDate(QDate(2020, 1, 1))
        self.dateEditSession.setCalendarPopup(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Cambiar la Fecha de Trabajo", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Inserte la fecha en la que desea trabajar", None))
        self.dateEditSession.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd/MM/yyyy", None))
    # retranslateUi

