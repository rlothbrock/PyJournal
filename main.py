#!/usr/bin/python3.8

import datetime
import os
import sys

import PySide2
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QMainWindow, QApplication

from UI.Main import Ui_MainWindow
from components.menus import set_menus
from modules.app_clock import app_clock
from modules.calculator import set_calculator
from modules.money_calc import set_bill_calculator
from routines.about_to_Quit import about_to_quit_routine
from routines.status_loader import status_loader_routine


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
        self.ui_init()

    def ui_init(self):
        self.status = status_loader_routine(self)
        set_menus(self)
        app_clock(self, self.ui.label_app_clock)
        set_calculator(self)
        set_bill_calculator(self)

        self.ui.tabWidget.setCurrentIndex(self.status.get('active_tab'))
        self.ui.label_data_session.setText(self.date_session)
        self.ui.label_table_on_display.setText(self.table_on_target)
        self.ui.label_current_database.setText(self.status.get('connected_to'))
        self.date_changed_signal.connect(self.change_date_session)


    def keyPressEvent(self, event: PySide2.QtGui.QKeyEvent):
        super(MainWindow, self).keyPressEvent(event)
        self.key_pressed_signal.emit(event.key())

    @Slot()
    def change_date_session(self, new_value):
        self.date_session = new_value
        self.ui.label_data_session.setText(new_value)
        print('current session settled to: {}'.format(new_value))

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
    w, h = window.status.get('width'), window.status.get('height')
    window.resize(w, h)
    window.show()
    app.aboutToQuit.connect(about_to_quit_routine)
    sys.exit(app.exec_())
