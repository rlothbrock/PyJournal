# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rent_salary_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RentOrSalaryDialog(object):
    def setupUi(self, RentOrSalaryDialog):
        if not RentOrSalaryDialog.objectName():
            RentOrSalaryDialog.setObjectName(u"RentOrSalaryDialog")
        RentOrSalaryDialog.resize(667, 204)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        RentOrSalaryDialog.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(RentOrSalaryDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(320, 170, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.frame = QFrame(RentOrSalaryDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 661, 151))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(7, 10, 651, 131))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.doubleSpinBox_changeSalary = QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_changeSalary.setObjectName(u"doubleSpinBox_changeSalary")

        self.gridLayout.addWidget(self.doubleSpinBox_changeSalary, 2, 1, 1, 1)

        self.doubleSpinBox_changeRent = QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_changeRent.setObjectName(u"doubleSpinBox_changeRent")

        self.gridLayout.addWidget(self.doubleSpinBox_changeRent, 1, 1, 1, 1)

        self.pushButtonChangeRent = QPushButton(self.gridLayoutWidget)
        self.pushButtonChangeRent.setObjectName(u"pushButtonChangeRent")

        self.gridLayout.addWidget(self.pushButtonChangeRent, 1, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButtonChangeSalary = QPushButton(self.gridLayoutWidget)
        self.pushButtonChangeSalary.setObjectName(u"pushButtonChangeSalary")

        self.gridLayout.addWidget(self.pushButtonChangeSalary, 2, 2, 1, 1)

        self.checkBox_changeSalary = QCheckBox(self.gridLayoutWidget)
        self.checkBox_changeSalary.setObjectName(u"checkBox_changeSalary")

        self.gridLayout.addWidget(self.checkBox_changeSalary, 2, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.checkBox_changeRent = QCheckBox(self.gridLayoutWidget)
        self.checkBox_changeRent.setObjectName(u"checkBox_changeRent")

        self.gridLayout.addWidget(self.checkBox_changeRent, 1, 0, 1, 1)

        self.radioButton_rate_over_proffit = QRadioButton(self.gridLayoutWidget)
        self.radioButton_rate_over_proffit.setObjectName(u"radioButton_rate_over_proffit")

        self.gridLayout.addWidget(self.radioButton_rate_over_proffit, 3, 1, 1, 1)

        self.radioButton_rate_over_sales = QRadioButton(self.gridLayoutWidget)
        self.radioButton_rate_over_sales.setObjectName(u"radioButton_rate_over_sales")

        self.gridLayout.addWidget(self.radioButton_rate_over_sales, 3, 2, 1, 1)

        self.radioButton_fixed_rate = QRadioButton(self.gridLayoutWidget)
        self.radioButton_fixed_rate.setObjectName(u"radioButton_fixed_rate")

        self.gridLayout.addWidget(self.radioButton_fixed_rate, 3, 0, 1, 1)


        self.retranslateUi(RentOrSalaryDialog)
        self.buttonBox.accepted.connect(RentOrSalaryDialog.accept)
        self.buttonBox.rejected.connect(RentOrSalaryDialog.reject)

        QMetaObject.connectSlotsByName(RentOrSalaryDialog)
    # setupUi

    def retranslateUi(self, RentOrSalaryDialog):
        RentOrSalaryDialog.setWindowTitle(QCoreApplication.translate("RentOrSalaryDialog", u"Modificar Salario o Renta", None))
        self.pushButtonChangeRent.setText(QCoreApplication.translate("RentOrSalaryDialog", u"Cambiar &Renta", None))
        self.label.setText(QCoreApplication.translate("RentOrSalaryDialog", u"Modificar:", None))
        self.pushButtonChangeSalary.setText(QCoreApplication.translate("RentOrSalaryDialog", u"Cambiar &Salario", None))
        self.checkBox_changeSalary.setText(QCoreApplication.translate("RentOrSalaryDialog", u"Tasa de Salario", None))
        self.label_2.setText(QCoreApplication.translate("RentOrSalaryDialog", u"Valor a insertar", None))
        self.checkBox_changeRent.setText(QCoreApplication.translate("RentOrSalaryDialog", u"Valor de la Renta Diaria", None))
        self.radioButton_rate_over_proffit.setText(QCoreApplication.translate("RentOrSalaryDialog", u"% sobre &Ganancias", None))
        self.radioButton_rate_over_sales.setText(QCoreApplication.translate("RentOrSalaryDialog", u"% sobre la &Venta", None))
        self.radioButton_fixed_rate.setText(QCoreApplication.translate("RentOrSalaryDialog", u"Usar Valor &Fijo", None))
    # retranslateUi

