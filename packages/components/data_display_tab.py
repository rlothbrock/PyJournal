# this components holds logic for the data displaying on tab 1
from PySide2.QtGui import QColor, QFont
from PySide2.QtWidgets import QTableWidgetItem

from packages.dialogs.auxiliar_dialogs import selfCloseInterface
from packages.modules.crud_sqlite import crud_driver
from packages.modules.db_templates_manager import get_template_fields, get_format_of_field


def execute_display_table(self, table_name):
    self.table_on_target = table_name
    self.headers_for_tab1 = get_template_fields(table_name)
    if table_name != 'diary':
        self.recalculate_tables_signal.emit()
        # what else??
    self.data_to_display_on_tab1 = crud_driver(self, table_name, 'read', {'pick_all': True})
    self.display_table_signal.emit()
    self.ui.tabWidget.setCurrentIndex(0)
    selfCloseInterface(
        'tabla: {} ha sido cargada con exito'.format(table_name), 1, 1,
        'Ver {}'.format(table_name)
    )
    return


# this function must be triggered by a signal and self.table_on_target must be changed previously
def display_active_table_on_data_display(self):
    # class props needed
    data_to_display = self.data_to_display_on_tab1.copy()
    table_name = self.table_on_target
    self.ui.label_table_on_display.setText(table_name)
    # headers
    fields = self.headers_for_tab1
    self.ui.tableWidget_table_display.setColumnCount(len(fields))
    tableHeadersWidgets_list = list((QTableWidgetItem() for n in fields))

    for index, field in enumerate(fields):
        tableHeadersWidgets_list[index].setText(field)
        self.ui.tableWidget_table_display.setHorizontalHeaderItem(index, tableHeadersWidgets_list[index])

    # table build process
    self.ui.tableWidget_table_display.setRowCount(0)
    for i_row, row in enumerate(data_to_display):
        self.ui.tableWidget_table_display.insertRow(i_row)
        for i_col, item_data in enumerate(row):
            item__ = QTableWidgetItem(str(item_data))
            if i_row % 2 == 0:
                item__.setBackgroundColor(QColor(220, 230, 255))
            try:
                negative_value = item_data < 0
                if negative_value:
                    item__.setBackgroundColor(QColor(120, 0, 0))
                    item__.setTextColor(QColor(255, 255, 255))
                    item__.setFont(QFont(weight=5))
            except:
                pass
            finally:
                item__.setText(
                    get_format_of_field(
                        table_name,
                        self.ui.tableWidget_table_display.horizontalHeaderItem(i_col).text()
                    )(item_data)
                )
                self.ui.tableWidget_table_display.setItem(i_row, i_col, item__)
    # print('debug: table {} displayed...'.format(table_name))
    return
