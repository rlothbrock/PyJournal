from PySide2.QtWidgets import QDialog, QDialogButtonBox

from packages.UI.exc_rate_dialog import Ui_Dialog as Ui_ExcRateDialog


def fix_exc_rate_routine(self):
    rate_dialog = RateDialog(self)
    rate_dialog.exec_()
    return


class RateDialog(QDialog):
    def __init__(self, parent):
        super(RateDialog, self).__init__(parent)
        self.ui = Ui_ExcRateDialog()
        self.ui.setupUi(self)

        self.ui.doubleSpinBox.setFocus()
        self.applyButton = self.ui.buttonBox.button(QDialogButtonBox.Apply)
        self.discardButton = self.ui.buttonBox.button(QDialogButtonBox.Discard)

        self.init_ui(parent)

    def init_ui(self, parent):
        self.discardButton.clicked.connect(self.reject)
        self.applyButton.clicked.connect(lambda: self.on_apply(parent))

    def on_apply(self, parent):
        rate_value = self.ui.doubleSpinBox.value()
        parent.status.update({'exc_rate': rate_value})
        parent.ui.doubleSpinBox_tasa_de_cambio_USD.setValue(rate_value)
        self.accept()


