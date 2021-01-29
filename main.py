#!/usr/bin/python3.8

import datetime
import os
import sys

import PySide2
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QMainWindow, QApplication

from UI.Main import Ui_MainWindow
from components.status import current_date
from dialogs.auxiliar_dialogs import selfCloseInterface
from routines.about_to_Quit import about_to_quit_routine
from routines.ui_initialization import ui_init_routine


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.status = {}
        # status props---------
        self.connection = None
        self.cursor = None
        self.date_session = current_date # yyyy-mm-dd
        self.operation = ''  # used for calculator to work
        self.table_for_filter_dialogs: str = None
        self.filter_dialog_options: dict = {}
        self.table_on_target = 'diary'
        self.use_secure_entry = True
        # this props will be initialized on init_ui. are used for keep track of counter
        self.counter = 0
        self.last_date = ''
        self.data_to_display_on_tab1 = [] # todo: this props holds the data to show on table
                                          #  and need a signal for detect changes and react properly
                                          #  is readen any time we display data and must be proper updated
        self.data_to_export = [] # todo : used most on buttons export appwide
                                 #  this prop is used for holding data just
                                 #  in case that prop <source> on export() is empty
                                 #  can remain [] if source is provided
        self.imported_data = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ui_init_routine(self)

    def keyPressEvent(self, event: PySide2.QtGui.QKeyEvent):
        super(MainWindow, self).keyPressEvent(event)
        self.key_pressed_signal.emit(event.key())

    def resizeEvent(self, event: PySide2.QtGui.QResizeEvent):
        # debug: print('resized event launched')
        self.resized_signal.emit()
        return super(MainWindow, self).resizeEvent(event)

    def change_date_session(self, new_value):
        self.date_session = new_value
        self.ui.label_data_session.setText(new_value)
        nd = 'Nueva Fecha: {}'.format(new_value)
        print(nd)
        selfCloseInterface(
            nd, 3, 1, 'Fecha de trabajo cambiada','\n\n *Las entradas tendran esa fecha')
        return


    @Slot()
    def save_window_size(self):
        self.status.update({'width': self.width(), 'height': self.height()})

    connected_signal = Signal(str)
    active_tab_signal = Signal(int)
    display_table_signal = Signal()
    resized_signal = Signal()
    value_changed_signal = Signal()
    sell_price_changed_signal = Signal(float)
    key_pressed_signal = Signal(int)
    date_changed_signal = Signal(str)
    counter_updated_signal = Signal()
    recalculate_tables_signal = Signal()

if __name__ == "__main__":
    try:
        db_dir = os.path.join(os.getcwd(), 'databases')
        os.mkdir(db_dir)
    except FileExistsError as error:
        print('info on main: {}'.format(error))

    app = QApplication(sys.argv)
    window = MainWindow()
    w, h = window.status.get('width'), window.status.get('height')
    window.resize(w, h)
    window.show()
    app.aboutToQuit.connect(about_to_quit_routine)
    sys.exit(app.exec_())
