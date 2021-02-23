from PySide2.QtGui import Qt

from packages.components.active_table_filter import filter_active_table
from packages.components.app_counter import update_counter
from packages.components.data_display_tab import display_active_table_on_data_display
from packages.components.menus import set_menus
from packages.components.statistics_display_tab import display_statistics_on_tab, export_statistics_page
from packages.components.status import current_date
from packages.dialogs.auxiliar_dialogs import selfCloseInterface
from packages.modules.accountant import calculate_auxiliar_tabs
from packages.modules.app_clock import app_clock
from packages.modules.calculator import set_calculator_ui
from packages.modules.crud_sqlite import crud_driver
from packages.modules.data_import_export import export_data_displayed_on_tab1
from packages.modules.money_calc import set_bill_calculator
from packages.routines.generate_tables_on_stats import generate_table_all_days_routine, generate_table_totales
from packages.routines.print_active_table import print_active_table_routine
from packages.routines.print_stats_table import print_stats_table_routine
from packages.routines.set_progressBar import set_progress_bar
from packages.routines.status_loader import status_loader_routine
from packages.routines.status_saver import status_saver_routine


def ui_init_routine(self):
    self.status = status_loader_routine(self)
    status_saver_routine(self, True)
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
        'value': ('{}'.format(current_date).replace('-', ''),)
    })
    set_menus(self)
    app_clock(self, self.ui.label_app_clock)
    set_calculator_ui(self)
    set_bill_calculator(self)
    set_progress_bar(self)

    # ui initialization
    self.ui.tabWidget.setCurrentIndex(self.status.get('active_tab'))
    self.ui.label_data_session.setText(self.date_session)
    self.ui.label_table_on_display.setText(self.table_on_target)
    self.ui.label_current_database.setText(self.status.get('connected_to'))
    # disabling intervals date edits on statistics tab
    self.ui.dateEdit_intervalo_start.setEnabled(False)
    self.ui.dateEdit_intervalo_stop.setEnabled(False)

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
    self.ui.pushButton_print_table.clicked.connect(lambda: print_active_table_routine(self))

    # statistics tab buttons
    self.ui.pushButton_update_stats_tab.clicked.connect(lambda: display_statistics_on_tab(self))
    self.ui.pushButton_update_stats_tab.clicked.connect(
        lambda: selfCloseInterface('Estadisticas Actualizadas', alert_level=1, title='Completado!'))
    self.ui.pushButton_print_stats_tab.clicked.connect(lambda: print_stats_table_routine(self))
    self.ui.pushButton_export_stats_tab.clicked.connect(lambda: export_statistics_page(self))
    self.ui.checkBox_ver_solo_intervalo.stateChanged.connect(lambda: set_conditional_enabled(self))
    self.ui.pushButton_generate_table_all_days.clicked.connect(lambda: generate_table_all_days_routine(self))
    self.ui.pushButton_generar_tabla_totales.clicked.connect(lambda: generate_table_totales(self))

def set_conditional_enabled(self):
    state = self.ui.checkBox_ver_solo_intervalo.checkState() == Qt.Checked
    self.ui.dateEdit_intervalo_start.setEnabled(state)
    self.ui.dateEdit_intervalo_stop.setEnabled(state)


def tab_index_reaction(self, index: int):
    if index == 2:
        self.recalculate_tables_signal.emit()
