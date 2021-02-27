from PySide2.QtWidgets import QDialog, QDialogButtonBox

from packages.UI.rent_salary_form import Ui_RentOrSalaryDialog
from packages.dialogs.auxiliar_dialogs import selfCloseInterface


def set_rent_or_salary_routine(self):
    rent_sal_mod_dialog = SalaryOrRentFormDialog(self)
    rent_sal_mod_dialog.exec_()


class SalaryOrRentFormDialog(QDialog):
    def __init__(self, parent):
        super(SalaryOrRentFormDialog, self).__init__(parent)
        self.ui = Ui_RentOrSalaryDialog()
        self.ui.setupUi(self)

        self.setSalary = self.ui.pushButtonChangeSalary
        self.setRent = self.ui.pushButtonChangeRent
        self.closeButton = self.ui.buttonBox.button(QDialogButtonBox.Close)
        self.radios = {
            0: self.ui.radioButton_fixed_rate,
            1: self.ui.radioButton_rate_over_sales,
            2: self.ui.radioButton_rate_over_proffit
        }

        self.init_ui(parent)

    def init_ui(self, parent):
        self.ui.doubleSpinBox_changeRent.setMaximum(10 ** 6)
        self.ui.doubleSpinBox_changeSalary.setMaximum(1000)

        self.read_parent_values_and_update_ui(parent)
        self.manage_conditional_enabled_state(
            self.ui.checkBox_changeSalary.checkState()
            , 'salary')
        self.manage_conditional_enabled_state(
            self.ui.checkBox_changeRent.checkState()
            , 'rent')

        # signals
        for radio in self.radios.values():
            # radio.toggled.connect(self.adjust_limit_on_salary_rate)
            radio.clicked.connect(self.adjust_limit_on_salary_rate)
        self.closeButton.clicked.connect(self.reject)
        self.ui.checkBox_changeRent.stateChanged.connect(
            lambda s: self.manage_conditional_enabled_state(s, 'rent')
        )
        self.ui.checkBox_changeSalary.stateChanged.connect(
            lambda s: self.manage_conditional_enabled_state(s, 'salary')
        )
        self.setRent.clicked.connect(lambda: self.on_set_rent(parent))
        self.setSalary.clicked.connect(lambda: self.on_set_salary(parent))

    def read_parent_values_and_update_ui(self, parent):
        old_rent_value = parent.status.get('daily_rent')
        old_salary_rate = parent.status.get('salary_rate')
        rate_type = parent.status.get('rate_over')

        self.ui.doubleSpinBox_changeRent.setValue(
            old_rent_value
        )
        self.ui.doubleSpinBox_changeSalary.setValue(
            old_salary_rate
        )
        self.radios.get(rate_type).setChecked(True)

    def manage_conditional_enabled_state(self, state, widgets):
        salary = [
            self.ui.doubleSpinBox_changeSalary,
            self.ui.pushButtonChangeSalary,
            self.ui.radioButton_fixed_rate,
            self.ui.radioButton_rate_over_proffit,
            self.ui.radioButton_rate_over_sales
        ]
        rent = [
            self.ui.doubleSpinBox_changeRent,
            self.ui.pushButtonChangeRent
        ]
        widgets_ = {'salary': salary, 'rent': rent}
        for i in widgets_.get(widgets):
            i.setEnabled(state)

    def adjust_limit_on_salary_rate(self):
        limits = {
            0: {'m': 0, 'M': 10 ** 6},
            1: {'m': 0, 'M': 100},
            2: {'m': 0, 'M': 100}
        }
        for key_, radio in enumerate(self.radios.values()):
            if radio.isChecked():
                limit = limits.get(key_)
                self.ui.doubleSpinBox_changeSalary.setMinimum(
                    limit.get('m')
                )
                self.ui.doubleSpinBox_changeSalary.setMaximum(
                    limit.get('M')
                )
                return
            continue

    def on_set_rent(self, parent):
        value = self.ui.doubleSpinBox_changeRent.value()
        old_value = parent.status.get('daily_rent')
        if value == old_value:
            return selfCloseInterface(
                'El valor actual ya estaba definido,', 4, 2, 'Valor Innecesario',
                'el valor que selecciono  <${:,.2f}>  ya estaba definido '
                'como valor de la renta.\nVerifique su entrada'.format(value)
            )
        parent.status.update({
            'daily_rent': value
        })
        selfCloseInterface(
            'Valor de la Renta modificado correctamente', 5, 1, 'Modificar Renta',
            '''antiguo valor: $ {:,.2f}\nnuevo valor:   $ {:,.2f}'''.format(old_value, value)
        )

    def on_set_salary(self, parent):
        old_rate_type = parent.status.get('rate_over')
        old_rate_value = parent.status.get('salary_rate')
        new_rate_type = next(
            filter(
                lambda i: i is not None,
                (key if radio.isChecked() else None for key, radio in enumerate(self.radios.values()))
            )
        )
        new_rate_value = self.ui.doubleSpinBox_changeSalary.value()
        if all([
            old_rate_value == new_rate_value,
            old_rate_type == new_rate_type
        ]):
            return selfCloseInterface(
                'El valor actual ya estaba definido,', 4, 2, 'Valor Innecesario',
                'el valor que selecciono  <${:,.2f}>  ya estaba definido en un mismo tipo '
                'como valor de la renta.\nVerifique su entrada'.format(new_rate_value)
            )
        parent.status.update({
            'salary_rate': new_rate_value, 'rate_over': new_rate_type
        })
        selfCloseInterface(
            'Valor del Salario modificado correctamente', 5, 1, 'Modificar Salario',
            '''nuevo valor: {} {}'''.format(
                new_rate_value,{
                    0: 'pesos de pago fijo',
                    1: 'porciento sobre las ventas',
                    2: 'porciento sobre las ganancias'
                }.get(new_rate_type)
            )
        )
