from packages.components.active_table_filter import filter_active_table
from packages.components.app_counter import update_counter
from packages.components.data_display_tab import display_active_table_on_data_display
from packages.components.menus import set_menus
from packages.components.statistics_display_tab import display_statistics_on_tab
from packages.components.status import current_date
from packages.dialogs.auxiliar_dialogs import selfCloseInterface
from packages.modules.accountant import calculate_auxiliar_tabs
from packages.modules.app_clock import app_clock
from packages.modules.calculator import set_calculator
from packages.modules.crud_sqlite import crud_driver
from packages.modules.data_import_export import export_data_displayed_on_tab1
from packages.modules.money_calc import set_bill_calculator
from packages.routines.status_loader import status_loader_routine
from packages.routines.status_saver import status_saver_routine


def ui_init_routine(self):
    self.status = status_loader_routine(self)
    status_saver_routine(self,True)
    if self.status.get('last_date') == current_date:
        self.counter = self.status.get('counter')
    self.status.update({'last_date': current_date})
    # self.data_to_display_on_tab1 = crud_driver(  # on init shows diary on current_date entries
    #     self, 'diary', 'raw_exec', {
    #         'raw_exec': 'SELECT * FROM diary WHERE entry_counter REGEXP ?',
    #         'value': ('{}'.format(current_date).replace('-',''),)
    #     })
    self.data_to_display_on_tab1 = crud_driver(self, 'diary', 'read', {
             'pick_all': False,
             'multi': False,
             'pick_cols': ['*'],
             'field': 'entry_counter',
             'operator': 'REGEXP',
             'order_by': ['entry_counter'],
             'order_': ['ASC', 'ASC'],
             'sort': True,
             'value': ('{}'.format(current_date).replace('-',''),)
    })
    set_menus(self)
    app_clock(self, self.ui.label_app_clock)
    set_calculator(self)
    set_bill_calculator(self)

    # ui initialization
    self.ui.tabWidget.setCurrentIndex(self.status.get('active_tab'))
    self.ui.label_data_session.setText(self.date_session)
    self.ui.label_table_on_display.setText(self.table_on_target)
    self.ui.label_current_database.setText(self.status.get('connected_to'))

    #  signal connections
    self.date_changed_signal.connect(self.change_date_session)
    self.connected_signal.connect(lambda db__: self.ui.label_current_database.setText(db__))
    self.resized_signal.connect(self.save_window_size)
    self.counter_updated_signal.connect(lambda: update_counter(self))
    self.display_table_signal.connect(lambda: display_active_table_on_data_display(self))
    if self.ui.tabWidget.currentIndex() == 0:
        self.display_table_signal.emit()
    self.recalculate_tables_signal.connect(lambda: calculate_auxiliar_tabs(self))
    self.recalculate_tables_signal.connect(lambda: display_statistics_on_tab(self))
    if self.ui.tabWidget.currentIndex() == 2:
        self.recalculate_tables_signal.emit()
    self.ui.tabWidget.currentChanged.connect(lambda i: tab_index_reaction(self, i))

    # tab1 buttons
    self.ui.pushButton_export_table.clicked.connect(lambda: export_data_displayed_on_tab1(self))
    self.ui.toolButton_filter.clicked.connect(lambda: filter_active_table(self))

    # statistics tab buttons
    self.ui.pushButton_update_stats_tab.clicked.connect(lambda: display_statistics_on_tab(self))
    self.ui.pushButton_update_stats_tab.clicked.connect(lambda: selfCloseInterface('Estadisticas Actualizadas',alert_level=1,title='Completado!'))


def tab_index_reaction(self, index: int):
    if index == 2:
        self.recalculate_tables_signal.emit()
