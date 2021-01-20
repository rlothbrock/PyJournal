from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication

from dialogs.auxiliar_dialogs import MessageBox
from routines.database_saver import database_saver_routine
from routines.status_saver import status_saver_routine


@Slot()
def quit_app_routine(self):
    confirm = MessageBox(
        lambda: shutdown_app(self),
        'Desea salir de la aplicacion?',
        'q',
        'Salir',
        'antes de salir revise que todo esté bien guardado'
    )
    confirm.show()


def shutdown_app(self):
    status_saver_routine(self,silent=True)
    QApplication.quit()