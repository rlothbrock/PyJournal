from PySide2.QtWidgets import QMessageBox, QDialog

from UI.new_db_alert import Ui_Dialog as Ui_new_db_alert


class MessageBox(QMessageBox):
    def __init__(self, slot_yes, text, icon='q', title='Alert', info=None, slot_no=None):
        super(MessageBox, self).__init__()
        self.setText(text)
        _icon = None
        if icon == 'q':
            _icon = QMessageBox.Question
        if icon == 'i':
            _icon = QMessageBox.Information
        if icon == 'w':
            _icon = QMessageBox.Warning
        if icon == 'e':
            _icon = QMessageBox.Critical
        if info is not None:
            self.setInformativeText(info)
        self.setWindowTitle(title)
        self.setIcon(_icon)
        self.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        self.buttonClicked.connect(lambda button: dialog_slot_driver(self, button, slot_yes, slot_no))


def dialog_slot_driver(self, button, slot_yes, slot_no):
    if button.text() == '&Yes':
        return slot_yes()
    if button.text() == '&No':
        if slot_no is None:
            self.close()
            return
        return slot_no()


class NewDBAlert(QDialog):
    def __init__(self, slot):
        super(NewDBAlert, self).__init__()
        self.ui = Ui_new_db_alert()
        self.ui.setupUi()
        # error here todo fix error here
        self.ui.buttonBox.button(QDialog.AcceptRole).clicked.connect(
            lambda: slot(self.valid_text())
        )

    def valid_text(self):
        if self.ui.lineEdit.text() is None:
            raise TypeError('db name can not be Empty')
        if not all[
            len(self.ui.lineEdit.text().splitlines()) == 1,
            len(self.ui.lineEdit.text().split(' ')) == 1,
            all('A' <= x <= 'z' for x in self.ui.lineEdit.text())
        ]:
            raise ValueError('use only alphabetic characters for database name')
        return self.ui.lineEdit.text()


def on_accept():
    print('aa')


