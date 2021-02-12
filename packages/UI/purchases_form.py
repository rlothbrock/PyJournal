# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchases_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_purchases_form(object):
    def setupUi(self, Dialog_purchases_form):
        if not Dialog_purchases_form.objectName():
            Dialog_purchases_form.setObjectName(u"Dialog_purchases_form")
        Dialog_purchases_form.setWindowModality(Qt.ApplicationModal)
        Dialog_purchases_form.resize(590, 502)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_purchases_form.setWindowIcon(icon)
        Dialog_purchases_form.setSizeGripEnabled(False)
        Dialog_purchases_form.setModal(False)
        self.buttonBox = QDialogButtonBox(Dialog_purchases_form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 460, 561, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Close|QDialogButtonBox.Reset)
        self.verticalLayoutWidget_5 = QWidget(Dialog_purchases_form)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 561, 401))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget_5)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_importar_ventas = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_importar_ventas.setObjectName(u"pushButton_importar_ventas")

        self.horizontalLayout.addWidget(self.pushButton_importar_ventas)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.itemAConsignacionLabel = QLabel(self.verticalLayoutWidget_5)
        self.itemAConsignacionLabel.setObjectName(u"itemAConsignacionLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.itemAConsignacionLabel)

        self.itemAConsignacionCheckBox = QCheckBox(self.verticalLayoutWidget_5)
        self.itemAConsignacionCheckBox.setObjectName(u"itemAConsignacionCheckBox")
        self.itemAConsignacionCheckBox.setToolTipDuration(-1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.itemAConsignacionCheckBox)

        self.nuevoItemMarcarCuandoEsUnNuevoProductoLabel = QLabel(self.verticalLayoutWidget_5)
        self.nuevoItemMarcarCuandoEsUnNuevoProductoLabel.setObjectName(u"nuevoItemMarcarCuandoEsUnNuevoProductoLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.nuevoItemMarcarCuandoEsUnNuevoProductoLabel)

        self.nuevoItemPurchaseCheckBox = QCheckBox(self.verticalLayoutWidget_5)
        self.nuevoItemPurchaseCheckBox.setObjectName(u"nuevoItemPurchaseCheckBox")
        self.nuevoItemPurchaseCheckBox.setToolTipDuration(-1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nuevoItemPurchaseCheckBox)

        self.nombreDelItemCompradoLabel = QLabel(self.verticalLayoutWidget_5)
        self.nombreDelItemCompradoLabel.setObjectName(u"nombreDelItemCompradoLabel")
        self.nombreDelItemCompradoLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.nombreDelItemCompradoLabel)

        self.nombreDelItemCompradoLineEdit = QLineEdit(self.verticalLayoutWidget_5)
        self.nombreDelItemCompradoLineEdit.setObjectName(u"nombreDelItemCompradoLineEdit")
        self.nombreDelItemCompradoLineEdit.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.nombreDelItemCompradoLineEdit)

        self.nombreDelItemIncrementadoLabel = QLabel(self.verticalLayoutWidget_5)
        self.nombreDelItemIncrementadoLabel.setObjectName(u"nombreDelItemIncrementadoLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.nombreDelItemIncrementadoLabel)

        self.nombreDelItemIncrementadoComboBox = QComboBox(self.verticalLayoutWidget_5)
        self.nombreDelItemIncrementadoComboBox.setObjectName(u"nombreDelItemIncrementadoComboBox")
        self.nombreDelItemIncrementadoComboBox.setDuplicatesEnabled(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.nombreDelItemIncrementadoComboBox)

        self.codigoDelItemIncrementadoLabel = QLabel(self.verticalLayoutWidget_5)
        self.codigoDelItemIncrementadoLabel.setObjectName(u"codigoDelItemIncrementadoLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.codigoDelItemIncrementadoLabel)

        self.codigoDelItemIncrementadoComboBox = QComboBox(self.verticalLayoutWidget_5)
        self.codigoDelItemIncrementadoComboBox.setObjectName(u"codigoDelItemIncrementadoComboBox")
        self.codigoDelItemIncrementadoComboBox.setDuplicatesEnabled(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.codigoDelItemIncrementadoComboBox)


        self.verticalLayout_5.addLayout(self.formLayout)

        self.label_2 = QLabel(self.verticalLayoutWidget_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_2)

        self.formLayout_purchases = QFormLayout()
        self.formLayout_purchases.setObjectName(u"formLayout_purchases")
        self.totalDeItemsCompradosLabel = QLabel(self.verticalLayoutWidget_5)
        self.totalDeItemsCompradosLabel.setObjectName(u"totalDeItemsCompradosLabel")

        self.formLayout_purchases.setWidget(0, QFormLayout.LabelRole, self.totalDeItemsCompradosLabel)

        self.totalDeItemsCompradosSpinBox = QSpinBox(self.verticalLayoutWidget_5)
        self.totalDeItemsCompradosSpinBox.setObjectName(u"totalDeItemsCompradosSpinBox")
        self.totalDeItemsCompradosSpinBox.setProperty("showGroupSeparator", True)
        self.totalDeItemsCompradosSpinBox.setMinimum(1)
        self.totalDeItemsCompradosSpinBox.setMaximum(10000)

        self.formLayout_purchases.setWidget(0, QFormLayout.FieldRole, self.totalDeItemsCompradosSpinBox)

        self.precioTotalPagadoPorLaCompraLabel = QLabel(self.verticalLayoutWidget_5)
        self.precioTotalPagadoPorLaCompraLabel.setObjectName(u"precioTotalPagadoPorLaCompraLabel")
        self.precioTotalPagadoPorLaCompraLabel.setEnabled(False)

        self.formLayout_purchases.setWidget(1, QFormLayout.LabelRole, self.precioTotalPagadoPorLaCompraLabel)

        self.precioTotalPagadoPorLaCompraDoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget_5)
        self.precioTotalPagadoPorLaCompraDoubleSpinBox.setObjectName(u"precioTotalPagadoPorLaCompraDoubleSpinBox")
        self.precioTotalPagadoPorLaCompraDoubleSpinBox.setEnabled(False)
        self.precioTotalPagadoPorLaCompraDoubleSpinBox.setToolTipDuration(-1)
        self.precioTotalPagadoPorLaCompraDoubleSpinBox.setProperty("showGroupSeparator", True)
        self.precioTotalPagadoPorLaCompraDoubleSpinBox.setMaximum(1000000.000000000000000)

        self.formLayout_purchases.setWidget(1, QFormLayout.FieldRole, self.precioTotalPagadoPorLaCompraDoubleSpinBox)

        self.comentariosDeEntradaLabel = QLabel(self.verticalLayoutWidget_5)
        self.comentariosDeEntradaLabel.setObjectName(u"comentariosDeEntradaLabel")

        self.formLayout_purchases.setWidget(2, QFormLayout.LabelRole, self.comentariosDeEntradaLabel)

        self.comentariosDeEntradaLineEdit = QLineEdit(self.verticalLayoutWidget_5)
        self.comentariosDeEntradaLineEdit.setObjectName(u"comentariosDeEntradaLineEdit")

        self.formLayout_purchases.setWidget(2, QFormLayout.FieldRole, self.comentariosDeEntradaLineEdit)


        self.verticalLayout_5.addLayout(self.formLayout_purchases)

        self.label_5 = QLabel(Dialog_purchases_form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QRect(10, 420, 559, 42))
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.retranslateUi(Dialog_purchases_form)
        self.buttonBox.accepted.connect(Dialog_purchases_form.accept)
        self.buttonBox.rejected.connect(Dialog_purchases_form.reject)

        QMetaObject.connectSlotsByName(Dialog_purchases_form)
    # setupUi

    def retranslateUi(self, Dialog_purchases_form):
        Dialog_purchases_form.setWindowTitle(QCoreApplication.translate("Dialog_purchases_form", u"Formulario de Compras", None))
        self.label.setText(QCoreApplication.translate("Dialog_purchases_form", u"Datos del producto (Lea cuidadosamente)", None))
        self.pushButton_importar_ventas.setText(QCoreApplication.translate("Dialog_purchases_form", u"Importar...", None))
        self.itemAConsignacionLabel.setText(QCoreApplication.translate("Dialog_purchases_form", u"Producto a Consignacion", None))
#if QT_CONFIG(tooltip)
        self.itemAConsignacionCheckBox.setToolTip(QCoreApplication.translate("Dialog_purchases_form", u"<html><head/><body><p>Marcar solamente si el producto que se va a entrar <span style=\" font-weight:600;\">NO </span>se pago con el dinero del negocio</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nuevoItemMarcarCuandoEsUnNuevoProductoLabel.setText(QCoreApplication.translate("Dialog_purchases_form", u"Producto Nuevo", None))
#if QT_CONFIG(tooltip)
        self.nuevoItemPurchaseCheckBox.setToolTip(QCoreApplication.translate("Dialog_purchases_form", u"<html><head/><body><p>Marcar solamente si el producto <span style=\" font-weight:600;\">no existe</span> en el inventario o existe con un <span style=\" font-weight:600;\">precio de compra diferente</span><span style=\" font-weight:600; font-style:italic;\"/>al de la entrada actual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nombreDelItemCompradoLabel.setText(QCoreApplication.translate("Dialog_purchases_form", u"Nombre del Nuevo Producto", None))
        self.nombreDelItemIncrementadoLabel.setText(QCoreApplication.translate("Dialog_purchases_form", u"Nombre del Producto", None))
        self.codigoDelItemIncrementadoLabel.setText(QCoreApplication.translate("Dialog_purchases_form", u"Codigo del Producto", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_purchases_form", u"Nota: Un producto se debe marcar como NUEVO si NO EXISTE en el inventario o existe con un PRECIO DIFERENTE al de la compra que se trabaja.", None))
        self.totalDeItemsCompradosLabel.setText(QCoreApplication.translate("Dialog_purchases_form", u"Total de Items Comprados", None))
        self.precioTotalPagadoPorLaCompraLabel.setText(QCoreApplication.translate("Dialog_purchases_form", u"Precio Total pagado por la Compra", None))
#if QT_CONFIG(tooltip)
        self.precioTotalPagadoPorLaCompraDoubleSpinBox.setToolTip(QCoreApplication.translate("Dialog_purchases_form", u"<html><head/><body><p>Escriba aqui el valor total que se paga por la compra de la cantidad indicada en la entrada actual <span style=\" font-weight:600;\">NO ponga el valor de un item solo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.precioTotalPagadoPorLaCompraDoubleSpinBox.setPrefix(QCoreApplication.translate("Dialog_purchases_form", u"$ ", None))
        self.comentariosDeEntradaLabel.setText(QCoreApplication.translate("Dialog_purchases_form", u"Comentarios de Entrada", None))
        self.comentariosDeEntradaLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog_purchases_form", u"Insertar comentarios ...", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_purchases_form", u"Utilice este formulario para insertar SOLAMENTE las COMPRAS", None))
    # retranslateUi

