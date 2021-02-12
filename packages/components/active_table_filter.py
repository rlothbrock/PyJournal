from packages.dialogs.auxiliar_dialogs import selfCloseInterface
from packages.dialogs.filter_dialog import FilterDialog


def filter_active_table(self):
    # fields = get_template_fields(self.table_on_target)
    # data = crud_driver(self,self.table_on_target,'read',{})

    fields = self.headers_for_tab1.copy()
    data = self.data_to_display_on_tab1.copy()

    if len(data) == 0:
        return selfCloseInterface(
            'No hay datos para filtrar !!',4,2,
            'Error del Filtro',
            '\n\nVaya a: \nMenu Herramientas > Ver\n y seleccione alguna tabla para aplicarle filtros'
        )
    filter_dialog = FilterDialog(self,fields,data)
    filter_dialog.exec_()
    self.display_table_signal.emit()
    return

