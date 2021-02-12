from PySide2.QtCore import Slot
from packages.components.data_display_tab import execute_display_table
from packages.dialogs.auxiliar_dialogs import selfCloseInterface
from packages.dialogs.capital_tool_dialog import CapitalFormDialog
from packages.dialogs.common_tool_dialogs import tool_launcher, HelpOfflineDialog, main_help_text_template
from packages.dialogs.purchases_tool_dialog import PurchasesFormDialog
from packages.dialogs.sales_tool_dialog import SalesFormDialog
from packages.modules.data_import_export import import_data_to_diary, export_data_from_diary
from packages.modules.db_templates_manager import connect_toDB
from packages.routines.change_session_date import manage_date_session
from packages.routines.database_saver import database_saver_routine
from packages.routines.quit_app import quit_app_routine
from packages.routines.status_saver import status_saver_routine


def set_menus(self):
    print('loading menus actions...')
    # menu File
    self.ui.actionGuardar_el_estado_de_la_aplicacion.triggered.connect(lambda: status_saver_routine(self))
    self.ui.actionImportar_datos_desde_CSV.triggered.connect(lambda: import_data_to_diary(self))
    self.ui.actionExportar_Diario_hacia_CSV.triggered.connect(lambda: export_data_from_diary(self))
    self.ui.actionCerrar_la_aplicacion.triggered.connect(lambda: quit_app_routine(self))

    # menu Databases
    self.ui.action_connect_Celulares.triggered.connect(lambda: connect_toDB(self, 'cellsDB.db'))
    self.ui.action_connect_Zapatos.triggered.connect(lambda: connect_toDB(self, 'shoesDB.db'))
    self.ui.action_connect_Bisuteria.triggered.connect(lambda: connect_toDB(self, 'bisutDB.db'))
    self.ui.actionCrear_nueva.triggered.connect(lambda: print('todo'))  # todo
    self.ui.actionSalvar_el_estado_de_la_DB_actual.triggered.connect(lambda: database_saver_routine(self))

    # menu Tools
    self.ui.actionA_adir_Compras_2.triggered.connect(lambda: tool_launcher(self, PurchasesFormDialog))
    self.ui.actionA_adir_Ventas_2.triggered.connect(lambda: tool_launcher(self, SalesFormDialog))
    self.ui.actionModificar_la_inversion.triggered.connect(lambda: tool_launcher(self, CapitalFormDialog))
    self.ui.actionVer_Inventario.triggered.connect(lambda: execute_display_table(self, 'stock'))
    self.ui.actionVer_Ventas.triggered.connect(lambda: execute_display_table(self, 'sales'))
    self.ui.actionVer_Capital.triggered.connect(lambda: execute_display_table(self, 'capital'))
    self.ui.actionVer_Diario.triggered.connect(lambda: execute_display_table(self, 'diary'))
    self.ui.actionCambiar_la_fecha_de_la_sesion.triggered.connect(lambda: manage_date_session(self))
    self.ui.actionUsar_verificacion_de_datos.triggered.connect(lambda: lock_entry(self))

    # menu Help
    self.ui.actionAyuda_offline.triggered.connect(lambda: tool_launcher(self, HelpOfflineDialog,main_help_text_template))


@Slot()
def lock_entry(self):
    self.use_secure_entry = self.ui.actionUsar_verificacion_de_datos.isChecked()
    sem = 'Activado' if self.use_secure_entry else 'Desactivado'
    print('Secure Entry Mode: {}'.format(sem))
    selfCloseInterface('Secure Entry Mode: {}'.format(sem),8,1,'Secure Entry Mode',
                       'Cuando el modo seguro está activo,'+
                       ' se solicita una confirmacion antes de entrar los datos a la base de datos. De esta manera se'
                       +' evitan errores en la entrada de datos.\n\nCuando está desactivado la entrada es directa')
    return
