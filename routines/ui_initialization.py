from components.app_counter import update_counter
from components.menus import set_menus
from components.status import current_date
from modules.app_clock import app_clock
from modules.calculator import set_calculator
from modules.money_calc import set_bill_calculator
from routines.status_loader import status_loader_routine


def ui_init_routine(self):
    self.status = status_loader_routine(self)
    if self.status.get('last_date') == current_date:
        self.counter = self.status.get('counter')
    self.status.update({'last_date': current_date})
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
    print('debug: finish ui_init')
