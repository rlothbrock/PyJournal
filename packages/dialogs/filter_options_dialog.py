# store here class for options (dialog with buttons) on filter
# steps:
#   el dialogo tiene 3 opciones
#       guardar - abrir - cerrar sin guardar
import os

from PySide2.QtWidgets import QDialog, QDialogButtonBox, QFileDialog

from packages.UI.filter_options import Ui_Dialog as Ui_filterOptions
from packages.dialogs.auxiliar_dialogs import selfCloseInterface
from packages.dialogs.save_filter_dialog import SaveFilterDialog


class FilterOptions(QDialog):
    def __init__(self, parent):
        super(FilterOptions, self).__init__(parent)

        self.ui = Ui_filterOptions()
        self.ui.setupUi(self)

        self.openButton = self.ui.buttonBox.button(QDialogButtonBox.Open)
        self.discardButton = self.ui.buttonBox.button(QDialogButtonBox.Discard)
        self.saveButton = self.ui.buttonBox.button(QDialogButtonBox.Save)

        self.init_ui(parent)

    def init_ui(self, parent):
        # signals:
        self.openButton.clicked.connect(lambda: self.on_open(parent))
        self.saveButton.clicked.connect(lambda: self.on_save(parent))
        self.discardButton.clicked.connect(lambda: self.on_discard())

    def on_save(self, parent):
        str_from_data_to_save = str(parent.filter_data_dict.copy())
        filename = {}
        name_dialog = SaveFilterDialog(parent, filename)
        name_dialog.exec_()
        if filename.get('name') is None: return
        filter_file = open(
            '{}{}.databases{}{}.flt'.format(
                os.curdir, os.sep, os.sep, filename.get('name')
            ), 'w'
        )
        filter_file.write(str_from_data_to_save)
        filter_file.close()
        selfCloseInterface(
            'Filtro salvado como: {}'.format(filename.get('name')),
            2,1,'Filtro Salvado','\n\npara cargar los datos use la opcion Abrir'
        )
        print('data: {}\nfilename:{}'.format(str_from_data_to_save, filename))
        self.accept()
        return

    def on_open(self, parent):
        #       sale el directorio donde estan todos los dicts guardados
        #       escoger el filename
        #       leer el filename
        #       new_dict = eval(data)
        #       dict = new_dict
        #   cerrar sin guardar
        #       cerrar el dialog y ya reject()
        filename = QFileDialog.getOpenFileName(
            self,
            'Open Filter File: ',
            '.databases',
            '*.flt'
        )
        data = open(filename[0],'r').readlines()[0]
        print('debug data: {}'.format(data))
        new_dict = eval(data)
        parent_keys = list((field.get('name') for field in parent.filter_data_dict))
        new_keys = list((field.get('name') for field in new_dict))
        if any((key not in parent_keys for key in new_keys)):
            selfCloseInterface(
                'el filtro que intenta cargar no es compatible con la tabla de datos que se muestra actualmente',
                5,3,'Error: Filtro incorrecto',
                'El filtro que ha seleccionado contiene campos que no estan presentes'
                'en la tabla que se encuentra actualmente en uso.\n Posibles soluciones:\n> Cambiar La '
                'tabla para que sea compatible con el filtro sleleccionado: Herramientas> Ver'
                '\n> Cambiar el nombre del filtro que desea cargar: Opciones > Abrir'
            )
            return
        parent.filter_data_dict = new_dict.copy()
        # todo relaunch build data on list ??
        self.accept()

    def on_discard(self):
        self.reject()
        return
