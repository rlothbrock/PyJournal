# store here the class for saving filter dialog
import os

from PySide2.QtWidgets import QDialog, QDialogButtonBox

from packages.UI.save_filter_dialog import Ui_Dialog as Ui_SaveFilterDialog
from packages.dialogs.auxiliar_dialogs import MessageBox


class SaveFilterDialog(QDialog):
    def __init__(self, parent, name_dict):
        super(SaveFilterDialog, self).__init__(parent)
        self.ui = Ui_SaveFilterDialog()
        self.ui.setupUi(self)

        self.acceptButton = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.cancelButton = self.ui.buttonBox.button(QDialogButtonBox.Cancel)
        self.init_ui(parent, name_dict)

    def init_ui(self, parent, name_dict):
        self.ui.lineEdit.setFocus()
        self.acceptButton.clicked.connect(lambda: self.on_accept(parent, name_dict))
        self.cancelButton.clicked.connect(lambda: self.on_cancel())

    def on_accept(self,parent, name_dict):
        if os.path.isfile(str.join('', [
            os.curdir,
            os.sep,
            '.databases', os.sep,
            self.ui.lineEdit.text(), '.flt'
        ])):
            overWrite = MessageBox(
                lambda: self.accept_routine(name_dict),
                'Ya existe un filtro con el nombre <{}>.\n '
                'si continua con la operacion va a sobreescribir los datos'.format(
                    self.ui.lineEdit.text()
                ),'w','Conflicto de Archivo: Nombre ya Existe',
                '\n\nPresionse "SI" para continuar con ese nombre y "NO" para cambiarlo',
                lambda: SaveFilterDialog(parent, name_dict).exec_()
            )
            overWrite.exec_()
            return
        else:
            self.accept_routine(name_dict)

    def accept_routine(self,name_dict):
        name_dict.update({'name': self.ui.lineEdit.text()})
        self.accept()

    def on_cancel(self):
        self.reject()