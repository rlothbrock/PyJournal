#!/usr/bin/python3.8

import datetime
import os
import sys

import PySide2
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QMainWindow, QApplication

from UI.Main import Ui_MainWindow
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
        self.date_session = datetime.datetime.now().__str__().split(' ')[0] # yyyy-mm-dd
        self.operation = ''  # used for calculator to work
        self.table_for_filter_dialogs: str = None
        self.filter_dialog_options: dict = {}
        self.table_on_target = 'diary'
        self.use_secure_entry = True

        self.diary_list = []
        self.data_to_display_on_tab1 = []  # this prop is extremely important, it holds the data to be displayed,
        # when action is triggered
        self.data_to_export = []           # this prop is extremely important, it holds the data to be exported
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
    w, h = window.status.get('width'), window.status.get('height')
    window.resize(w, h)
    window.show()
    app.aboutToQuit.connect(about_to_quit_routine)
    sys.exit(app.exec_())
