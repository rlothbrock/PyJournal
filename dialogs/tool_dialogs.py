from random import random

from PySide2.QtWidgets import QDialog, QDialogButtonBox

from UI.help_offline import Ui_Dialog as Ui_help_dialog

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


# todo
#  so far the rent is fixed (125). in future versions must be posssible to dinamically
#  adjust the rent through a dialog on the app level.

def build_salary(parent,sale,price):
    sale,proffit = float(sale), float(sale)-float(price)

    bases = {
        'cellsDB.db': proffit,
        'bisutDB.db': sale,
        'shoesDBdb': 1
    }
    salaries = {
        'cellsDB.db': lambda prof_: 10 / 100 * prof_,
        'bisutDB.db': lambda sale_: 6 / 100 * sale_,
        'shoesDBdb': lambda _: 25
    }
    return salaries.get(parent.status.get('connected_to'))(
        bases.get(parent.status.get('connected_to'))
    )

    # todo:
    #   on next versions must implement a proper way to define the salary rate
    #   on the main app (through an action on menus ) based on that rate salary must
    #   be calculated. so far it will be declared here (fixed) and there's no way
    #   to change it.


def build_item_code(price, consignation):
    consignation__ = 'c' if consignation else 'p'
    return '{}{:X}-{}'.format(consignation__, int(random() * 10 ** 18), price)


def build_data_template():
    return [0, 0, 0, 0, 0, 0, 0, '', 0, 0, '', '', 0, 0, '', 0, 0, 0, 0, 0, '']


def buddy_sync(master, slave, dependant=None, value=0, is_text=False, trigger=True):
    idx = master.currentIndex()
    if slave is not None:
        slave.setCurrentIndex(idx)
    if dependant is not None and trigger:
        if is_text:
            dependant.setText(value)
        if not is_text:
            dependant.setValue(value)


# ---
class HelpOfflineDialog(QDialog):
    def __init__(self, parent):
        super(HelpOfflineDialog, self).__init__(parent)
        self.ui = Ui_help_dialog()
        self.ui.setupUi(self)
