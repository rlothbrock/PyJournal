import datetime

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QDialog, QDialogButtonBox
from packages.UI.old_session_dialog import Ui_Dialog


class DateManager(QDialog):

    def __init__(self, target):
        super(DateManager, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.Reject_Btn = self.ui.buttonBox.button(QDialogButtonBox.Cancel)
        self.Accept_Btn = self.ui.buttonBox.button(QDialogButtonBox.Ok)

        self.Reject_Btn.clicked.connect(lambda: self.reject)
        self.Accept_Btn.clicked.connect(lambda: self.accept_(target))

        self.ui.dateEditSession.dateChanged.connect(lambda: self.Accept_Btn.setDisabled(self.ui.dateEditSession.date() > datetime.datetime.now()))

    @Slot()
    def accept_(self, target):
        target.date_changed_signal.emit('%04d-%02d-%02d' % self.ui.dateEditSession.date().getDate())
        target.recalculate_tables_signal.emit()
        self.accept()

def manage_date_session(session):
    datePicker = DateManager(session)
    datePicker.show()
