from PySide2.QtWidgets import QDialog, QTableWidgetItem

from packages.UI.stats_dialog import Ui_Dialog as Ui_StatsDialog


class ExternalStatsDialog(QDialog):
    def __init__(self, parent, h_head: list, v_head: list, data: list, data_name: str, scope: str):
        super(ExternalStatsDialog, self).__init__(parent)
        self.ui = Ui_StatsDialog()
        self.ui.setupUi(self)

        # rename widgets on class for easy management
        self.exportButton = self.ui.pushButtonexport_dialog_stats_table
        self.printButton = self.ui.pushButtonprint_dialog_stats_table
        self.filterButton = self.ui.pushButtonfilter_dialog_stats_table
        self.dataDisplay = self.ui.tableWidget_dialog_stats
        self.init_ui(h_head, v_head, data, data_name, scope)

    def init_ui(self, h_head, v_head, data, data_name, scope):
        self.exportButton.clicked.connect(lambda: True)
        self.printButton.clicked.connect(lambda: True)
        self.filterButton.clicked.connect(lambda: True)
        self.display_data(h_head, v_head, data, data_name, scope)

    def display_data(self, h_head, v_head, data, data_name, scope, ):
        dialog_name = 'Tabla de {} Resumida en Ambito: "{}"'.format(data_name, scope)
        self.setWindowTitle(dialog_name)

        self.dataDisplay.setColumnCount(len(h_head))
        self.dataDisplay.setRowCount(len(v_head))

        horizontalTableHeaders = list(map(
            setTextOnItem,
            (QTableWidgetItem() for h in h_head),
            h_head
        ))

        for h_idx, h_h_item in enumerate(horizontalTableHeaders):
            self.dataDisplay.setHorizontalHeaderItem(h_idx, h_h_item)

        verticalTableHeaders = list(map(
            setTextOnItem,
            (QTableWidgetItem() for v in v_head),
            v_head
        ))

        for v_idx, v_h_item in enumerate(verticalTableHeaders):
            self.dataDisplay.setVerticalHeaderItem(v_idx, v_h_item)

        for row_index, row in enumerate(data):
            for col_index, col in enumerate(row):
                item_index = col_index, row_index
                item__ = QTableWidgetItem()
                content = ('$ {:,.2f}'.format(col) if isinstance(col,float) else str(col)) if col else '0'
                item__.setText(content)
                self.dataDisplay.setItem(*item_index, item__)


def setTextOnItem(item, text):
    item.setText(text)
    return item
