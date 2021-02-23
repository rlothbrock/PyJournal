from packages.components.printing_service import data_printer


def print_active_table_routine(self):
    data_printer(self, self.ui.tableWidget_table_display)
    return
