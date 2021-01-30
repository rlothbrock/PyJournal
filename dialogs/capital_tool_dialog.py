# Capital entries Form -------------------------------
from PySide2.QtWidgets import QDialog, QDialogButtonBox
from dialogs.auxiliar_dialogs import MessageBox, selfCloseInterface
from dialogs.tool_dialogs import build_data_template
from modules.crud_sqlite import crud_driver
from modules.db_templates_manager import get_template_fields, get_index_in_template
from UI.capital_form import Ui_DialogCapital


class CapitalFormDialog(QDialog):
    def __init__(self, parent):
        super(CapitalFormDialog, self).__init__(parent)
        self.ui = Ui_DialogCapital()
        self.ui.setupUi(self)

        self.data_for_diary = []
        self.apply_button = self.ui.buttonBox.button(QDialogButtonBox.Apply)
        self.cancel_button = self.ui.buttonBox.button(QDialogButtonBox.Cancel)
        self.reset_button = self.ui.buttonBox.button(QDialogButtonBox.Reset)

        self.init_ui(parent)

    def init_ui(self, parent):
        self.fill_label()
        self.ui.nombreDelQueInsertaElDineroComboBox.currentTextChanged.connect(self.fill_label)
        self.ui.extraccionDelMontoCheckBox.stateChanged.connect(self.fill_label)
        self.ui.cantidadDeDineroDoubleSpinBox.valueChanged.connect(self.fill_label)

        self.cancel_button.clicked.connect(self.reject_form)
        self.reset_button.clicked.connect(self.clean_form)
        self.apply_button.clicked.connect(lambda: self.apply_form(parent))

    def fill_label(self):
        operation = 'extraer' if self.ui.extraccionDelMontoCheckBox.isChecked() else 'añadir'
        amount = '$ {:,.2f}'.format(self.ui.cantidadDeDineroDoubleSpinBox.value())
        owner = self.ui.nombreDelQueInsertaElDineroComboBox.currentText()
        self.ui.notasDeCapital.setText(
            'Esta accion va a {}: {} pesos del aporte a la inversion de {}. '
            'Prestar atención antes de realizar cualquier entrada en esta seccion '.format(
                operation, amount, owner
            ))

    def apply_form(self, parent):
        # props alias...
        data_len__ = get_template_fields('diary')
        comments__ = get_index_in_template('diary', 'comments')
        amount__ = get_index_in_template('diary', 'amount')
        owner__ = get_index_in_template('diary', 'owner')
        invested__ = get_index_in_template('diary', 'invested_')
        cash__ = get_index_in_template('diary', 'cash_')
        total__ = get_index_in_template('diary', 'total_')
        parts__ = [get_index_in_template('diary', 'robert_'), get_index_in_template('diary', 'ariadna_')]
        sign__ = -1 if self.ui.extraccionDelMontoCheckBox.isChecked() else 1
        last_row_data__ = crud_driver(parent, 'diary', 'read', {})
        last_row_data = build_data_template() if len(last_row_data__) == 0 else last_row_data__[-1]
        last_row_data = build_data_template() if len(data_len__) > len(last_row_data) else last_row_data
        data = build_data_template()

        data[comments__] = self.ui.comentariosDeCapitalLineEdit.text()
        data[amount__] = self.ui.cantidadDeDineroDoubleSpinBox.value() * sign__
        data[owner__] = self.ui.nombreDelQueInsertaElDineroComboBox.currentText()
        data[parts__[0]] = last_row_data[parts__[0]]
        data[parts__[1]] = last_row_data[parts__[1]]
        data[parts__[self.ui.nombreDelQueInsertaElDineroComboBox.currentIndex()]] = \
            last_row_data[parts__[self.ui.nombreDelQueInsertaElDineroComboBox.currentIndex()]] + data[amount__]

        # this block is for defunding protection:
        amount___ = float(data[parts__[self.ui.nombreDelQueInsertaElDineroComboBox.currentIndex()]])
        if amount___ < 0 :
            print('capital extraction denied. No enough funds ')
            selfCloseInterface(
                'No puede extraer $ {:,.2f} del saldo de {}.\nFondos Insuficientes'.format(
                    self.ui.cantidadDeDineroDoubleSpinBox.value(),
                    self.ui.nombreDelQueInsertaElDineroComboBox.currentText()
                ),
                5,3,'Extraccion Denegada',
                'No esta permitido extraer mas dinero que el total de la parte de un socio ')
            return self.clean_form()

        data[invested__] = last_row_data[invested__]
        data[total__] = data[parts__[0]] + data[parts__[1]]
        data[cash__] = data[total__] - data[invested__]

        confirm = MessageBox(
            lambda: parent.append_data_to_diary(data),
            'Desea confirmar la Entrada?', 'q', 'Confirmar Entrada', self.ui.notasDeCapital.text())
        confirm.show()
        return

    def clean_form(self):
        self.ui.nombreDelQueInsertaElDineroComboBox.setCurrentIndex(0)
        self.ui.cantidadDeDineroDoubleSpinBox.setValue(0)
        self.ui.extraccionDelMontoCheckBox.setChecked(False)
        self.ui.comentariosDeCapitalLineEdit.clear()
        self.ui.validacionDeLaEntradaLineEdit.clear()

    def reject_form(self):
        self.clean_form()
        self.reject()


# todo:
#   - debo añadir una verificacion al capital de manera tal que no me permita sacar
#   mas dinero del que tengo invertido, es decir que el maximo extraible de la inver
#   sion sea el maximo que tiene cada socio en la inversion. esto debe hacerse a
#   nivel de chequeo de formulario, antes de procesar la orden
#   - tambien debo añadir en el form la opcion de verificar contra la contraseña,
#   de manera tal que si no se provee la contraseña correcta se rechace la entrada.
#