#!/usr/bin/python3.8

import datetime
import os
import sys

import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMainWindow, QApplication

from UI.Main import Ui_MainWindow
from dialogs.tool_dialogs import PurchasesFormDialog, tool_launcher, HelpOfflineDialog, CapitalFormDialog, \
    SalesFormDialog
from modules.calculator import set_calculator
from modules.data_import_export import  import_data_to_diary, export_data_from_diary
from modules.money_calc import set_bill_calculator


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.status = {}
        # status props---------
        self.current_connection = None
        self.cursor = None
        self.date_session = datetime.datetime.now().__str__().split(' ')[0] # yyyy-mm-dd
        self.operation = ''  # used for calculator to work
        self.table_for_filter_dialogs: str = None
        self.filter_dialog_options: dict = {}
        self.table_on_target = 'Empty So Far...'

        self.diary_list = []
        self.data_to_display_on_tab1 = []  # this prop is extremely important, it holds the data to be displayed,
        # when action is triggered
        self.data_to_export = []           # this prop is extremely important, it holds the data to be exported
        self.imported_data = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #        Actions on menus
        self.ui.actionA_adir_Compras_2.triggered.connect(lambda: tool_launcher(self, PurchasesFormDialog))
        self.ui.actionA_adir_Ventas_2.triggered.connect(lambda: tool_launcher(self, SalesFormDialog))
        self.ui.actionModificar_la_inversion.triggered.connect(lambda: tool_launcher(self, CapitalFormDialog))
        self.ui.actionAyuda_offline.triggered.connect(lambda: tool_launcher(self, HelpOfflineDialog))

        # Action imports
        # todo add the source to export or target to import
        self.ui.actionImportar_datos_desde_CSV.triggered.connect(lambda: import_data_to_diary(self)) # missing target
        # Action exports
        self.ui.actionExportar_Diario_hacia_CSV.triggered.connect(lambda: export_data_from_diary(self)) # missing target
        # todo move this block to file apart

        # calculator tab
        set_bill_calculator(self)
        set_calculator(self)

    def keyPressEvent(self, event: PySide2.QtGui.QKeyEvent):
        super(MainWindow, self).keyPressEvent(event)
        self.key_pressed_signal.emit(event.key())

    connected_signal = Signal(str)
    active_tab_signal = Signal(int)
    table_on_edition_signal = Signal(str)
    resized_signal = Signal()
    value_changed_signal = Signal()
    sell_price_changed_signal = Signal(float)
    key_pressed_signal = Signal(int)
    date_changed_signal = Signal(str)

if __name__ == "__main__":
    try:
        db_dir = os.path.join(os.getcwd(), 'databases')
        os.mkdir(db_dir)
    except FileExistsError as error:
        print('info on main: {}'.format(error))

    app = QApplication(sys.argv)
    window = MainWindow()
    # todo imlement this:
    #  app.aboutToQuit.connect(about_to_quit_protocol)
    #  w, h = window.get_status().get('width'), window.get_status().get('height')
    #  window.resize(w, h)
    window.show()
    sys.exit(app.exec_())
