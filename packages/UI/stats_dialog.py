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
        self.filter_dialog_stats_table = QPushButton(self.horizontalLayoutWidget)
        self.filter_dialog_stats_table.setObjectName(u"filter_dialog_stats_table")

        self.horizontalLayout.addWidget(self.filter_dialog_stats_table)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.export_dialog_stats_table = QPushButton(self.horizontalLayoutWidget)
        self.export_dialog_stats_table.setObjectName(u"export_dialog_stats_table")

        self.horizontalLayout.addWidget(self.export_dialog_stats_table)

        self.Print_dialog_stats_table = QPushButton(self.horizontalLayoutWidget)
        self.Print_dialog_stats_table.setObjectName(u"Print_dialog_stats_table")

        self.horizontalLayout.addWidget(self.Print_dialog_stats_table)

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
        self.filter_dialog_stats_table.setText(QCoreApplication.translate("Dialog", u"&Filter...", None))
        self.export_dialog_stats_table.setText(QCoreApplication.translate("Dialog", u"&Export", None))
        self.Print_dialog_stats_table.setText(QCoreApplication.translate("Dialog", u"&Print", None))
    # retranslateUi

