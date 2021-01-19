from PySide2.QtWidgets import QDialog, QDialogButtonBox

from UI.capital_form import Ui_DialogCapital
from UI.help_offline import Ui_Dialog as Ui_help_dialog
from UI.purchases_form import Ui_Dialog_purchases_form
from UI.sales_form import Ui_Dialog_sales_form


# this functions launches the dialog as a modal window
def tool_launcher(self, tool):
    dialog = tool(self)
    # debug print('launching tool as: {}'.format(tool))
    # relocating dialoq on parent bottom right border
    self.ui.tabWidget.setCurrentIndex(0)
    ph = self.geometry().height()
    pw = self.geometry().width()
    px = self.geometry().x()
    py = self.geometry().y()
    dw = dialog.width()
    dh = dialog.height()
    # debug print('x: {},y: {}, width: {}, height: {}'.format(pw-dw, ph-dh, dw,dh))
    dialog.setGeometry(pw-dw+px, ph-dh+py, dw, dh)
    dialog.show()





class SalesFormDialog(QDialog):
    def __init__(self,parent):
        super(SalesFormDialog, self).__init__(parent)
        self.ui = Ui_Dialog_sales_form()
        self.ui.setupUi(self)


class PurchasesFormDialog(QDialog):
    def __init__(self, parent):
        super(PurchasesFormDialog,self).__init__(parent)
        self.ui = Ui_Dialog_purchases_form()
        self.ui.setupUi(self)

        # buttons
        self.closeButton = self.ui.buttonBox.button(QDialogButtonBox.Close)
        self.applyButton = self.ui.buttonBox.button(QDialogButtonBox.Apply)
        self.resetButton = self.ui.buttonBox.button(QDialogButtonBox.Reset)

        # behavior of buttons
        self.applyButton.clicked.connect(self.accept_rutine)
        self.closeButton.clicked.connect(self.reject_rutine)

    def accept_rutine(self):
        #  self. accept() : its not triggered since apply allows can be clicked many times
        print('applied')
        return

    def reject_rutine(self):
        self.reject()

class CapitalFormDialog(QDialog):
    def __init__(self, parent):
        super(CapitalFormDialog, self).__init__(parent)
        self.ui = Ui_DialogCapital()
        self.ui.setupUi(self)


class HelpOfflineDialog(QDialog):
    def __init__(self, parent):
        super(HelpOfflineDialog, self).__init__(parent)
        self.ui = Ui_help_dialog()
        self.ui.setupUi(self)


