# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filters_form.ui'
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
        Dialog.resize(772, 484)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 430, 711, 41))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Discard|QDialogButtonBox.Help|QDialogButtonBox.Reset)
        self.toolButton_filter_options = QToolButton(Dialog)
        self.toolButton_filter_options.setObjectName(u"toolButton_filter_options")
        self.toolButton_filter_options.setGeometry(QRect(10, 430, 31, 31))
        self.listWidget_field_manager = QListWidget(Dialog)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_field_manager)
        __qlistwidgetitem.setCheckState(Qt.Checked);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_field_manager)
        __qlistwidgetitem1.setCheckState(Qt.Checked);
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_field_manager)
        __qlistwidgetitem2.setCheckState(Qt.Checked);
        __qlistwidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_field_manager)
        __qlistwidgetitem3.setCheckState(Qt.Checked);
        __qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_field_manager)
        __qlistwidgetitem4.setCheckState(Qt.Checked);
        __qlistwidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget_field_manager)
        __qlistwidgetitem5.setCheckState(Qt.Checked);
        __qlistwidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget_field_manager)
        __qlistwidgetitem6.setCheckState(Qt.Checked);
        __qlistwidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget_field_manager)
        __qlistwidgetitem7.setCheckState(Qt.Checked);
        __qlistwidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget_field_manager.setObjectName(u"listWidget_field_manager")
        self.listWidget_field_manager.setGeometry(QRect(10, 70, 341, 101))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 251, 21))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.comboBox_field_modificator = QComboBox(Dialog)
        self.comboBox_field_modificator.addItem("")
        self.comboBox_field_modificator.addItem("")
        self.comboBox_field_modificator.addItem("")
        self.comboBox_field_modificator.addItem("")
        self.comboBox_field_modificator.addItem("")
        self.comboBox_field_modificator.addItem("")
        self.comboBox_field_modificator.addItem("")
        self.comboBox_field_modificator.addItem("")
        self.comboBox_field_modificator.setObjectName(u"comboBox_field_modificator")
        self.comboBox_field_modificator.setGeometry(QRect(10, 210, 341, 29))
        self.label_modificar_field = QLabel(Dialog)
        self.label_modificar_field.setObjectName(u"label_modificar_field")
        self.label_modificar_field.setGeometry(QRect(10, 180, 341, 21))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.label_modificar_field.setFont(font1)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 250, 111, 21))
        self.label_3.setFont(font1)
        self.lineEdit_valor_del_campo_modificado = QLineEdit(Dialog)
        self.lineEdit_valor_del_campo_modificado.setObjectName(u"lineEdit_valor_del_campo_modificado")
        self.lineEdit_valor_del_campo_modificado.setEnabled(False)
        self.lineEdit_valor_del_campo_modificado.setGeometry(QRect(10, 280, 341, 29))
        self.label_descriptor_del_filtro = QLabel(Dialog)
        self.label_descriptor_del_filtro.setObjectName(u"label_descriptor_del_filtro")
        self.label_descriptor_del_filtro.setGeometry(QRect(9, 350, 341, 71))
        self.label_descriptor_del_filtro.setScaledContents(False)
        self.label_descriptor_del_filtro.setWordWrap(True)
        self.textEdit_plantilla_del_filtro = QTextEdit(Dialog)
        self.textEdit_plantilla_del_filtro.setObjectName(u"textEdit_plantilla_del_filtro")
        self.textEdit_plantilla_del_filtro.setGeometry(QRect(363, 70, 391, 271))
        self.textEdit_plantilla_del_filtro.setReadOnly(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 30, 251, 21))
        self.label_2.setFont(font)
        self.label_filas_de_rsultados = QLabel(Dialog)
        self.label_filas_de_rsultados.setObjectName(u"label_filas_de_rsultados")
        self.label_filas_de_rsultados.setGeometry(QRect(360, 350, 391, 71))
        self.label_filas_de_rsultados.setAlignment(Qt.AlignCenter)
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 50, 281, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(360, 50, 341, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.comboBox_valor_del_filtro = QComboBox(Dialog)
        self.comboBox_valor_del_filtro.addItem("")
        self.comboBox_valor_del_filtro.addItem("")
        self.comboBox_valor_del_filtro.addItem("")
        self.comboBox_valor_del_filtro.addItem("")
        self.comboBox_valor_del_filtro.addItem("")
        self.comboBox_valor_del_filtro.addItem("")
        self.comboBox_valor_del_filtro.addItem("")
        self.comboBox_valor_del_filtro.addItem("")
        self.comboBox_valor_del_filtro.setObjectName(u"comboBox_valor_del_filtro")
        self.comboBox_valor_del_filtro.setEnabled(False)
        self.comboBox_valor_del_filtro.setGeometry(QRect(10, 310, 341, 29))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Filtros Avanzados", None))
#if QT_CONFIG(tooltip)
        self.buttonBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.toolButton_filter_options.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Opciones de los filtros</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_filter_options.setText(QCoreApplication.translate("Dialog", u"...", None))

        __sortingEnabled = self.listWidget_field_manager.isSortingEnabled()
        self.listWidget_field_manager.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_field_manager.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"id", None));
        ___qlistwidgetitem1 = self.listWidget_field_manager.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"date", None));
        ___qlistwidgetitem2 = self.listWidget_field_manager.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"entry_counter", None));
        ___qlistwidgetitem3 = self.listWidget_field_manager.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"is_sale", None));
        ___qlistwidgetitem4 = self.listWidget_field_manager.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"is_new", None));
        ___qlistwidgetitem5 = self.listWidget_field_manager.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Dialog", u"is_consignation", None));
        ___qlistwidgetitem6 = self.listWidget_field_manager.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Dialog", u"item_name", None));
        ___qlistwidgetitem7 = self.listWidget_field_manager.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Dialog", u"item_code", None));
        self.listWidget_field_manager.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.listWidget_field_manager.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Marque los campos que desea ver en el filtro y seleccione si desea aplicar alguna condicion a los resultados del campo</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Dialog", u"Campos a mostrar: ", None))
        self.comboBox_field_modificator.setItemText(0, QCoreApplication.translate("Dialog", u"\"None\"  Mostrar todo ", None))
        self.comboBox_field_modificator.setItemText(1, QCoreApplication.translate("Dialog", u"\"=\" Mostrar iguales a", None))
        self.comboBox_field_modificator.setItemText(2, QCoreApplication.translate("Dialog", u"\"<>\" Mostrar todos excepto", None))
        self.comboBox_field_modificator.setItemText(3, QCoreApplication.translate("Dialog", u"\"<\" Mostrar menores que", None))
        self.comboBox_field_modificator.setItemText(4, QCoreApplication.translate("Dialog", u"\"<=\" Mostrar menores o iguales que", None))
        self.comboBox_field_modificator.setItemText(5, QCoreApplication.translate("Dialog", u"\">\" Mostrar mayores que", None))
        self.comboBox_field_modificator.setItemText(6, QCoreApplication.translate("Dialog", u"\">=\" Mostrar mayores o iguales que", None))
        self.comboBox_field_modificator.setItemText(7, QCoreApplication.translate("Dialog", u"\"regexp\" Mostrar similares a", None))

#if QT_CONFIG(tooltip)
        self.comboBox_field_modificator.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Escoja el operador para afectar los resultados del campo</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_modificar_field.setText(QCoreApplication.translate("Dialog", u"Modificar el resultado de: {}", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Con el valor: ", None))
        self.lineEdit_valor_del_campo_modificado.setPlaceholderText(QCoreApplication.translate("Dialog", u"Valor del filtro...", None))
        self.label_descriptor_del_filtro.setText(QCoreApplication.translate("Dialog", u"El campo {} solo va a mostrar las filas {} {}", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Plantilla del Filtro a aplicar:", None))
        self.label_filas_de_rsultados.setText(QCoreApplication.translate("Dialog", u"Los resultados abarcan {} filas.", None))
        self.comboBox_valor_del_filtro.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox_valor_del_filtro.setItemText(1, QCoreApplication.translate("Dialog", u"Value1", None))
        self.comboBox_valor_del_filtro.setItemText(2, QCoreApplication.translate("Dialog", u"value2", None))
        self.comboBox_valor_del_filtro.setItemText(3, QCoreApplication.translate("Dialog", u"value3", None))
        self.comboBox_valor_del_filtro.setItemText(4, QCoreApplication.translate("Dialog", u"value4", None))
        self.comboBox_valor_del_filtro.setItemText(5, QCoreApplication.translate("Dialog", u"value5", None))
        self.comboBox_valor_del_filtro.setItemText(6, QCoreApplication.translate("Dialog", u"value6", None))
        self.comboBox_valor_del_filtro.setItemText(7, QCoreApplication.translate("Dialog", u"value7", None))

    # retranslateUi

