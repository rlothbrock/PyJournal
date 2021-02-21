# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progressBar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_progressBar(object):
    def setupUi(self, Dialog_progressBar):
        if not Dialog_progressBar.objectName():
            Dialog_progressBar.setObjectName(u"Dialog_progressBar")
        Dialog_progressBar.resize(400, 95)
        self.progressBar = QProgressBar(Dialog_progressBar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 20, 381, 23))
        self.progressBar.setValue(80)
        self.progressBar.setInvertedAppearance(False)
        self.horizontalLayoutWidget = QWidget(Dialog_progressBar)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 50, 381, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_cantidad_completada = QLabel(self.horizontalLayoutWidget)
        self.label_cantidad_completada.setObjectName(u"label_cantidad_completada")

        self.horizontalLayout.addWidget(self.label_cantidad_completada)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_cantidad_total = QLabel(self.horizontalLayoutWidget)
        self.label_cantidad_total.setObjectName(u"label_cantidad_total")

        self.horizontalLayout.addWidget(self.label_cantidad_total)


        self.retranslateUi(Dialog_progressBar)

        QMetaObject.connectSlotsByName(Dialog_progressBar)
    # setupUi

    def retranslateUi(self, Dialog_progressBar):
        Dialog_progressBar.setWindowTitle(QCoreApplication.translate("Dialog_progressBar", u"Realizando Operacion", None))
        self.label.setText(QCoreApplication.translate("Dialog_progressBar", u"Completado: ", None))
        self.label_cantidad_completada.setText(QCoreApplication.translate("Dialog_progressBar", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_progressBar", u"De", None))
        self.label_cantidad_total.setText(QCoreApplication.translate("Dialog_progressBar", u"100", None))
    # retranslateUi

