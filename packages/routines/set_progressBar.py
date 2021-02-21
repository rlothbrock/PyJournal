import math

from PySide2 import QtCore
from PySide2.QtWidgets import QProgressBar


def set_progress_bar(self):
    self.progressBar = QProgressBar(self)
    self.progressBar.setGeometry(
        math.floor(self.width() / 2) - math.floor(self.width() / 4),
        math.floor(self.height() / 2) - math.floor(self.height() / 50),
        math.floor(self.width() / 2), math.floor(self.height() / 25))
    self.progressBar.close()
    #self.progressBar.setHidden(True)
    self.show_progress_bar_signal.connect(lambda: set_modality_and_show(self))
    self.close_progress_bar_signal.connect(lambda: self.progressBar.close())
    self.update_progress_bar_signal.connect(lambda v: self.progressBar.setValue(v))
    return

def set_modality_and_show(self):
    self.progressBar.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
    self.progressBar.show()