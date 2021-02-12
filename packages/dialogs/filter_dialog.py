from PySide2.QtCore import Slot
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QDialog, QDialogButtonBox, QListWidgetItem

from packages.UI.filters_form import Ui_Dialog as Ui_Filter_Dialog

from packages.dialogs.auxiliar_dialogs import MessageBox
from packages.dialogs.common_tool_dialogs import tool_launcher, HelpOfflineDialog
from packages.modules.db_templates_manager import regexp

modify_field_label_template = 'Modificar el resultado de: {}'
descriptor_text_label_template = 'El campo "{}" solo va a mostrar las filas "{} {}"'
filter_help_text_template = '''Ayuda
 
El filtro permite cambiar los campos que se van a mostrar asi como afectar los resultados que se muestran en ellos. Mediante el uso combinado del filtro en varios campos a la vez se puede lograr mostrar consultas complejas. La aplicacion soporta el uso de varios filtros al unisono de manera que sea posible adaptar a las necesidades de la consulta.

Funciones del filtro:
Seleccione o Deseleccione los campos para mostrarlos o quitarlos de la tabla filtrada. 
Los campos que sean seleccionados pueden mostrarse con o sin restriccion de los resultados, de acuerdo a los operadores que se le apliquen. Los campos que NO sean seleccionados NO van a mostrarse en la tabla filtrada. 
Por defecto todos los campos vienen seleccionados.

Seleccione el operador apropiado de acuerdo a la restriccion que quiere aplicar a cada campo
El operador es el que aplica la restriccion a los campos. El filtro cuenta con varios de ellos:
 None    : Este operador muestra el campo con todos los resultados. Es el operador por defecto
 =       : Este operador muestra los resultados exactamente iguales a los que se definan en el valor del filtro
 <>      : Este operador muestra todos los resultados EXCEPTO los exactamente iguales a los que se definan en el valor del filtro
 >       : Este operador muestra los resultados mayores a los que se definan en el valor del filtro
 >=      : Este operador muestra los resultados mayores o iguales a los que se definan en el valor del filtro
 <       : Este operador muestra los resultados menores a los que se definan en el valor del filtro
 <=      : Este operador muestra los resultados menores o iguales a los que se definan en el valor del filtro
 regexp  : Este operador muestra los resultados parecidos a los que se definan en el valor del filtro

Escriba el valor que quiere usar para aplicar la restriccion en cada campo.
En la barra de Edicion de Valores usted puede aplicar el valor que desea usar para modificar los resultados del filtro
En el caso de que el operador sea None no se necesitan aplicar valores en la barra.

Funciones de los botones:
El boton Reset limpia los filtros y reestablece a los valores originales a todos los campos (sin filtro)

'''
len_of_results_label_template = 'Los resultados abarcan {} filas.'

# deprecated function ... to be eliminated on next versions
# def replace__(iterable_, index_, data_):
#     iter__ = list(iterable_).copy()
#     iter__.pop(index_)
#     iter__.insert(index_, data_)
#     return iter__


def operation_eval(operator__, value__, context):  # must return a boolean...
    operators = {'<>': find_exceptions, 'None': find_all, '=': find_equal, 'regexp': regexp}
    if operator__ in ['>', '>=', '<', '<=']:
        str__ = '{} {} {}'.format(context, operator__, value__)
        result = eval(str__)
    else:
        if operators.get(operator__) is None:
            result = find_all(value__, context)
        else:
            result = operators.get(operator__)(value__, context)
    return result


def find_exceptions(value, context):
    return not (value == context)


def find_all(value, context):
    return True


def find_equal(value, context):
    return value == context


class FilterDialog(QDialog):
    def __init__(self, parent, fields, data):
        super(FilterDialog, self).__init__(parent)
        self.ui = Ui_Filter_Dialog()
        self.ui.setupUi(self)

        self.applyButton = self.ui.buttonBox.button(QDialogButtonBox.Apply)
        self.discardButton = self.ui.buttonBox.button(QDialogButtonBox.Discard)
        self.resetButton = self.ui.buttonBox.button(QDialogButtonBox.Reset)
        self.helpButton = self.ui.buttonBox.button(QDialogButtonBox.Help)

        self.parent_data = data
        self.parent_fields = fields
        self.filter_data_dict = []

        self.filtered_fields = self.parent_fields.copy()
        self.filtered_data = self.parent_data.copy()
        self.result_rows_len = len(self.filtered_data)

        self.init_ui(parent)

    def init_ui(self, parent):
        self.generate_filter_data_dict()
        self.build_listWidget_field_manager()
        self.update_textedit_display_filter()
        self.set_proper_values_on_filter_values_comboBox(0)

        # set labels
        self.ui.label_modificar_field.setText(
            modify_field_label_template.format(self.get_selected_field_name())
        )
        self.ui.label_descriptor_del_filtro.setText(
            self.get_descriptor_label()
        )
        self.ui.label_filas_de_rsultados.setText(
            len_of_results_label_template.format(self.result_rows_len))
        # init signals
        self.init_signals_on_ui(parent)
        return

    def init_signals_on_ui(self, parent):
        self.ui.listWidget_field_manager.itemClicked.connect(self.item_check_state_changed)
        self.ui.listWidget_field_manager.currentItemChanged.connect(self.item_selected_reaction)
        self.ui.listWidget_field_manager.currentItemChanged.connect(self.set_proper_values_on_filter_values_comboBox)
        self.ui.comboBox_field_modificator.currentTextChanged.connect(
            self.on_change_modificator_comboBox_current_text
        )
        self.ui.comboBox_valor_del_filtro.currentIndexChanged.connect(
            lambda: self.item_selected_reaction(self.get_current_item_on_listWidget())
        )
        self.ui.lineEdit_valor_del_campo_modificado.textChanged.connect(
            lambda: self.item_selected_reaction(self.get_current_item_on_listWidget())
        )
        self.discardButton.clicked.connect(self.on_discard_button_clicked)
        self.helpButton.clicked.connect(lambda: tool_launcher(self, HelpOfflineDialog, filter_help_text_template))
        self.resetButton.clicked.connect(self.on_reset_button_clicked)
        self.applyButton.clicked.connect(lambda: self.on_apply_button_clicked(parent))

        # todo
        self.ui.toolButton_filter_options.clicked.connect(self.debug_printer_delete_after_finish)

    # Slots ________________________
    @Slot()  # todo delete this debug slot...
    def debug_printer_delete_after_finish(self):
        print('Slot to do')
        return

    @Slot()
    def item_selected_reaction(self, item):
        self.modificar_data_dict_y_actualizar_textEdit()
        self.manejar_estado_habilitado_condicional_de_combo_y_lineEdit(item)
        self.manejar_mensaje_en_las_labels_segun_estado_del_campo(item)
        return

    @Slot()
    def item_check_state_changed(self, item):
        self.modificar_data_dict_y_actualizar_textEdit()
        if any([
            self.ui.listWidget_field_manager.currentItem() == item,
            item in self.ui.listWidget_field_manager.selectedItems()
        ]):
            self.manejar_estado_habilitado_condicional_de_combo_y_lineEdit(item)
            self.manejar_mensaje_en_las_labels_segun_estado_del_campo(item)
        return

    # ---------- todo
    def show_options_routine(self):
        # esta fun se lanza para mostrar los botones de salvar y cargar los filtros
        pass

    # regular methods___________________

    def build_listWidget_field_manager(self):
        __items_for_field_list = list(map(lambda i: QListWidgetItem(i), self.parent_fields))
        self.ui.listWidget_field_manager.clear()
        selected_state_generator = (True if i == 0 else False for i in range(len(__items_for_field_list)))
        for item in __items_for_field_list:
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Checked)
            self.ui.listWidget_field_manager.addItem(item)
            item.setSelected(next(selected_state_generator))

    def modificar_data_dict_y_actualizar_textEdit(self):
        self.actualizar_los_valores_de_data_dict()
        self.update_textedit_display_filter()

    def manejar_estado_habilitado_condicional_de_combo_y_lineEdit(self, selected_item):
        self.ui.comboBox_field_modificator.setEnabled(selected_item.checkState() is Qt.CheckState.Checked)
        self.ui.lineEdit_valor_del_campo_modificado.setEnabled(
            all([
                selected_item.checkState() is Qt.CheckState.Checked,
                self.ui.comboBox_field_modificator.currentIndex() == 7
            ])
        )
        self.ui.comboBox_valor_del_filtro.setEnabled(
            all([
                selected_item.checkState() is Qt.CheckState.Checked,
                self.ui.comboBox_field_modificator.currentIndex() != 0,
                self.ui.comboBox_field_modificator.currentIndex() != 7
            ])
        )
        self.ui.label_3.setEnabled(selected_item.checkState() is Qt.CheckState.Checked)

    def manejar_mensaje_en_las_labels_segun_estado_del_campo(self, selected_item):
        if selected_item.checkState() is Qt.CheckState.Unchecked:
            self.ui.label_modificar_field.setText('el campo "{}" esta desactivado'.format(selected_item.text()))
            self.ui.label_descriptor_del_filtro.setText('el campo "{}" esta desactivado'.format(selected_item.text()))
            return
        else:
            self.ui.label_modificar_field.setText(modify_field_label_template.format(selected_item.text()))
            self.ui.label_descriptor_del_filtro.setText(self.get_descriptor_label())
            return

    def update_textedit_display_filter(self):
        # {name checked operator value}
        data__ = map(
            lambda item: '{}    {}    {}'.format(item.get('name'), item.get('operator'), item.get('value')),
            filter(
                lambda dict__: dict__.get('checked') is True,
                self.filter_data_dict
            )
        )
        str__ = str.join('\n----------------\n', data__)
        self.ui.textEdit_plantilla_del_filtro.setText(str__)

        return

    def get_selected_field_name(self):
        return self.ui.listWidget_field_manager.selectedItems()[0].text()

    def get_descriptor_label(self):
        return descriptor_text_label_template.format(
            self.get_selected_field_name(),
            self.ui.comboBox_field_modificator.currentText().split('"')[2].split('Mostrar')[1],
            self.ui.lineEdit_valor_del_campo_modificado.text() if
            self.ui.lineEdit_valor_del_campo_modificado.isEnabled() else
            self.ui.comboBox_valor_del_filtro.currentText()
        )

    def generate_filter_data_dict(self):  # only for use on_init
        # [dict] {name: str checked: bool selected: bool operator: str value: str }
        self.filter_data_dict.clear()
        self.filter_data_dict.extend(list(map(
            lambda field: {
                'name': field,
                'checked': True,
                'operator': None,
                'value': None
            },
            self.parent_fields
        )))
        return

    def actualizar_los_valores_de_data_dict(self):
        # esta primera funcion altera los valores de operator y value (el resto de la fun es para checked y name)
        self.modificar_operator_y_value_en_data_dict()
        # items__ is a list with all listWidget_field_manager items
        items__ = list((
            self.ui.listWidget_field_manager.item(row) for row in range(self.ui.listWidget_field_manager.count())
        ))
        # data__ is a map that converts each item i items__ in its dict version on data_dict
        data__ = map(
            lambda item_widget: {
                'name': item_widget.text(),
                'checked': item_widget.checkState() is Qt.CheckState.Checked,
                'operator': next(
                    filter(lambda item_data: item_data.get('name') == item_widget.text(), self.filter_data_dict)).get(
                    'operator'),
                'value': next(
                    filter(lambda item_data: item_data.get('name') == item_widget.text(), self.filter_data_dict)).get(
                    'value')
            },
            items__)
        data_extend = list(data__)
        self.filter_data_dict.clear()
        self.filter_data_dict.extend(data_extend)

        # self.apply_filter_on_data()
        return

    def modificar_operator_y_value_en_data_dict(self):
        # this function changes operator and value in the corresponding item (dict) of data_dict (list)
        current__ = self.ui.listWidget_field_manager.currentItem()
        name = current__.text() if current__ is not None else self.ui.listWidget_field_manager.selectedItems()[0].text()
        item_dict = next(filter(lambda item: item.get('name') == name, self.filter_data_dict))
        item_dict.update({
            'operator': self.ui.comboBox_field_modificator.currentText().split('"')[1],
            'value': self.ui.comboBox_valor_del_filtro.currentText() if
            self.ui.comboBox_valor_del_filtro.isEnabled() else
            self.ui.lineEdit_valor_del_campo_modificado.text()
        })
        old__ = self.filter_data_dict.copy()
        self.filter_data_dict.clear()
        self.filter_data_dict.extend(list(map(
            lambda item_dict_old: item_dict if item_dict_old.get('name') == name else item_dict_old,
            old__
        )))

    def get_current_item_on_listWidget(self):
        return self.ui.listWidget_field_manager.currentItem() if \
            self.ui.listWidget_field_manager.currentItem() is not None else \
            self.ui.listWidget_field_manager.selectedItems()[0]

    def on_change_modificator_comboBox_current_text(self, text):
        if 'None' in text:
            self.ui.comboBox_valor_del_filtro.setEnabled(False)
            self.ui.lineEdit_valor_del_campo_modificado.setEnabled(False)
            self.ui.lineEdit_valor_del_campo_modificado.setText('None')
        self.item_selected_reaction(self.get_current_item_on_listWidget())
        return

    def set_proper_values_on_filter_values_comboBox(self, fixed_index=None):
        index__ = self.ui.listWidget_field_manager.currentRow() if \
            self.ui.listWidget_field_manager.currentRow() is not None else 0
        index = index__ if fixed_index is None or type(fixed_index) is not int else fixed_index
        values = set(map(
            lambda item: str(item[index]),
            self.parent_data
        )).copy()
        self.ui.comboBox_valor_del_filtro.clear()
        self.ui.comboBox_valor_del_filtro.addItems(values)
        return

    def apply_filter_on_data(self):
        checked_fields = self.get_checked_fields()
        total_fields = list(range(self.ui.listWidget_field_manager.count())).copy()
        self.filtered_data = list(map(
            lambda row: list(filter(lambda cell: cell is not None, map(
                lambda cell_index, cell: cell if cell_index in checked_fields else None,
                total_fields,
                row
            ))).copy(),
            self.filtered_data
        )).copy()

        self.filtered_fields = list(filter(  # this blocks removes any unchecked header
            lambda i: i is not None,
            map(
                lambda data_dict__: data_dict__.get('name') if data_dict__.get('checked') else None,
                self.filter_data_dict
            )))

        for field_dict in self.filter_data_dict:
            if not field_dict.get('checked'):
                continue
            else:
                name__ = field_dict.get('name')
                operator__ = field_dict.get('operator')
                value__ = field_dict.get('value')
                try:
                    self.filtered_data = list(filter(  # evals row_ cell: and filters for True
                        lambda row: operation_eval(operator__, value__, row[self.filtered_fields.index(name__)]),
                        self.filtered_data
                    )).copy()
                    print('debug: parcial con:\nfield_dict: {}\noper: {}\nvalue: {}\ndata: {}'.format(
                        field_dict,operator__,value__,self.filtered_data
                    )+'\n'+'-'*100)
                except BaseException as err:
                    print('>>>>>err:\n{} '.format(err))
                    continue

    def on_reset_button_clicked(self):
        self.generate_filter_data_dict()
        self.build_listWidget_field_manager()
        self.update_textedit_display_filter()
        self.item_selected_reaction(self.ui.listWidget_field_manager.selectedItems()[0])
        return

    def get_checked_fields(self):
        return list(filter(
            lambda index: index is not None,
            map(
                lambda dict__: self.filter_data_dict.index(dict__) if dict__.get('checked') else None,
                self.filter_data_dict)
        ))

    def on_discard_button_clicked(self):
        confirm_exit = MessageBox(
            lambda: self.reject(),
            'Desea Descartar los Cambios en el Filtro?',
            'q', 'Descartar los Cambios en el Filtro',
            '\n\nSi Descarta no se aplica ningun filtro y se pierden los cambios realizados que no hayan sido guardados'
        )
        confirm_exit.exec_()
        return

    def on_apply_button_clicked(self, parent):
        self.apply_filter_on_data()
        parent.headers_for_tab1 = self.filtered_fields.copy()
        parent.data_to_display_on_tab1 = self.filtered_data.copy()
        self.accept()
        return
