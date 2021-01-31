from random import random

from PySide2.QtWidgets import QDialog, QDialogButtonBox

from UI.help_offline import Ui_Dialog as Ui_help_dialog
from UI.sales_form import Ui_Dialog_sales_form

from dialogs.auxiliar_dialogs import MessageBox, selfCloseInterface
from modules.crud_sqlite import crud_driver
from modules.db_templates_manager import get_template_fields, get_index_in_template


# common resources-------------------

def tool_launcher(self, tool):
    dialog = tool(self)
    self.ui.tabWidget.setCurrentIndex(0)
    ph = self.geometry().height()
    pw = self.geometry().width()
    px = self.geometry().x()
    py = self.geometry().y()
    dw = dialog.width()
    dh = dialog.height()
    dialog.setGeometry(pw - dw + px, ph - dh + py, dw, dh)
    dialog.show()


def build_item_code(price):
    return 'p{:X}-{}'.format(int(random()*10**18),price)


def build_data_template():
    return [0, 0, 0, 0, 0, 0, 0, '', 0, 0, '', '', 0, 0, '', 0, 0, 0, 0, 0, '']


def buddy_sync(master, slave, dependant= None, value=0, is_text=False,trigger=True ):
    idx = master.currentIndex()
    if slave is not None:
        slave.setCurrentIndex(idx)
    if dependant is not None and trigger:
        if is_text:
            dependant.setText(value)
        if not is_text:
            dependant.setValue(value)

# purchases form ---------------------------------




# todo not touched  must enhance---
class SalesFormDialog(QDialog):
    def __init__(self, parent):
        super(SalesFormDialog, self).__init__(parent)
        self.ui = Ui_Dialog_sales_form()
        self.ui.setupUi(self)


class HelpOfflineDialog(QDialog):
    def __init__(self, parent):
        super(HelpOfflineDialog, self).__init__(parent)
        self.ui = Ui_help_dialog()
        self.ui.setupUi(self)
