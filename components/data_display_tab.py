# this components holds logic for the data displaying on tab 1
from PySide2.QtGui import QColor, QFont
from PySide2.QtWidgets import QTableWidgetItem

from modules.crud_sqlite import crud_driver
from modules.db_templates_manager import get_template_fields


def execute_display_table(self, table_name):
    self.table_on_target = table_name
    if table_name != 'diary':
        self.recalculate_tables_signal.emit()
        # what else??
    self.data_to_display_on_tab1 = crud_driver(self, table_name, 'read', {'pick_all': True})
    self.display_table_signal.emit()
    self.ui.tabWidget.setCurrentIndex(0)
    return


# this function must be triggered by a signal and self.table_on_target must be changed previously
def display_active_table_on_data_display(self):
    # class props needed
    data_to_display = self.data_to_display_on_tab1.copy()
    table_name = self.table_on_target
    # print('debug: \ndata_to_display on {}:\n{}'.format(table_name,data_to_display))
    self.ui.label_table_on_display.setText(table_name)
    # headers
    fields = get_template_fields(table_name)
    self.ui.tableWidget_table_display.setColumnCount(len(fields))
    header_widgets_list = list((QTableWidgetItem() for n in fields))

    for index, field in enumerate(fields):
        header_widgets_list[index].setText(field)
        self.ui.tableWidget_table_display.setHorizontalHeaderItem(index, header_widgets_list[index])

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
                    item__.setTextColor(QColor(255,255,255))
                    item__.setFont(QFont(weight=5))
            except:
                pass
            finally:
                self.ui.tableWidget_table_display.setItem(i_row, i_col, item__)
    # print('debug: table {} displayed...'.format(table_name))
    return

