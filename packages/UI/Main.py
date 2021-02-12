# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_v3.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1318, 609)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionA_adir_Ventas = QAction(MainWindow)
        self.actionA_adir_Ventas.setObjectName(u"actionA_adir_Ventas")
        self.actionA_adir_Compras = QAction(MainWindow)
        self.actionA_adir_Compras.setObjectName(u"actionA_adir_Compras")
        self.actionA_adir_Compras_2 = QAction(MainWindow)
        self.actionA_adir_Compras_2.setObjectName(u"actionA_adir_Compras_2")
        self.actionA_adir_Compras_2.setShortcutContext(Qt.WindowShortcut)
        self.actionA_adir_Ventas_2 = QAction(MainWindow)
        self.actionA_adir_Ventas_2.setObjectName(u"actionA_adir_Ventas_2")
        self.actionA_adir_Ventas_2.setShortcutContext(Qt.WindowShortcut)
        self.actionModificar_la_inversion = QAction(MainWindow)
        self.actionModificar_la_inversion.setObjectName(u"actionModificar_la_inversion")
        self.actionModificar_la_inversion.setShortcutContext(Qt.WindowShortcut)
        self.actionCelulares = QAction(MainWindow)
        self.actionCelulares.setObjectName(u"actionCelulares")
        self.actionBistueria = QAction(MainWindow)
        self.actionBistueria.setObjectName(u"actionBistueria")
        self.actionZapatos = QAction(MainWindow)
        self.actionZapatos.setObjectName(u"actionZapatos")
        self.actionCrear_una_nueva_base_de_datos = QAction(MainWindow)
        self.actionCrear_una_nueva_base_de_datos.setObjectName(u"actionCrear_una_nueva_base_de_datos")
        self.actionGuardar_el_estado_de_la_aplicacion = QAction(MainWindow)
        self.actionGuardar_el_estado_de_la_aplicacion.setObjectName(u"actionGuardar_el_estado_de_la_aplicacion")
        self.actionGuardar_el_estado_de_la_aplicacion.setShortcutContext(Qt.ApplicationShortcut)
        self.actionGuardar_el_estado_de_la_base_de_datos = QAction(MainWindow)
        self.actionGuardar_el_estado_de_la_base_de_datos.setObjectName(u"actionGuardar_el_estado_de_la_base_de_datos")
        self.actionCrear_nueva = QAction(MainWindow)
        self.actionCrear_nueva.setObjectName(u"actionCrear_nueva")
        self.actionSalvar_el_estado_de_la_DB_actual = QAction(MainWindow)
        self.actionSalvar_el_estado_de_la_DB_actual.setObjectName(u"actionSalvar_el_estado_de_la_DB_actual")
        self.action_connect_Celulares = QAction(MainWindow)
        self.action_connect_Celulares.setObjectName(u"action_connect_Celulares")
        self.action_connect_Zapatos = QAction(MainWindow)
        self.action_connect_Zapatos.setObjectName(u"action_connect_Zapatos")
        self.action_connect_Bisuteria = QAction(MainWindow)
        self.action_connect_Bisuteria.setObjectName(u"action_connect_Bisuteria")
        self.actionCerrar_la_aplicacion = QAction(MainWindow)
        self.actionCerrar_la_aplicacion.setObjectName(u"actionCerrar_la_aplicacion")
        self.actionCerrar_la_aplicacion.setShortcutContext(Qt.ApplicationShortcut)
        self.actionExportar_Diario_hacia_CSV = QAction(MainWindow)
        self.actionExportar_Diario_hacia_CSV.setObjectName(u"actionExportar_Diario_hacia_CSV")
        self.actionExportar_Diario_hacia_CSV.setShortcutContext(Qt.WindowShortcut)
        self.actionImportar_datos_desde_CSV = QAction(MainWindow)
        self.actionImportar_datos_desde_CSV.setObjectName(u"actionImportar_datos_desde_CSV")
        self.actionImportar_datos_desde_CSV.setShortcutContext(Qt.WindowShortcut)
        self.actionCambiar_la_fecha_de_la_sesion = QAction(MainWindow)
        self.actionCambiar_la_fecha_de_la_sesion.setObjectName(u"actionCambiar_la_fecha_de_la_sesion")
        self.actionAyuda_offline = QAction(MainWindow)
        self.actionAyuda_offline.setObjectName(u"actionAyuda_offline")
        self.actionAyuda_offline.setShortcutContext(Qt.ApplicationShortcut)
        self.actionUsar_verificacion_de_datos = QAction(MainWindow)
        self.actionUsar_verificacion_de_datos.setObjectName(u"actionUsar_verificacion_de_datos")
        self.actionUsar_verificacion_de_datos.setCheckable(True)
        self.actionUsar_verificacion_de_datos.setChecked(True)
        self.actionVer_Inventario = QAction(MainWindow)
        self.actionVer_Inventario.setObjectName(u"actionVer_Inventario")
        self.actionVer_Ventas = QAction(MainWindow)
        self.actionVer_Ventas.setObjectName(u"actionVer_Ventas")
        self.actionVer_Capital = QAction(MainWindow)
        self.actionVer_Capital.setObjectName(u"actionVer_Capital")
        self.actionVer_Diario = QAction(MainWindow)
        self.actionVer_Diario.setObjectName(u"actionVer_Diario")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1311, 581))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tableWidget_table_display = QTableWidget(self.tab_1)
        self.tableWidget_table_display.setObjectName(u"tableWidget_table_display")
        self.tableWidget_table_display.setGeometry(QRect(10, 50, 1291, 471))
        self.horizontalLayoutWidget = QWidget(self.tab_1)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 1291, 32))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.label_current_database = QLabel(self.horizontalLayoutWidget)
        self.label_current_database.setObjectName(u"label_current_database")

        self.horizontalLayout.addWidget(self.label_current_database)

        self.line = QFrame(self.horizontalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFont(font)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_data_session = QLabel(self.horizontalLayoutWidget)
        self.label_data_session.setObjectName(u"label_data_session")

        self.horizontalLayout.addWidget(self.label_data_session)

        self.line_3 = QFrame(self.horizontalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout.addWidget(self.label_7)

        self.label_table_on_display = QLabel(self.horizontalLayoutWidget)
        self.label_table_on_display.setObjectName(u"label_table_on_display")

        self.horizontalLayout.addWidget(self.label_table_on_display)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_filter = QToolButton(self.horizontalLayoutWidget)
        self.toolButton_filter.setObjectName(u"toolButton_filter")

        self.horizontalLayout.addWidget(self.toolButton_filter)

        self.pushButton_export_table = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_export_table.setObjectName(u"pushButton_export_table")

        self.horizontalLayout.addWidget(self.pushButton_export_table)

        self.pushButton_print_table = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_print_table.setObjectName(u"pushButton_print_table")

        self.horizontalLayout.addWidget(self.pushButton_print_table)

        self.line_2 = QFrame(self.horizontalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_app_clock = QLabel(self.horizontalLayoutWidget)
        self.label_app_clock.setObjectName(u"label_app_clock")
        self.label_app_clock.setFont(font)

        self.horizontalLayout.addWidget(self.label_app_clock)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.line_40 = QFrame(self.tab_2)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setGeometry(QRect(690, 50, 20, 391))
        self.line_40.setFrameShape(QFrame.VLine)
        self.line_40.setFrameShadow(QFrame.Sunken)
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 30, 421, 20))
        font1 = QFont()
        font1.setItalic(True)
        self.label_10.setFont(font1)
        self.verticalLayoutWidget_16 = QWidget(self.tab_2)
        self.verticalLayoutWidget_16.setObjectName(u"verticalLayoutWidget_16")
        self.verticalLayoutWidget_16.setGeometry(QRect(10, 60, 681, 448))
        self.verticalLayout_20 = QVBoxLayout(self.verticalLayoutWidget_16)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.l005Label_7 = QLabel(self.verticalLayoutWidget_16)
        self.l005Label_7.setObjectName(u"l005Label_7")
        self.l005Label_7.setFont(font)

        self.horizontalLayout_17.addWidget(self.l005Label_7)

        self.line_22 = QFrame(self.verticalLayoutWidget_16)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.VLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.line_22)

        self.l005Label_8 = QLabel(self.verticalLayoutWidget_16)
        self.l005Label_8.setObjectName(u"l005Label_8")
        self.l005Label_8.setFont(font)

        self.horizontalLayout_17.addWidget(self.l005Label_8)


        self.verticalLayout_20.addLayout(self.horizontalLayout_17)

        self.line_21 = QFrame(self.verticalLayoutWidget_16)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_20.addWidget(self.line_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.q005Label_3 = QLabel(self.verticalLayoutWidget_16)
        self.q005Label_3.setObjectName(u"q005Label_3")
        self.q005Label_3.setFont(font)

        self.verticalLayout_12.addWidget(self.q005Label_3)

        self.q010Label_3 = QLabel(self.verticalLayoutWidget_16)
        self.q010Label_3.setObjectName(u"q010Label_3")
        self.q010Label_3.setFont(font)

        self.verticalLayout_12.addWidget(self.q010Label_3)

        self.q025Label_3 = QLabel(self.verticalLayoutWidget_16)
        self.q025Label_3.setObjectName(u"q025Label_3")
        self.q025Label_3.setFont(font)

        self.verticalLayout_12.addWidget(self.q025Label_3)

        self.q050Label_3 = QLabel(self.verticalLayoutWidget_16)
        self.q050Label_3.setObjectName(u"q050Label_3")
        self.q050Label_3.setFont(font)

        self.verticalLayout_12.addWidget(self.q050Label_3)

        self.q100Label_5 = QLabel(self.verticalLayoutWidget_16)
        self.q100Label_5.setObjectName(u"q100Label_5")
        self.q100Label_5.setFont(font)

        self.verticalLayout_12.addWidget(self.q100Label_5)

        self.q300Label_5 = QLabel(self.verticalLayoutWidget_16)
        self.q300Label_5.setObjectName(u"q300Label_5")
        self.q300Label_5.setFont(font)

        self.verticalLayout_12.addWidget(self.q300Label_5)

        self.q500Label_5 = QLabel(self.verticalLayoutWidget_16)
        self.q500Label_5.setObjectName(u"q500Label_5")
        self.q500Label_5.setFont(font)

        self.verticalLayout_12.addWidget(self.q500Label_5)

        self.q1000Label_5 = QLabel(self.verticalLayoutWidget_16)
        self.q1000Label_5.setObjectName(u"q1000Label_5")
        self.q1000Label_5.setFont(font)

        self.verticalLayout_12.addWidget(self.q1000Label_5)

        self.q2000Label_5 = QLabel(self.verticalLayoutWidget_16)
        self.q2000Label_5.setObjectName(u"q2000Label_5")
        self.q2000Label_5.setFont(font)

        self.verticalLayout_12.addWidget(self.q2000Label_5)

        self.q5000Label_5 = QLabel(self.verticalLayoutWidget_16)
        self.q5000Label_5.setObjectName(u"q5000Label_5")
        self.q5000Label_5.setFont(font)

        self.verticalLayout_12.addWidget(self.q5000Label_5)

        self.q10000Label_5 = QLabel(self.verticalLayoutWidget_16)
        self.q10000Label_5.setObjectName(u"q10000Label_5")
        self.q10000Label_5.setFont(font)

        self.verticalLayout_12.addWidget(self.q10000Label_5)


        self.horizontalLayout_18.addLayout(self.verticalLayout_12)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.spinBox_cuc5cent = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cuc5cent.setObjectName(u"spinBox_cuc5cent")
        self.spinBox_cuc5cent.setMaximum(100000000)

        self.verticalLayout_15.addWidget(self.spinBox_cuc5cent)

        self.spinBox_cuc10cent = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cuc10cent.setObjectName(u"spinBox_cuc10cent")
        self.spinBox_cuc10cent.setMaximum(100000000)

        self.verticalLayout_15.addWidget(self.spinBox_cuc10cent)

        self.spinBox_cuc25cent = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cuc25cent.setObjectName(u"spinBox_cuc25cent")
        self.spinBox_cuc25cent.setMaximum(100000000)

        self.verticalLayout_15.addWidget(self.spinBox_cuc25cent)

        self.spinBox_cuc50cent = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cuc50cent.setObjectName(u"spinBox_cuc50cent")
        self.spinBox_cuc50cent.setMaximum(100000000)

        self.verticalLayout_15.addWidget(self.spinBox_cuc50cent)

        self.spinBox_cuc1 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cuc1.setObjectName(u"spinBox_cuc1")
        self.spinBox_cuc1.setMaximum(100000000)

        self.verticalLayout_15.addWidget(self.spinBox_cuc1)

        self.spinBox_cuc3 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cuc3.setObjectName(u"spinBox_cuc3")
        self.spinBox_cuc3.setMaximum(100000000)

        self.verticalLayout_15.addWidget(self.spinBox_cuc3)

        self.spinBox_cuc5 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cuc5.setObjectName(u"spinBox_cuc5")
        self.spinBox_cuc5.setMaximum(100000000)

        self.verticalLayout_15.addWidget(self.spinBox_cuc5)

        self.spinBox_cuc10 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cuc10.setObjectName(u"spinBox_cuc10")
        self.spinBox_cuc10.setMaximum(100000000)

        self.verticalLayout_15.addWidget(self.spinBox_cuc10)

        self.spinBox_cuc20 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cuc20.setObjectName(u"spinBox_cuc20")
        self.spinBox_cuc20.setMaximum(100000000)

        self.verticalLayout_15.addWidget(self.spinBox_cuc20)

        self.spinBox_cuc50 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cuc50.setObjectName(u"spinBox_cuc50")
        self.spinBox_cuc50.setMaximum(100000000)

        self.verticalLayout_15.addWidget(self.spinBox_cuc50)

        self.spinBox_cuc100 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cuc100.setObjectName(u"spinBox_cuc100")
        self.spinBox_cuc100.setMaximum(100000000)

        self.verticalLayout_15.addWidget(self.spinBox_cuc100)


        self.horizontalLayout_18.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.cuc5centsumlabel = QLabel(self.verticalLayoutWidget_16)
        self.cuc5centsumlabel.setObjectName(u"cuc5centsumlabel")

        self.verticalLayout_16.addWidget(self.cuc5centsumlabel)

        self.cuc10centsumlabel = QLabel(self.verticalLayoutWidget_16)
        self.cuc10centsumlabel.setObjectName(u"cuc10centsumlabel")

        self.verticalLayout_16.addWidget(self.cuc10centsumlabel)

        self.cuc25centsumlabel = QLabel(self.verticalLayoutWidget_16)
        self.cuc25centsumlabel.setObjectName(u"cuc25centsumlabel")

        self.verticalLayout_16.addWidget(self.cuc25centsumlabel)

        self.cuc50centsumlabel = QLabel(self.verticalLayoutWidget_16)
        self.cuc50centsumlabel.setObjectName(u"cuc50centsumlabel")

        self.verticalLayout_16.addWidget(self.cuc50centsumlabel)

        self.cuc1sumlabel = QLabel(self.verticalLayoutWidget_16)
        self.cuc1sumlabel.setObjectName(u"cuc1sumlabel")

        self.verticalLayout_16.addWidget(self.cuc1sumlabel)

        self.cuc3sumlabel = QLabel(self.verticalLayoutWidget_16)
        self.cuc3sumlabel.setObjectName(u"cuc3sumlabel")

        self.verticalLayout_16.addWidget(self.cuc3sumlabel)

        self.cuc5sumlabel = QLabel(self.verticalLayoutWidget_16)
        self.cuc5sumlabel.setObjectName(u"cuc5sumlabel")

        self.verticalLayout_16.addWidget(self.cuc5sumlabel)

        self.cuc10sumlabel = QLabel(self.verticalLayoutWidget_16)
        self.cuc10sumlabel.setObjectName(u"cuc10sumlabel")

        self.verticalLayout_16.addWidget(self.cuc10sumlabel)

        self.cuc20sumlabel = QLabel(self.verticalLayoutWidget_16)
        self.cuc20sumlabel.setObjectName(u"cuc20sumlabel")

        self.verticalLayout_16.addWidget(self.cuc20sumlabel)

        self.cuc50sumlabel = QLabel(self.verticalLayoutWidget_16)
        self.cuc50sumlabel.setObjectName(u"cuc50sumlabel")

        self.verticalLayout_16.addWidget(self.cuc50sumlabel)

        self.cuc100sumlabel = QLabel(self.verticalLayoutWidget_16)
        self.cuc100sumlabel.setObjectName(u"cuc100sumlabel")

        self.verticalLayout_16.addWidget(self.cuc100sumlabel)


        self.horizontalLayout_18.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.cucTocup5centlabel = QLabel(self.verticalLayoutWidget_16)
        self.cucTocup5centlabel.setObjectName(u"cucTocup5centlabel")

        self.verticalLayout_17.addWidget(self.cucTocup5centlabel)

        self.cucTocup10centlabel = QLabel(self.verticalLayoutWidget_16)
        self.cucTocup10centlabel.setObjectName(u"cucTocup10centlabel")

        self.verticalLayout_17.addWidget(self.cucTocup10centlabel)

        self.cucTocup25centlabel = QLabel(self.verticalLayoutWidget_16)
        self.cucTocup25centlabel.setObjectName(u"cucTocup25centlabel")

        self.verticalLayout_17.addWidget(self.cucTocup25centlabel)

        self.cucTocup50centlabel = QLabel(self.verticalLayoutWidget_16)
        self.cucTocup50centlabel.setObjectName(u"cucTocup50centlabel")

        self.verticalLayout_17.addWidget(self.cucTocup50centlabel)

        self.cucTocup1label = QLabel(self.verticalLayoutWidget_16)
        self.cucTocup1label.setObjectName(u"cucTocup1label")

        self.verticalLayout_17.addWidget(self.cucTocup1label)

        self.cucTocup3label = QLabel(self.verticalLayoutWidget_16)
        self.cucTocup3label.setObjectName(u"cucTocup3label")

        self.verticalLayout_17.addWidget(self.cucTocup3label)

        self.cucTocup5label = QLabel(self.verticalLayoutWidget_16)
        self.cucTocup5label.setObjectName(u"cucTocup5label")

        self.verticalLayout_17.addWidget(self.cucTocup5label)

        self.cucTocup10label = QLabel(self.verticalLayoutWidget_16)
        self.cucTocup10label.setObjectName(u"cucTocup10label")

        self.verticalLayout_17.addWidget(self.cucTocup10label)

        self.cucTocup20label = QLabel(self.verticalLayoutWidget_16)
        self.cucTocup20label.setObjectName(u"cucTocup20label")

        self.verticalLayout_17.addWidget(self.cucTocup20label)

        self.cucTocup50label = QLabel(self.verticalLayoutWidget_16)
        self.cucTocup50label.setObjectName(u"cucTocup50label")

        self.verticalLayout_17.addWidget(self.cucTocup50label)

        self.cucTocup100label = QLabel(self.verticalLayoutWidget_16)
        self.cucTocup100label.setObjectName(u"cucTocup100label")

        self.verticalLayout_17.addWidget(self.cucTocup100label)


        self.horizontalLayout_18.addLayout(self.verticalLayout_17)

        self.line_9 = QFrame(self.verticalLayoutWidget_16)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_18.addWidget(self.line_9)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.p005Label_9 = QLabel(self.verticalLayoutWidget_16)
        self.p005Label_9.setObjectName(u"p005Label_9")
        self.p005Label_9.setFont(font)

        self.verticalLayout_21.addWidget(self.p005Label_9)

        self.p010Label_7 = QLabel(self.verticalLayoutWidget_16)
        self.p010Label_7.setObjectName(u"p010Label_7")
        self.p010Label_7.setFont(font)

        self.verticalLayout_21.addWidget(self.p010Label_7)

        self.p025Label_7 = QLabel(self.verticalLayoutWidget_16)
        self.p025Label_7.setObjectName(u"p025Label_7")
        self.p025Label_7.setFont(font)

        self.verticalLayout_21.addWidget(self.p025Label_7)

        self.p050Label_7 = QLabel(self.verticalLayoutWidget_16)
        self.p050Label_7.setObjectName(u"p050Label_7")
        self.p050Label_7.setFont(font)

        self.verticalLayout_21.addWidget(self.p050Label_7)

        self.p2000Label_9 = QLabel(self.verticalLayoutWidget_16)
        self.p2000Label_9.setObjectName(u"p2000Label_9")
        self.p2000Label_9.setFont(font)

        self.verticalLayout_21.addWidget(self.p2000Label_9)

        self.p5000Label_9 = QLabel(self.verticalLayoutWidget_16)
        self.p5000Label_9.setObjectName(u"p5000Label_9")
        self.p5000Label_9.setFont(font)

        self.verticalLayout_21.addWidget(self.p5000Label_9)

        self.p10000Label_9 = QLabel(self.verticalLayoutWidget_16)
        self.p10000Label_9.setObjectName(u"p10000Label_9")
        self.p10000Label_9.setFont(font)

        self.verticalLayout_21.addWidget(self.p10000Label_9)

        self.p10000Label_11 = QLabel(self.verticalLayoutWidget_16)
        self.p10000Label_11.setObjectName(u"p10000Label_11")
        self.p10000Label_11.setFont(font)

        self.verticalLayout_21.addWidget(self.p10000Label_11)

        self.p10000Label_12 = QLabel(self.verticalLayoutWidget_16)
        self.p10000Label_12.setObjectName(u"p10000Label_12")
        self.p10000Label_12.setFont(font)

        self.verticalLayout_21.addWidget(self.p10000Label_12)

        self.p10000Label_13 = QLabel(self.verticalLayoutWidget_16)
        self.p10000Label_13.setObjectName(u"p10000Label_13")
        self.p10000Label_13.setFont(font)

        self.verticalLayout_21.addWidget(self.p10000Label_13)


        self.horizontalLayout_19.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.spinBox_cup1 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cup1.setObjectName(u"spinBox_cup1")
        self.spinBox_cup1.setMaximum(100000000)

        self.verticalLayout_22.addWidget(self.spinBox_cup1)

        self.spinBox_cup3 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cup3.setObjectName(u"spinBox_cup3")
        self.spinBox_cup3.setMaximum(100000000)

        self.verticalLayout_22.addWidget(self.spinBox_cup3)

        self.spinBox_cup5 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cup5.setObjectName(u"spinBox_cup5")
        self.spinBox_cup5.setMaximum(100000000)

        self.verticalLayout_22.addWidget(self.spinBox_cup5)

        self.spinBox_cup10 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cup10.setObjectName(u"spinBox_cup10")
        self.spinBox_cup10.setMaximum(100000000)

        self.verticalLayout_22.addWidget(self.spinBox_cup10)

        self.spinBox_cup20 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cup20.setObjectName(u"spinBox_cup20")
        self.spinBox_cup20.setMaximum(100000000)

        self.verticalLayout_22.addWidget(self.spinBox_cup20)

        self.spinBox_cup50 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cup50.setObjectName(u"spinBox_cup50")
        self.spinBox_cup50.setMaximum(100000000)

        self.verticalLayout_22.addWidget(self.spinBox_cup50)

        self.spinBox_cup100 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cup100.setObjectName(u"spinBox_cup100")
        self.spinBox_cup100.setMaximum(100000000)

        self.verticalLayout_22.addWidget(self.spinBox_cup100)

        self.spinBox_cup200 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cup200.setObjectName(u"spinBox_cup200")
        self.spinBox_cup200.setMaximum(100000000)

        self.verticalLayout_22.addWidget(self.spinBox_cup200)

        self.spinBox_cup500 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cup500.setObjectName(u"spinBox_cup500")
        self.spinBox_cup500.setMaximum(100000000)

        self.verticalLayout_22.addWidget(self.spinBox_cup500)

        self.spinBox_cup1000 = QSpinBox(self.verticalLayoutWidget_16)
        self.spinBox_cup1000.setObjectName(u"spinBox_cup1000")
        self.spinBox_cup1000.setMaximum(100000000)

        self.verticalLayout_22.addWidget(self.spinBox_cup1000)


        self.horizontalLayout_19.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_cup1 = QLabel(self.verticalLayoutWidget_16)
        self.label_cup1.setObjectName(u"label_cup1")

        self.verticalLayout_23.addWidget(self.label_cup1)

        self.label_cup3 = QLabel(self.verticalLayoutWidget_16)
        self.label_cup3.setObjectName(u"label_cup3")

        self.verticalLayout_23.addWidget(self.label_cup3)

        self.label_cup5 = QLabel(self.verticalLayoutWidget_16)
        self.label_cup5.setObjectName(u"label_cup5")

        self.verticalLayout_23.addWidget(self.label_cup5)

        self.label_cup10 = QLabel(self.verticalLayoutWidget_16)
        self.label_cup10.setObjectName(u"label_cup10")

        self.verticalLayout_23.addWidget(self.label_cup10)

        self.label_cup20 = QLabel(self.verticalLayoutWidget_16)
        self.label_cup20.setObjectName(u"label_cup20")

        self.verticalLayout_23.addWidget(self.label_cup20)

        self.label_cup50 = QLabel(self.verticalLayoutWidget_16)
        self.label_cup50.setObjectName(u"label_cup50")

        self.verticalLayout_23.addWidget(self.label_cup50)

        self.label_cup100 = QLabel(self.verticalLayoutWidget_16)
        self.label_cup100.setObjectName(u"label_cup100")

        self.verticalLayout_23.addWidget(self.label_cup100)

        self.label_cup200 = QLabel(self.verticalLayoutWidget_16)
        self.label_cup200.setObjectName(u"label_cup200")

        self.verticalLayout_23.addWidget(self.label_cup200)

        self.label_cup500 = QLabel(self.verticalLayoutWidget_16)
        self.label_cup500.setObjectName(u"label_cup500")

        self.verticalLayout_23.addWidget(self.label_cup500)

        self.label_cup1000 = QLabel(self.verticalLayoutWidget_16)
        self.label_cup1000.setObjectName(u"label_cup1000")

        self.verticalLayout_23.addWidget(self.label_cup1000)


        self.horizontalLayout_19.addLayout(self.verticalLayout_23)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_18)


        self.verticalLayout_20.addLayout(self.horizontalLayout_20)

        self.verticalLayoutWidget_7 = QWidget(self.tab_2)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(710, 150, 424, 134))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.verticalLayoutWidget_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.verticalLayout_11.addWidget(self.label_21)

        self.line_10 = QFrame(self.verticalLayoutWidget_7)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_10)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_24 = QLabel(self.verticalLayoutWidget_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.horizontalLayout_31.addWidget(self.label_24)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_6)

        self.label_monto_total_calculator = QLabel(self.verticalLayoutWidget_7)
        self.label_monto_total_calculator.setObjectName(u"label_monto_total_calculator")

        self.horizontalLayout_31.addWidget(self.label_monto_total_calculator)


        self.verticalLayout_18.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_22 = QLabel(self.verticalLayoutWidget_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.horizontalLayout_30.addWidget(self.label_22)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_5)

        self.checkBox_use_calculator = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_use_calculator.setObjectName(u"checkBox_use_calculator")

        self.horizontalLayout_30.addWidget(self.checkBox_use_calculator)

        self.doubleSpinBox_dineroEsperado = QDoubleSpinBox(self.verticalLayoutWidget_7)
        self.doubleSpinBox_dineroEsperado.setObjectName(u"doubleSpinBox_dineroEsperado")
        self.doubleSpinBox_dineroEsperado.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.doubleSpinBox_dineroEsperado.setProperty("showGroupSeparator", True)
        self.doubleSpinBox_dineroEsperado.setMaximum(100000000.989999994635582)

        self.horizontalLayout_30.addWidget(self.doubleSpinBox_dineroEsperado)


        self.verticalLayout_18.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_26 = QLabel(self.verticalLayoutWidget_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.horizontalLayout_32.addWidget(self.label_26)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_7)

        self.label_sobra_falta_palabra = QLabel(self.verticalLayoutWidget_7)
        self.label_sobra_falta_palabra.setObjectName(u"label_sobra_falta_palabra")
        self.label_sobra_falta_palabra.setFont(font)

        self.horizontalLayout_32.addWidget(self.label_sobra_falta_palabra)

        self.label_sobra_falta_cantidad = QLabel(self.verticalLayoutWidget_7)
        self.label_sobra_falta_cantidad.setObjectName(u"label_sobra_falta_cantidad")

        self.horizontalLayout_32.addWidget(self.label_sobra_falta_cantidad)


        self.verticalLayout_18.addLayout(self.horizontalLayout_32)


        self.verticalLayout_11.addLayout(self.verticalLayout_18)

        self.verticalLayoutWidget_6 = QWidget(self.tab_2)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(710, 60, 391, 85))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_19 = QLabel(self.verticalLayoutWidget_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.horizontalLayout_29.addWidget(self.label_19)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_10)

        self.label_montoCUPparcial = QLabel(self.verticalLayoutWidget_6)
        self.label_montoCUPparcial.setObjectName(u"label_montoCUPparcial")

        self.horizontalLayout_29.addWidget(self.label_montoCUPparcial)


        self.verticalLayout_10.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.verticalLayoutWidget_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_12)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_9)

        self.label_montoCUCparcial = QLabel(self.verticalLayoutWidget_6)
        self.label_montoCUCparcial.setObjectName(u"label_montoCUCparcial")

        self.horizontalLayout_15.addWidget(self.label_montoCUCparcial)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_13 = QLabel(self.verticalLayoutWidget_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.horizontalLayout_28.addWidget(self.label_13)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_8)

        self.label_montoCUCconvertido = QLabel(self.verticalLayoutWidget_6)
        self.label_montoCUCconvertido.setObjectName(u"label_montoCUCconvertido")

        self.horizontalLayout_28.addWidget(self.label_montoCUCconvertido)


        self.verticalLayout_10.addLayout(self.horizontalLayout_28)

        self.line_8 = QFrame(self.tab_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(10, 40, 911, 16))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.pushButton_reset_calc = QPushButton(self.tab_2)
        self.pushButton_reset_calc.setObjectName(u"pushButton_reset_calc")
        self.pushButton_reset_calc.setGeometry(QRect(928, 20, 171, 25))
        self.frame_calculator = QFrame(self.tab_2)
        self.frame_calculator.setObjectName(u"frame_calculator")
        self.frame_calculator.setEnabled(False)
        self.frame_calculator.setGeometry(QRect(710, 280, 391, 241))
        self.frame_calculator.setFrameShape(QFrame.StyledPanel)
        self.frame_calculator.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_13 = QWidget(self.frame_calculator)
        self.verticalLayoutWidget_13.setObjectName(u"verticalLayoutWidget_13")
        self.verticalLayoutWidget_13.setGeometry(QRect(10, 10, 372, 264))
        self.verticalLayout_14 = QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_calc_result = QLabel(self.verticalLayoutWidget_13)
        self.label_calc_result.setObjectName(u"label_calc_result")
        self.label_calc_result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_calc_result)

        self.line_11 = QFrame(self.verticalLayoutWidget_13)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_11)

        self.label_calc_operation = QLabel(self.verticalLayoutWidget_13)
        self.label_calc_operation.setObjectName(u"label_calc_operation")
        self.label_calc_operation.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_calc_operation)


        self.horizontalLayout_38.addLayout(self.verticalLayout_7)


        self.verticalLayout_14.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.pushButton_calc_clear = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_clear.setObjectName(u"pushButton_calc_clear")

        self.horizontalLayout_39.addWidget(self.pushButton_calc_clear)

        self.pushButton_calc_delete = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_delete.setObjectName(u"pushButton_calc_delete")

        self.horizontalLayout_39.addWidget(self.pushButton_calc_delete)

        self.pushButton_calc_store_value = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_store_value.setObjectName(u"pushButton_calc_store_value")

        self.horizontalLayout_39.addWidget(self.pushButton_calc_store_value)


        self.verticalLayout_6.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.pushButton_calc_1 = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_1.setObjectName(u"pushButton_calc_1")

        self.horizontalLayout_35.addWidget(self.pushButton_calc_1)

        self.pushButton_calc_2 = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_2.setObjectName(u"pushButton_calc_2")

        self.horizontalLayout_35.addWidget(self.pushButton_calc_2)

        self.pushButton_calc_3 = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_3.setObjectName(u"pushButton_calc_3")

        self.horizontalLayout_35.addWidget(self.pushButton_calc_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.pushButton_calc_4 = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_4.setObjectName(u"pushButton_calc_4")

        self.horizontalLayout_33.addWidget(self.pushButton_calc_4)

        self.pushButton_calc_5 = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_5.setObjectName(u"pushButton_calc_5")

        self.horizontalLayout_33.addWidget(self.pushButton_calc_5)

        self.pushButton_calc_6 = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_6.setObjectName(u"pushButton_calc_6")

        self.horizontalLayout_33.addWidget(self.pushButton_calc_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.pushButton_calc_7 = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_7.setObjectName(u"pushButton_calc_7")

        self.horizontalLayout_34.addWidget(self.pushButton_calc_7)

        self.pushButton_calc_8 = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_8.setObjectName(u"pushButton_calc_8")

        self.horizontalLayout_34.addWidget(self.pushButton_calc_8)

        self.pushButton_calc_9 = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_9.setObjectName(u"pushButton_calc_9")

        self.horizontalLayout_34.addWidget(self.pushButton_calc_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.pushButton_calc_cents = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_cents.setObjectName(u"pushButton_calc_cents")

        self.horizontalLayout_36.addWidget(self.pushButton_calc_cents)

        self.pushButton_calc_0 = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_0.setObjectName(u"pushButton_calc_0")

        self.horizontalLayout_36.addWidget(self.pushButton_calc_0)

        self.pushButton_calc_float = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_float.setObjectName(u"pushButton_calc_float")

        self.horizontalLayout_36.addWidget(self.pushButton_calc_float)


        self.verticalLayout_6.addLayout(self.horizontalLayout_36)


        self.horizontalLayout_37.addLayout(self.verticalLayout_6)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_calc_plus = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_plus.setObjectName(u"pushButton_calc_plus")

        self.verticalLayout_13.addWidget(self.pushButton_calc_plus)

        self.pushButton_calc_minus = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_minus.setObjectName(u"pushButton_calc_minus")

        self.verticalLayout_13.addWidget(self.pushButton_calc_minus)

        self.pushButton_calc_multiply = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_multiply.setObjectName(u"pushButton_calc_multiply")

        self.verticalLayout_13.addWidget(self.pushButton_calc_multiply)

        self.pushButton_calc_divide = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_divide.setObjectName(u"pushButton_calc_divide")

        self.verticalLayout_13.addWidget(self.pushButton_calc_divide)

        self.pushButton_calc_equal = QPushButton(self.verticalLayoutWidget_13)
        self.pushButton_calc_equal.setObjectName(u"pushButton_calc_equal")

        self.verticalLayout_13.addWidget(self.pushButton_calc_equal)


        self.horizontalLayout_37.addLayout(self.verticalLayout_13)


        self.verticalLayout_14.addLayout(self.horizontalLayout_37)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayoutWidget = QWidget(self.tab_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(670, 170, 601, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_33 = QLabel(self.verticalLayoutWidget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_33)

        self.label_plac_total_ventas = QLabel(self.verticalLayoutWidget)
        self.label_plac_total_ventas.setObjectName(u"label_plac_total_ventas")

        self.horizontalLayout_12.addWidget(self.label_plac_total_ventas)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_37 = QLabel(self.verticalLayoutWidget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_37)

        self.label_plac_total_net_proffit = QLabel(self.verticalLayoutWidget)
        self.label_plac_total_net_proffit.setObjectName(u"label_plac_total_net_proffit")

        self.horizontalLayout_14.addWidget(self.label_plac_total_net_proffit)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_41 = QLabel(self.verticalLayoutWidget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)

        self.horizontalLayout_21.addWidget(self.label_41)

        self.label_plac_total_real_proffit = QLabel(self.verticalLayoutWidget)
        self.label_plac_total_real_proffit.setObjectName(u"label_plac_total_real_proffit")

        self.horizontalLayout_21.addWidget(self.label_plac_total_real_proffit)


        self.verticalLayout.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_39 = QLabel(self.verticalLayoutWidget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_39)

        self.label_plac_total_capital_low = QLabel(self.verticalLayoutWidget)
        self.label_plac_total_capital_low.setObjectName(u"label_plac_total_capital_low")

        self.horizontalLayout_16.addWidget(self.label_plac_total_capital_low)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_43 = QLabel(self.verticalLayoutWidget)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)

        self.horizontalLayout_22.addWidget(self.label_43)

        self.label_plac_total_rob_capital = QLabel(self.verticalLayoutWidget)
        self.label_plac_total_rob_capital.setObjectName(u"label_plac_total_rob_capital")

        self.horizontalLayout_22.addWidget(self.label_plac_total_rob_capital)


        self.verticalLayout.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_35 = QLabel(self.verticalLayoutWidget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_35)

        self.label_plac_total_ary_capital = QLabel(self.verticalLayoutWidget)
        self.label_plac_total_ary_capital.setObjectName(u"label_plac_total_ary_capital")

        self.horizontalLayout_13.addWidget(self.label_plac_total_ary_capital)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.label_45 = QLabel(self.tab_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(10, 140, 311, 21))
        self.label_45.setFont(font)
        self.verticalLayoutWidget_2 = QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 170, 631, 265))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_48 = QLabel(self.verticalLayoutWidget_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)

        self.horizontalLayout_24.addWidget(self.label_48)

        self.label_plac_day_ventas = QLabel(self.verticalLayoutWidget_2)
        self.label_plac_day_ventas.setObjectName(u"label_plac_day_ventas")

        self.horizontalLayout_24.addWidget(self.label_plac_day_ventas)


        self.verticalLayout_2.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_46 = QLabel(self.verticalLayoutWidget_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)

        self.horizontalLayout_23.addWidget(self.label_46)

        self.label_plac_day_inversion = QLabel(self.verticalLayoutWidget_2)
        self.label_plac_day_inversion.setObjectName(u"label_plac_day_inversion")

        self.horizontalLayout_23.addWidget(self.label_plac_day_inversion)


        self.verticalLayout_2.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_52 = QLabel(self.verticalLayoutWidget_2)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font)

        self.horizontalLayout_41.addWidget(self.label_52)

        self.label_plac_day_net_proffit = QLabel(self.verticalLayoutWidget_2)
        self.label_plac_day_net_proffit.setObjectName(u"label_plac_day_net_proffit")

        self.horizontalLayout_41.addWidget(self.label_plac_day_net_proffit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_60 = QLabel(self.verticalLayoutWidget_2)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font)

        self.horizontalLayout_42.addWidget(self.label_60)

        self.label_plac_day_salary = QLabel(self.verticalLayoutWidget_2)
        self.label_plac_day_salary.setObjectName(u"label_plac_day_salary")

        self.horizontalLayout_42.addWidget(self.label_plac_day_salary)


        self.verticalLayout_2.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_16 = QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_16)

        self.label_plac_day_rent = QLabel(self.verticalLayoutWidget_2)
        self.label_plac_day_rent.setObjectName(u"label_plac_day_rent")

        self.horizontalLayout_6.addWidget(self.label_plac_day_rent)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_62 = QLabel(self.verticalLayoutWidget_2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font)

        self.horizontalLayout_43.addWidget(self.label_62)

        self.label_plac_day_real_proffit = QLabel(self.verticalLayoutWidget_2)
        self.label_plac_day_real_proffit.setObjectName(u"label_plac_day_real_proffit")

        self.horizontalLayout_43.addWidget(self.label_plac_day_real_proffit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_64 = QLabel(self.verticalLayoutWidget_2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font)

        self.horizontalLayout_44.addWidget(self.label_64)

        self.label_plac_day_part_proffit = QLabel(self.verticalLayoutWidget_2)
        self.label_plac_day_part_proffit.setObjectName(u"label_plac_day_part_proffit")

        self.horizontalLayout_44.addWidget(self.label_plac_day_part_proffit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_51 = QLabel(self.verticalLayoutWidget_2)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)

        self.horizontalLayout_26.addWidget(self.label_51)

        self.label_plac_day_compras = QLabel(self.verticalLayoutWidget_2)
        self.label_plac_day_compras.setObjectName(u"label_plac_day_compras")

        self.horizontalLayout_26.addWidget(self.label_plac_day_compras)


        self.verticalLayout_2.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_50 = QLabel(self.verticalLayoutWidget_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)

        self.horizontalLayout_25.addWidget(self.label_50)

        self.label_plac_day_consignation = QLabel(self.verticalLayoutWidget_2)
        self.label_plac_day_consignation.setObjectName(u"label_plac_day_consignation")

        self.horizontalLayout_25.addWidget(self.label_plac_day_consignation)


        self.verticalLayout_2.addLayout(self.horizontalLayout_25)

        self.pushButton_update_stats_tab = QPushButton(self.tab_3)
        self.pushButton_update_stats_tab.setObjectName(u"pushButton_update_stats_tab")
        self.pushButton_update_stats_tab.setGeometry(QRect(730, 80, 191, 25))
        self.dateEdit_intervalo_start = QDateEdit(self.tab_3)
        self.dateEdit_intervalo_start.setObjectName(u"dateEdit_intervalo_start")
        self.dateEdit_intervalo_start.setGeometry(QRect(950, 380, 131, 26))
        self.dateEdit_intervalo_start.setCalendarPopup(True)
        self.dateEdit_intervalo_start.setDate(QDate(2020, 1, 1))
        self.dateEdit_intervalo_stop = QDateEdit(self.tab_3)
        self.dateEdit_intervalo_stop.setObjectName(u"dateEdit_intervalo_stop")
        self.dateEdit_intervalo_stop.setGeometry(QRect(1100, 380, 141, 26))
        self.dateEdit_intervalo_stop.setCalendarPopup(True)
        self.dateEdit_intervalo_stop.setDate(QDate(2020, 1, 1))
        self.line_4 = QFrame(self.tab_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(640, 170, 20, 261))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.tab_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(10, 160, 401, 16))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_66 = QLabel(self.tab_3)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(670, 140, 311, 21))
        self.label_66.setFont(font)
        self.line_6 = QFrame(self.tab_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(670, 160, 341, 16))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.checkBox_ver_solo_intervalo = QCheckBox(self.tab_3)
        self.checkBox_ver_solo_intervalo.setObjectName(u"checkBox_ver_solo_intervalo")
        self.checkBox_ver_solo_intervalo.setGeometry(QRect(670, 380, 281, 23))
        self.pushButton_generar_tabla_totales = QPushButton(self.tab_3)
        self.pushButton_generar_tabla_totales.setObjectName(u"pushButton_generar_tabla_totales")
        self.pushButton_generar_tabla_totales.setGeometry(QRect(660, 470, 301, 25))
        self.pushButton_generate_table_all_days = QPushButton(self.tab_3)
        self.pushButton_generate_table_all_days.setObjectName(u"pushButton_generate_table_all_days")
        self.pushButton_generate_table_all_days.setGeometry(QRect(10, 470, 301, 25))
        self.label_67 = QLabel(self.tab_3)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(670, 420, 251, 21))
        self.label_67.setFont(font)
        self.comboBox_ambito_de_tabla = QComboBox(self.tab_3)
        self.comboBox_ambito_de_tabla.addItem("")
        self.comboBox_ambito_de_tabla.addItem("")
        self.comboBox_ambito_de_tabla.addItem("")
        self.comboBox_ambito_de_tabla.addItem("")
        self.comboBox_ambito_de_tabla.addItem("")
        self.comboBox_ambito_de_tabla.setObjectName(u"comboBox_ambito_de_tabla")
        self.comboBox_ambito_de_tabla.setGeometry(QRect(930, 420, 311, 25))
        self.frame = QFrame(self.tab_3)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 30, 701, 101))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.frame)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 10, 681, 85))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_70 = QLabel(self.verticalLayoutWidget_3)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font)

        self.horizontalLayout_46.addWidget(self.label_70)

        self.label_plac_capital_total = QLabel(self.verticalLayoutWidget_3)
        self.label_plac_capital_total.setObjectName(u"label_plac_capital_total")

        self.horizontalLayout_46.addWidget(self.label_plac_capital_total)


        self.verticalLayout_5.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_68 = QLabel(self.verticalLayoutWidget_3)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font)

        self.horizontalLayout_45.addWidget(self.label_68)

        self.label_plac_capital_invertido = QLabel(self.verticalLayoutWidget_3)
        self.label_plac_capital_invertido.setObjectName(u"label_plac_capital_invertido")

        self.horizontalLayout_45.addWidget(self.label_plac_capital_invertido)


        self.verticalLayout_5.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_72 = QLabel(self.verticalLayoutWidget_3)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font)

        self.horizontalLayout_47.addWidget(self.label_72)

        self.label_plac_cash_en_caja = QLabel(self.verticalLayoutWidget_3)
        self.label_plac_cash_en_caja.setObjectName(u"label_plac_cash_en_caja")

        self.horizontalLayout_47.addWidget(self.label_plac_cash_en_caja)


        self.verticalLayout_5.addLayout(self.horizontalLayout_47)

        self.label_74 = QLabel(self.tab_3)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(10, 0, 251, 21))
        self.label_74.setFont(font)
        self.pushButton_export_stats_tab = QPushButton(self.tab_3)
        self.pushButton_export_stats_tab.setObjectName(u"pushButton_export_stats_tab")
        self.pushButton_export_stats_tab.setGeometry(QRect(930, 80, 171, 25))
        self.pushButton_print_stats_tab = QPushButton(self.tab_3)
        self.pushButton_print_stats_tab.setObjectName(u"pushButton_print_stats_tab")
        self.pushButton_print_stats_tab.setGeometry(QRect(1110, 80, 171, 25))
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1318, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHerramientas = QMenu(self.menubar)
        self.menuHerramientas.setObjectName(u"menuHerramientas")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        self.menuBase_de_Datos = QMenu(self.menubar)
        self.menuBase_de_Datos.setObjectName(u"menuBase_de_Datos")
        self.menuCambiar_a = QMenu(self.menuBase_de_Datos)
        self.menuCambiar_a.setObjectName(u"menuCambiar_a")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuBase_de_Datos.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuFile.addAction(self.actionGuardar_el_estado_de_la_aplicacion)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImportar_datos_desde_CSV)
        self.menuFile.addAction(self.actionExportar_Diario_hacia_CSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCerrar_la_aplicacion)
        self.menuHerramientas.addAction(self.actionA_adir_Compras_2)
        self.menuHerramientas.addAction(self.actionA_adir_Ventas_2)
        self.menuHerramientas.addAction(self.actionModificar_la_inversion)
        self.menuHerramientas.addAction(self.actionCambiar_la_fecha_de_la_sesion)
        self.menuHerramientas.addAction(self.actionUsar_verificacion_de_datos)
        self.menuHerramientas.addSeparator()
        self.menuHerramientas.addAction(self.actionVer_Inventario)
        self.menuHerramientas.addAction(self.actionVer_Ventas)
        self.menuHerramientas.addAction(self.actionVer_Capital)
        self.menuHerramientas.addAction(self.actionVer_Diario)
        self.menuAyuda.addAction(self.actionAyuda_offline)
        self.menuBase_de_Datos.addAction(self.menuCambiar_a.menuAction())
        self.menuBase_de_Datos.addAction(self.actionCrear_nueva)
        self.menuBase_de_Datos.addAction(self.actionSalvar_el_estado_de_la_DB_actual)
        self.menuCambiar_a.addAction(self.action_connect_Celulares)
        self.menuCambiar_a.addAction(self.action_connect_Zapatos)
        self.menuCambiar_a.addAction(self.action_connect_Bisuteria)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyJournal", None))
        self.actionA_adir_Ventas.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Ventas", None))
        self.actionA_adir_Compras.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Compras", None))
        self.actionA_adir_Compras_2.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Compras", None))
#if QT_CONFIG(shortcut)
        self.actionA_adir_Compras_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionA_adir_Ventas_2.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Ventas", None))
#if QT_CONFIG(shortcut)
        self.actionA_adir_Ventas_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionModificar_la_inversion.setText(QCoreApplication.translate("MainWindow", u"Modificar la inversion", None))
#if QT_CONFIG(shortcut)
        self.actionModificar_la_inversion.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionCelulares.setText(QCoreApplication.translate("MainWindow", u"Celulares", None))
        self.actionBistueria.setText(QCoreApplication.translate("MainWindow", u"Bistueria", None))
        self.actionZapatos.setText(QCoreApplication.translate("MainWindow", u"Zapatos", None))
        self.actionCrear_una_nueva_base_de_datos.setText(QCoreApplication.translate("MainWindow", u"Crear una nueva base de datos", None))
        self.actionGuardar_el_estado_de_la_aplicacion.setText(QCoreApplication.translate("MainWindow", u"Guardar el estado de la aplicacion", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar_el_estado_de_la_aplicacion.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar_el_estado_de_la_base_de_datos.setText(QCoreApplication.translate("MainWindow", u"Guardar el estado de la base de datos", None))
        self.actionCrear_nueva.setText(QCoreApplication.translate("MainWindow", u"Crear nueva", None))
#if QT_CONFIG(shortcut)
        self.actionCrear_nueva.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalvar_el_estado_de_la_DB_actual.setText(QCoreApplication.translate("MainWindow", u"Salvar el estado de la DB actual", None))
#if QT_CONFIG(shortcut)
        self.actionSalvar_el_estado_de_la_DB_actual.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_connect_Celulares.setText(QCoreApplication.translate("MainWindow", u"Celulares", None))
#if QT_CONFIG(shortcut)
        self.action_connect_Celulares.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.action_connect_Zapatos.setText(QCoreApplication.translate("MainWindow", u"Zapatos", None))
#if QT_CONFIG(shortcut)
        self.action_connect_Zapatos.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Z", None))
#endif // QT_CONFIG(shortcut)
        self.action_connect_Bisuteria.setText(QCoreApplication.translate("MainWindow", u"Bisuteria", None))
#if QT_CONFIG(shortcut)
        self.action_connect_Bisuteria.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+B", None))
#endif // QT_CONFIG(shortcut)
        self.actionCerrar_la_aplicacion.setText(QCoreApplication.translate("MainWindow", u"Cerrar la aplicacion", None))
#if QT_CONFIG(shortcut)
        self.actionCerrar_la_aplicacion.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionExportar_Diario_hacia_CSV.setText(QCoreApplication.translate("MainWindow", u"Exportar Diario hacia archivo .CSV", None))
#if QT_CONFIG(shortcut)
        self.actionExportar_Diario_hacia_CSV.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionImportar_datos_desde_CSV.setText(QCoreApplication.translate("MainWindow", u"Importar datos desde archivo .CSV", None))
#if QT_CONFIG(shortcut)
        self.actionImportar_datos_desde_CSV.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionCambiar_la_fecha_de_la_sesion.setText(QCoreApplication.translate("MainWindow", u"Cambiar la fecha de la sesion", None))
#if QT_CONFIG(shortcut)
        self.actionCambiar_la_fecha_de_la_sesion.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionAyuda_offline.setText(QCoreApplication.translate("MainWindow", u"Ayuda offline", None))
#if QT_CONFIG(shortcut)
        self.actionAyuda_offline.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionUsar_verificacion_de_datos.setText(QCoreApplication.translate("MainWindow", u"Usar verificacion de datos", None))
#if QT_CONFIG(shortcut)
        self.actionUsar_verificacion_de_datos.setShortcut(QCoreApplication.translate("MainWindow", u"F6", None))
#endif // QT_CONFIG(shortcut)
        self.actionVer_Inventario.setText(QCoreApplication.translate("MainWindow", u"Ver Inventario", None))
        self.actionVer_Ventas.setText(QCoreApplication.translate("MainWindow", u"Ver Ventas", None))
        self.actionVer_Capital.setText(QCoreApplication.translate("MainWindow", u"Ver Capital", None))
        self.actionVer_Diario.setText(QCoreApplication.translate("MainWindow", u"Ver Diario", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Conectado a: ", None))
        self.label_current_database.setText(QCoreApplication.translate("MainWindow", u"{           db}", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sesion:", None))
        self.label_data_session.setText(QCoreApplication.translate("MainWindow", u"{      session}", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Table:", None))
        self.label_table_on_display.setText(QCoreApplication.translate("MainWindow", u"{     table}", None))
        self.toolButton_filter.setText(QCoreApplication.translate("MainWindow", u"Filtrar...", None))
        self.pushButton_export_table.setText(QCoreApplication.translate("MainWindow", u"Exportar tabla", None))
        self.pushButton_print_table.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Reloj", None))
        self.label_app_clock.setText(QCoreApplication.translate("MainWindow", u"{placeholder for clock}", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Datos", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Utilizar esta calculadora la hora de contabilizar sumas mixtas", None))
        self.l005Label_7.setText(QCoreApplication.translate("MainWindow", u"CUC", None))
        self.l005Label_8.setText(QCoreApplication.translate("MainWindow", u"CUP", None))
        self.q005Label_3.setText(QCoreApplication.translate("MainWindow", u"$0.05", None))
        self.q010Label_3.setText(QCoreApplication.translate("MainWindow", u"$0.10", None))
        self.q025Label_3.setText(QCoreApplication.translate("MainWindow", u"$0.25", None))
        self.q050Label_3.setText(QCoreApplication.translate("MainWindow", u"$0.50", None))
        self.q100Label_5.setText(QCoreApplication.translate("MainWindow", u"$1.00", None))
        self.q300Label_5.setText(QCoreApplication.translate("MainWindow", u"$3.00", None))
        self.q500Label_5.setText(QCoreApplication.translate("MainWindow", u"$5.00", None))
        self.q1000Label_5.setText(QCoreApplication.translate("MainWindow", u"$10.00", None))
        self.q2000Label_5.setText(QCoreApplication.translate("MainWindow", u"$20.00", None))
        self.q5000Label_5.setText(QCoreApplication.translate("MainWindow", u"$50.00", None))
        self.q10000Label_5.setText(QCoreApplication.translate("MainWindow", u"$100.00", None))
        self.cuc5centsumlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cuc10centsumlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cuc25centsumlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cuc50centsumlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cuc1sumlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cuc3sumlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cuc5sumlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cuc10sumlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cuc20sumlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cuc50sumlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cuc100sumlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cucTocup5centlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cucTocup10centlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cucTocup25centlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cucTocup50centlabel.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cucTocup1label.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cucTocup3label.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cucTocup5label.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cucTocup10label.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cucTocup20label.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cucTocup50label.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.cucTocup100label.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.p005Label_9.setText(QCoreApplication.translate("MainWindow", u"$1.00", None))
        self.p010Label_7.setText(QCoreApplication.translate("MainWindow", u"$3.00", None))
        self.p025Label_7.setText(QCoreApplication.translate("MainWindow", u"5.00", None))
        self.p050Label_7.setText(QCoreApplication.translate("MainWindow", u"$10.00", None))
        self.p2000Label_9.setText(QCoreApplication.translate("MainWindow", u"$20.00", None))
        self.p5000Label_9.setText(QCoreApplication.translate("MainWindow", u"$50.00", None))
        self.p10000Label_9.setText(QCoreApplication.translate("MainWindow", u"$100.00", None))
        self.p10000Label_11.setText(QCoreApplication.translate("MainWindow", u"$200.00", None))
        self.p10000Label_12.setText(QCoreApplication.translate("MainWindow", u"$500.00", None))
        self.p10000Label_13.setText(QCoreApplication.translate("MainWindow", u"$1000.00", None))
        self.label_cup1.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_cup3.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_cup5.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_cup10.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_cup20.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_cup50.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_cup100.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_cup200.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_cup500.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_cup1000.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Comparacion de Sumas", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Monto Total (CUP):", None))
        self.label_monto_total_calculator.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Dinero a Esperar:", None))
        self.checkBox_use_calculator.setText(QCoreApplication.translate("MainWindow", u"calcular", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Diferencia:", None))
        self.label_sobra_falta_palabra.setText(QCoreApplication.translate("MainWindow", u"Sobran", None))
        self.label_sobra_falta_cantidad.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Monto en CUP", None))
        self.label_montoCUPparcial.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Monto en CUC:", None))
        self.label_montoCUCparcial.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Monto  en CUC convertido :", None))
        self.label_montoCUCconvertido.setText(QCoreApplication.translate("MainWindow", u"$ 0.00", None))
        self.pushButton_reset_calc.setText(QCoreApplication.translate("MainWindow", u"Reset Calculator", None))
        self.label_calc_result.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_calc_operation.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_calc_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_calc_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_calc_store_value.setText(QCoreApplication.translate("MainWindow", u"Store value", None))
        self.pushButton_calc_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_calc_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_calc_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_calc_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_calc_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_calc_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_calc_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_calc_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_calc_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_calc_cents.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.pushButton_calc_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_calc_float.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_calc_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_calc_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_calc_multiply.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_calc_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_calc_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Calculadora de billetes", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.label_plac_total_ventas.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Ganancias", None))
        self.label_plac_total_net_proffit.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Ganancias reales", None))
        self.label_plac_total_real_proffit.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Capital Invertido Total", None))
        self.label_plac_total_capital_low.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Capital de Robert", None))
        self.label_plac_total_rob_capital.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Capital de Ariadna", None))
        self.label_plac_total_ary_capital.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Resumen de las estadisticas del dia", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.label_plac_day_ventas.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Retorno de la inversion", None))
        self.label_plac_day_inversion.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Ganancias netas", None))
        self.label_plac_day_net_proffit.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Salario", None))
        self.label_plac_day_salary.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Renta", None))
        self.label_plac_day_rent.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Ganancias totales", None))
        self.label_plac_day_real_proffit.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Ganancias de la parte", None))
        self.label_plac_day_part_proffit.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Compras del dia", None))
        self.label_plac_day_compras.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Pagos a Consignacion del dia", None))
        self.label_plac_day_consignation.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.pushButton_update_stats_tab.setText(QCoreApplication.translate("MainWindow", u"Actualizar estadisticas", None))
        self.dateEdit_intervalo_start.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.dateEdit_intervalo_stop.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Resumen de las estadisticas totales", None))
        self.checkBox_ver_solo_intervalo.setText(QCoreApplication.translate("MainWindow", u"Ver solamente en el intervalo:", None))
        self.pushButton_generar_tabla_totales.setText(QCoreApplication.translate("MainWindow", u"Generar tabla con todos los totales", None))
        self.pushButton_generate_table_all_days.setText(QCoreApplication.translate("MainWindow", u"Generar tabla con todos los diarios", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Ver los datos en el ambito: ", None))
        self.comboBox_ambito_de_tabla.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.comboBox_ambito_de_tabla.setItemText(1, QCoreApplication.translate("MainWindow", u"Diario", None))
        self.comboBox_ambito_de_tabla.setItemText(2, QCoreApplication.translate("MainWindow", u"Semanal", None))
        self.comboBox_ambito_de_tabla.setItemText(3, QCoreApplication.translate("MainWindow", u"Mensual", None))
        self.comboBox_ambito_de_tabla.setItemText(4, QCoreApplication.translate("MainWindow", u"Anual", None))

        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Capital total en el negocio", None))
        self.label_plac_capital_total.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"De ello esta invertido", None))
        self.label_plac_capital_invertido.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"En efectivo queda", None))
        self.label_plac_cash_en_caja.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Flujo del efectivo en la caja", None))
        self.pushButton_export_stats_tab.setText(QCoreApplication.translate("MainWindow", u"Exportar Pagina", None))
        self.pushButton_print_stats_tab.setText(QCoreApplication.translate("MainWindow", u"Imprimir esta Vista", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Estadisticas", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuHerramientas.setTitle(QCoreApplication.translate("MainWindow", u"Herramientas", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.menuBase_de_Datos.setTitle(QCoreApplication.translate("MainWindow", u"Base de Datos", None))
        self.menuCambiar_a.setTitle(QCoreApplication.translate("MainWindow", u"Cambiar a: ", None))
    # retranslateUi

