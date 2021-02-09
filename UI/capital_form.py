# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'capital_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogCapital(object):
    def setupUi(self, DialogCapital):
        if not DialogCapital.objectName():
            DialogCapital.setObjectName(u"DialogCapital")
        DialogCapital.setWindowModality(Qt.ApplicationModal)
        DialogCapital.resize(543, 313)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogCapital.setWindowIcon(icon)
        DialogCapital.setModal(False)
        self.buttonBox = QDialogButtonBox(DialogCapital)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 270, 511, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Close|QDialogButtonBox.Reset)
        self.formLayoutWidget_2 = QWidget(DialogCapital)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(8, 12, 511, 168))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.nombreDelQueInsertaElDineroLabel = QLabel(self.formLayoutWidget_2)
        self.nombreDelQueInsertaElDineroLabel.setObjectName(u"nombreDelQueInsertaElDineroLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.nombreDelQueInsertaElDineroLabel)

        self.nombreDelQueInsertaElDineroComboBox = QComboBox(self.formLayoutWidget_2)
        self.nombreDelQueInsertaElDineroComboBox.addItem("")
        self.nombreDelQueInsertaElDineroComboBox.addItem("")
        self.nombreDelQueInsertaElDineroComboBox.setObjectName(u"nombreDelQueInsertaElDineroComboBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.nombreDelQueInsertaElDineroComboBox)

        self.cantidadDeDineroLabel = QLabel(self.formLayoutWidget_2)
        self.cantidadDeDineroLabel.setObjectName(u"cantidadDeDineroLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.cantidadDeDineroLabel)

        self.cantidadDeDineroDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.cantidadDeDineroDoubleSpinBox.setObjectName(u"cantidadDeDineroDoubleSpinBox")
        self.cantidadDeDineroDoubleSpinBox.setProperty("showGroupSeparator", True)
        self.cantidadDeDineroDoubleSpinBox.setMaximum(1000000.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.cantidadDeDineroDoubleSpinBox)

        self.extraccionDelMontoLabel = QLabel(self.formLayoutWidget_2)
        self.extraccionDelMontoLabel.setObjectName(u"extraccionDelMontoLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.extraccionDelMontoLabel)

        self.extraccionDelMontoCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.extraccionDelMontoCheckBox.setObjectName(u"extraccionDelMontoCheckBox")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.extraccionDelMontoCheckBox)

        self.comentariosDeCapitalLabel = QLabel(self.formLayoutWidget_2)
        self.comentariosDeCapitalLabel.setObjectName(u"comentariosDeCapitalLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.comentariosDeCapitalLabel)

        self.comentariosDeCapitalLineEdit = QLineEdit(self.formLayoutWidget_2)
        self.comentariosDeCapitalLineEdit.setObjectName(u"comentariosDeCapitalLineEdit")
        self.comentariosDeCapitalLineEdit.setInputMethodHints(Qt.ImhMultiLine)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comentariosDeCapitalLineEdit)

        self.validacionDeLaEntradaLabel = QLabel(self.formLayoutWidget_2)
        self.validacionDeLaEntradaLabel.setObjectName(u"validacionDeLaEntradaLabel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.validacionDeLaEntradaLabel)

        self.validacionDeLaEntradaLineEdit = QLineEdit(self.formLayoutWidget_2)
        self.validacionDeLaEntradaLineEdit.setObjectName(u"validacionDeLaEntradaLineEdit")
        self.validacionDeLaEntradaLineEdit.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.validacionDeLaEntradaLineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.validacionDeLaEntradaLineEdit)

        self.notasDeCapital = QLabel(DialogCapital)
        self.notasDeCapital.setObjectName(u"notasDeCapital")
        self.notasDeCapital.setGeometry(QRect(10, 190, 511, 71))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.notasDeCapital.setFont(font)
        self.notasDeCapital.setWordWrap(True)

        self.retranslateUi(DialogCapital)
        self.buttonBox.accepted.connect(DialogCapital.accept)
        self.buttonBox.rejected.connect(DialogCapital.reject)

        QMetaObject.connectSlotsByName(DialogCapital)
    # setupUi

    def retranslateUi(self, DialogCapital):
        DialogCapital.setWindowTitle(QCoreApplication.translate("DialogCapital", u"Insertar Capital", None))
        self.nombreDelQueInsertaElDineroLabel.setText(QCoreApplication.translate("DialogCapital", u"Nombre del que Inserta el dinero", None))
        self.nombreDelQueInsertaElDineroComboBox.setItemText(0, QCoreApplication.translate("DialogCapital", u"Robert", None))
        self.nombreDelQueInsertaElDineroComboBox.setItemText(1, QCoreApplication.translate("DialogCapital", u"Ariadna", None))

        self.cantidadDeDineroLabel.setText(QCoreApplication.translate("DialogCapital", u"Cantidad de Dinero ", None))
        self.cantidadDeDineroDoubleSpinBox.setPrefix(QCoreApplication.translate("DialogCapital", u"$ ", None))
        self.extraccionDelMontoLabel.setText(QCoreApplication.translate("DialogCapital", u"Extraer dinero (Rebaja la inversion)", None))
        self.comentariosDeCapitalLabel.setText(QCoreApplication.translate("DialogCapital", u"Comentarios de Capital", None))
        self.comentariosDeCapitalLineEdit.setPlaceholderText(QCoreApplication.translate("DialogCapital", u"Insertar  comentarios si es necesario ...", None))
        self.validacionDeLaEntradaLabel.setText(QCoreApplication.translate("DialogCapital", u"Validacion de la entrada", None))
        self.notasDeCapital.setText(QCoreApplication.translate("DialogCapital", u"Esta accion va a {}: {} pesos del aporte de {} de la inversion. Prestar atenci\u00f3n antes de realizar cualquier entrada en esta seccion ", None))
    # retranslateUi

