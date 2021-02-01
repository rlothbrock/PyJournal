# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sales_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_sales_form(object):
    def setupUi(self, Dialog_sales_form):
        if not Dialog_sales_form.objectName():
            Dialog_sales_form.setObjectName(u"Dialog_sales_form")
        Dialog_sales_form.setWindowModality(Qt.ApplicationModal)
        Dialog_sales_form.resize(531, 316)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_sales_form.setWindowIcon(icon)
        Dialog_sales_form.setModal(False)
        self.buttonBox = QDialogButtonBox(Dialog_sales_form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 280, 511, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Close|QDialogButtonBox.Reset)
        self.verticalLayoutWidget_5 = QWidget(Dialog_sales_form)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 511, 261))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_sales = QFormLayout()
        self.formLayout_sales.setObjectName(u"formLayout_sales")
        self.nombreDelProductoLabel = QLabel(self.verticalLayoutWidget_5)
        self.nombreDelProductoLabel.setObjectName(u"nombreDelProductoLabel")

        self.formLayout_sales.setWidget(0, QFormLayout.LabelRole, self.nombreDelProductoLabel)

        self.nombreDelProductoComboBox = QComboBox(self.verticalLayoutWidget_5)
        self.nombreDelProductoComboBox.setObjectName(u"nombreDelProductoComboBox")
        self.nombreDelProductoComboBox.setDuplicatesEnabled(True)

        self.formLayout_sales.setWidget(0, QFormLayout.FieldRole, self.nombreDelProductoComboBox)

        self.codigoDelProductoLabel = QLabel(self.verticalLayoutWidget_5)
        self.codigoDelProductoLabel.setObjectName(u"codigoDelProductoLabel")

        self.formLayout_sales.setWidget(1, QFormLayout.LabelRole, self.codigoDelProductoLabel)

        self.codigoDelProductoComboBox = QComboBox(self.verticalLayoutWidget_5)
        self.codigoDelProductoComboBox.setObjectName(u"codigoDelProductoComboBox")
        self.codigoDelProductoComboBox.setDuplicatesEnabled(True)

        self.formLayout_sales.setWidget(1, QFormLayout.FieldRole, self.codigoDelProductoComboBox)

        self.cantidadVendidaLabel = QLabel(self.verticalLayoutWidget_5)
        self.cantidadVendidaLabel.setObjectName(u"cantidadVendidaLabel")

        self.formLayout_sales.setWidget(2, QFormLayout.LabelRole, self.cantidadVendidaLabel)

        self.precioDeVentaLabel = QLabel(self.verticalLayoutWidget_5)
        self.precioDeVentaLabel.setObjectName(u"precioDeVentaLabel")

        self.formLayout_sales.setWidget(3, QFormLayout.LabelRole, self.precioDeVentaLabel)

        self.precioDeVentaDoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget_5)
        self.precioDeVentaDoubleSpinBox.setObjectName(u"precioDeVentaDoubleSpinBox")
        self.precioDeVentaDoubleSpinBox.setToolTipDuration(3)
        self.precioDeVentaDoubleSpinBox.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.precioDeVentaDoubleSpinBox.setProperty("showGroupSeparator", True)
        self.precioDeVentaDoubleSpinBox.setMaximum(1000000.000000000000000)

        self.formLayout_sales.setWidget(3, QFormLayout.FieldRole, self.precioDeVentaDoubleSpinBox)

        self.comentariosLabel = QLabel(self.verticalLayoutWidget_5)
        self.comentariosLabel.setObjectName(u"comentariosLabel")

        self.formLayout_sales.setWidget(4, QFormLayout.LabelRole, self.comentariosLabel)

        self.comentariosLineEdit = QLineEdit(self.verticalLayoutWidget_5)
        self.comentariosLineEdit.setObjectName(u"comentariosLineEdit")
        self.comentariosLineEdit.setClearButtonEnabled(False)

        self.formLayout_sales.setWidget(4, QFormLayout.FieldRole, self.comentariosLineEdit)

        self.cantidadVendidaComboBox = QComboBox(self.verticalLayoutWidget_5)
        self.cantidadVendidaComboBox.setObjectName(u"cantidadVendidaComboBox")

        self.formLayout_sales.setWidget(2, QFormLayout.FieldRole, self.cantidadVendidaComboBox)


        self.verticalLayout_5.addLayout(self.formLayout_sales)

        self.label_5 = QLabel(self.verticalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_5)


        self.retranslateUi(Dialog_sales_form)
        self.buttonBox.accepted.connect(Dialog_sales_form.accept)
        self.buttonBox.rejected.connect(Dialog_sales_form.reject)

        QMetaObject.connectSlotsByName(Dialog_sales_form)
    # setupUi

    def retranslateUi(self, Dialog_sales_form):
        Dialog_sales_form.setWindowTitle(QCoreApplication.translate("Dialog_sales_form", u"Formulario de Ventas", None))
        self.nombreDelProductoLabel.setText(QCoreApplication.translate("Dialog_sales_form", u"Nombre del Producto", None))
        self.codigoDelProductoLabel.setText(QCoreApplication.translate("Dialog_sales_form", u"Codigo del Producto", None))
        self.cantidadVendidaLabel.setText(QCoreApplication.translate("Dialog_sales_form", u"Cantidad Vendida", None))
        self.precioDeVentaLabel.setText(QCoreApplication.translate("Dialog_sales_form", u"Precio de Venta", None))
#if QT_CONFIG(tooltip)
        self.precioDeVentaDoubleSpinBox.setToolTip(QCoreApplication.translate("Dialog_sales_form", u"<html><head/><body><p>Escriba aqui el <span style=\" font-weight:600;\">precio de venta total</span> recibido por la cantidad de articulos de la entrada</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.precioDeVentaDoubleSpinBox.setPrefix(QCoreApplication.translate("Dialog_sales_form", u"$", None))
        self.comentariosLabel.setText(QCoreApplication.translate("Dialog_sales_form", u"Comentarios", None))
        self.comentariosLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog_sales_form", u"Insertar comentarios...", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_sales_form", u"Utilice este formulario para insertar las ventas de la sesion (d\u00eda) en el que se trabaja. NO UTILIZAR para insertar las compras", None))
    # retranslateUi

