from random import random

from PySide2.QtWidgets import QDialog
from packages.UI.help_offline import Ui_Dialog as Ui_help_dialog
# common resources-------------------
from packages.dialogs.auxiliar_dialogs import selfCloseInterface

main_help_text_template = '''
Introduccion
Esta aplicacion se utiliza para llevar registros simplificados de la actividad de un local de ventas.
Soporta hasta 3 areas de ventas distintas (puede ser aumentadas de ser necesario)
En la version actual (1.0.0) no existe una variante online, por lo que la actividad de registro se realiza de manera retroactiva

Funcionamiento:
La aplicacion cuenta con varias herramientas
Añadir Compras
	Se utiliza para insertar todas las compras del area en el dia que se esta trabajando
Añadir Ventas
	Se utiliza para añadir las ventas del area, se recomienda utilizar luego de añadir las compras para evitar un saldo negativo falso
Modificar la inversion
	Se utiliza para mantener un registro de la cantidad de dinero que tiene cada parte en el negocio en cuestion, en la version actual 1.0.0 solamente soporta 2 partes predefinidas
Cambiar la fecha de la sesion
	Se usa para el caso en el que se quiera trabajar con dias anteriores a la fecha en la que  abre la aplicacion.
	La aplicacion por defecto va a insertar los datos con la fecha del dia actual del que se trate, es por ello que se debe tener en cuenta a la hora de insertar datos de manera retroactiva

Otras caracteristicas
Menu Base de Datos:
	En este menu podemos salvar el estado de la base de datos en la que estamos trabajando para de esta manera mantener una copia de los cambios realizados hasta el momento de la salva
	Tambien podemos añadir una nueva base de datos (no soportado en la version actual 1.0.0)
	
	La funcion mas importante de este menu es la que nos permite cambiar la base de datos en la que vamos a trabajar, es de tener en cuenta que a la hora de rebajar en areas diferentes debe cambiarse la base de datos, a fin de usar la respectiva de cada area
Menu Archivo
	En este menu podemos exportar e importar los datos hacia un archivo CSV (formato compatible con excel)
	Tambien podemos guardar el estado de la aplicacion (en la version actual solamente incluye el tamaño del viewport y la base de datos a la que se estaba conectado al momento de cerrar)
	Tambien aqui tenemos la opcion de cierre seguro, dado que el cierre desde este menu evita perdidas de datos no deseadas

Version actual 1.0.0 inicio: 16-01-2021
'''


def tool_launcher(self, tool, template=None):
    try:
        # set proper tools
        if template is not None:
            dialog = tool(self, template)
        else:
            dialog = tool(self)
            self.ui.tabWidget.setCurrentIndex(0)
        ph = self.geometry().height()
        pw = self.geometry().width()
        px = self.geometry().x()
        py = self.geometry().y()
        dw = dialog.width()
        dh = dialog.height()
        dialog.setGeometry(pw - dw + px, ph - dh + py, dw, dh)
        dialog.show()
        return
    except IndexError as error:
        return selfCloseInterface(
            'La herramienta que solicita no puede ser mostrada',
            8,3,'Error en la herramienta',
            '\n\n si se trata de ventas, es probable que no cuente con articulos en su inventario\nsi se trata de '
            'compras revise el saldo (cash_) antes de hacer alguna compra'
        )


# todo
#  so far the rent is fixed (125). in future versions must be possible to dynamically
#  adjust the rent through a dialog on the app level.

def build_salary(parent, sale, price):
    sale, proffit = float(sale), float(sale) - float(price)

    bases = {
        'cellsDB.db': proffit,
        'bisutDB.db': sale,
        'shoesDBdb.db': 1
    }
    salaries = {
        'cellsDB.db': lambda prof_: 10 / 100 * prof_,
        'bisutDB.db': lambda sale_: 6 / 100 * sale_,
        'shoesDB.db': lambda _: 25
    }
    db__ = parent.status.get('connected_to')
    salary_calculator = salaries.get(db__)
    bases_ = bases.get(db__)
    print('debug: db__ : {} salary_calc: {}  bases: {}'.format(db__, salary_calculator,bases_))
    return salary_calculator(bases_)


    # todo:
    #   on next versions must implement a proper way to define the salary rate
    #   on the main app (through an action on menus ) based on that rate salary must
    #   be calculated. so far it will be declared here (fixed) and there's no way
    #   to change it.


def build_item_code(price, consignation):
    consignation__ = 'c' if consignation else 'p'
    return '{}{:X}-{}'.format(consignation__, int(random() * 10 ** 18), price)


def build_data_template():
    return [0, 0, 0, 0, 0, 0, 0, '', 0, 0, '', '', 0, 0, '', 0, 0, 0, 0, 0, '']


def buddy_sync(master, slave, dependant=None, value=0, is_text=False, trigger=True):
    idx = master.currentIndex()
    if slave is not None:
        slave.setCurrentIndex(idx)
    if dependant is not None and trigger:
        if is_text:
            dependant.setText(value)
        if not is_text:
            dependant.setValue(value)


# ---
class HelpOfflineDialog(QDialog):
    def __init__(self, parent, template):
        super(HelpOfflineDialog, self).__init__(parent)
        self.ui = Ui_help_dialog()
        self.ui.setupUi(self)

        self.ui.textEdit.setText(template)
