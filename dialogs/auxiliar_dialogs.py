from PySide2.QtCore import QTimer, SLOT
from PySide2.QtWidgets import QMessageBox


class SelfCloseMsgBox(QMessageBox):
    def __init__(
            self,
            message: str,
            alert_level: int = 1,  # [0,1,2,3]
            title: str = 'Alert',
            info: str = ''
    ):
        super(SelfCloseMsgBox, self).__init__()
        self.levels = [
            QMessageBox.Question,
            QMessageBox.Information,
            QMessageBox.Warning,
            QMessageBox.Critical
        ]
        self.setText(message)
        self.setIcon(self.levels[alert_level])
        self.setWindowTitle(title)
        self.setInformativeText(info)


def selfCloseInterface(
        message: str,
        time_to_close: int = 2,
        alert_level: int = 1,  # [0,1,2,3]
        title: str = 'Alert',
        info: str = ''
):
    alert = SelfCloseMsgBox(message, alert_level, title, info)
    QTimer.singleShot(time_to_close*1000, alert, SLOT('accept()'))
    return alert.exec_()


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
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.buttonClicked.connect(lambda button: dialog_slot_driver(self, button, slot_yes, slot_no))


def dialog_slot_driver(self, button, slot_yes, slot_no):
    if button.text() == '&Yes':
        return slot_yes()
    if button.text() == '&No':
        if slot_no is None:
            self.close()
            return
        return slot_no()

# unused class (so far)
# class NewDBAlert(QDialog):
#     def __init__(self, slot):
#         super(NewDBAlert, self).__init__()
#         self.ui = Ui_new_db_alert()
#         self.ui.setupUi()
#         # error here  fix error here
#         self.ui.buttonBox.button(QDialog.AcceptRole).clicked.connect(
#             lambda: slot(self.valid_text())
#         )
#
#     def valid_text(self):
#         if self.ui.lineEdit.text() is None:
#             raise TypeError('db name can not be Empty')
#         if not all[
#             len(self.ui.lineEdit.text().splitlines()) == 1,
#             len(self.ui.lineEdit.text().split(' ')) == 1,
#             all('A' <= x <= 'z' for x in self.ui.lineEdit.text())
#         ]:
#             raise ValueError('use only alphabetic characters for database name')
#         return self.ui.lineEdit.text()
