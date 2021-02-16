# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exc_rate_dialog.ui'
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
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(400, 165)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 110, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Discard)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 311, 21))
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(12, 30, 381, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.doubleSpinBox = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMaximum(1000.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout.addWidget(self.label_4)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Fijar Tasa de Cambio", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Insertar la tasa de Cambio:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"1 USD ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"es igual a ", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"CUP", None))
    # retranslateUi

