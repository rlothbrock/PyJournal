# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stats_dialog.ui'
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
        Dialog.resize(1200, 600)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 1171, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonfilter_dialog_stats_table = QPushButton(self.horizontalLayoutWidget)
        self.pushButtonfilter_dialog_stats_table.setObjectName(u"pushButtonfilter_dialog_stats_table")

        self.horizontalLayout.addWidget(self.pushButtonfilter_dialog_stats_table)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonexport_dialog_stats_table = QPushButton(self.horizontalLayoutWidget)
        self.pushButtonexport_dialog_stats_table.setObjectName(u"pushButtonexport_dialog_stats_table")

        self.horizontalLayout.addWidget(self.pushButtonexport_dialog_stats_table)

        self.pushButtonprint_dialog_stats_table = QPushButton(self.horizontalLayoutWidget)
        self.pushButtonprint_dialog_stats_table.setObjectName(u"pushButtonprint_dialog_stats_table")

        self.horizontalLayout.addWidget(self.pushButtonprint_dialog_stats_table)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 50, 1171, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.tableWidget_dialog_stats = QTableWidget(Dialog)
        self.tableWidget_dialog_stats.setObjectName(u"tableWidget_dialog_stats")
        self.tableWidget_dialog_stats.setGeometry(QRect(15, 71, 1171, 521))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButtonfilter_dialog_stats_table.setText(QCoreApplication.translate("Dialog", u"&Filter...", None))
        self.pushButtonexport_dialog_stats_table.setText(QCoreApplication.translate("Dialog", u"&Export", None))
        self.pushButtonprint_dialog_stats_table.setText(QCoreApplication.translate("Dialog", u"&Print", None))
    # retranslateUi

