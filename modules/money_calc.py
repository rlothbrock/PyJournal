import locale
import math

locale.setlocale(locale.LC_MONETARY)


def multiply(self,
             result_container,
             amount_container,
             bill_value_container,
             exchange_rate=1,
             bill_value_container_is_text=True,
             result_emitter=None
             ):
    self.ui.checkBox_use_calculator.setChecked(False)  # this line deactivates the calculator
    self.ui.frame_calculator.setEnabled(False)
    amount = amount_container.value()
    bill_value = 0.0
    if bill_value_container_is_text:
        if '$' in bill_value_container.text():
            bill_value = float(bill_value_container.text().split('$')[1])
        if '$' not in bill_value_container.text():
            bill_value = float(bill_value_container.text())
    if not bill_value_container_is_text:
        if type(bill_value_container) is int or type(bill_value_container) is float:
            bill_value = bill_value_container
        if type(bill_value_container) is not int and type(bill_value_container) is not float:
            bill_value = bill_value_container.value()
    result = bill_value * exchange_rate * amount
    if result_emitter is not None:
        result_emitter.emit()
        result_container.setText(locale.format_string('$ %.2f', result, True, True))
    if not result_emitter:
        return result


def set_bill_calculator(self):
    # cuc to cuc column
    self.ui.pushButton_reset_calc.clicked.connect(lambda: reset_calc(self))
    self.ui.spinBox_cuc5cent.valueChanged.connect(
        lambda: multiply(self, self.ui.cuc5centsumlabel, self.ui.spinBox_cuc5cent, 0.05, 1, False,
                         self.value_changed_signal))
    self.ui.spinBox_cuc10cent.valueChanged.connect(
        lambda: multiply(self, self.ui.cuc10centsumlabel, self.ui.spinBox_cuc10cent, 0.1, 1, False,
                         self.value_changed_signal))
    self.ui.spinBox_cuc25cent.valueChanged.connect(
        lambda: multiply(self, self.ui.cuc25centsumlabel, self.ui.spinBox_cuc25cent, 0.25, 1, False,
                         self.value_changed_signal))
    self.ui.spinBox_cuc50cent.valueChanged.connect(
        lambda: multiply(self, self.ui.cuc50centsumlabel, self.ui.spinBox_cuc50cent, 0.5, 1, False,
                         self.value_changed_signal))
    self.ui.spinBox_cuc1.valueChanged.connect(
        lambda: multiply(self, self.ui.cuc1sumlabel, self.ui.spinBox_cuc1, 1, 1, False, self.value_changed_signal))
    self.ui.spinBox_cuc3.valueChanged.connect(
        lambda: multiply(self, self.ui.cuc3sumlabel, self.ui.spinBox_cuc3, 3, 1, False, self.value_changed_signal))
    self.ui.spinBox_cuc5.valueChanged.connect(
        lambda: multiply(self, self.ui.cuc5sumlabel, self.ui.spinBox_cuc5, 5, 1, False, self.value_changed_signal))
    self.ui.spinBox_cuc10.valueChanged.connect(
        lambda: multiply(self, self.ui.cuc10sumlabel, self.ui.spinBox_cuc10, 10, 1, False, self.value_changed_signal))
    self.ui.spinBox_cuc20.valueChanged.connect(
        lambda: multiply(self, self.ui.cuc20sumlabel, self.ui.spinBox_cuc20, 20, 1, False, self.value_changed_signal))
    self.ui.spinBox_cuc50.valueChanged.connect(
        lambda: multiply(self, self.ui.cuc50sumlabel, self.ui.spinBox_cuc50, 50, 1, False, self.value_changed_signal))
    self.ui.spinBox_cuc100.valueChanged.connect(
        lambda: multiply(self, self.ui.cuc100sumlabel, self.ui.spinBox_cuc100, 100, 1, False,
                         self.value_changed_signal))

    # cuc to cup column
    self.ui.spinBox_cuc5cent.valueChanged.connect(
        lambda: multiply(self, self.ui.cucTocup5centlabel, self.ui.spinBox_cuc5cent, 0.05, 24, False,
                         self.value_changed_signal))
    self.ui.spinBox_cuc10cent.valueChanged.connect(
        lambda: multiply(self, self.ui.cucTocup10centlabel, self.ui.spinBox_cuc10cent, 0.1, 24, False,
                         self.value_changed_signal))
    self.ui.spinBox_cuc25cent.valueChanged.connect(
        lambda: multiply(self, self.ui.cucTocup25centlabel, self.ui.spinBox_cuc25cent, 0.25, 24, False,
                         self.value_changed_signal))
    self.ui.spinBox_cuc50cent.valueChanged.connect(
        lambda: multiply(self, self.ui.cucTocup50centlabel, self.ui.spinBox_cuc50cent, 0.5, 24, False,
                         self.value_changed_signal))
    self.ui.spinBox_cuc1.valueChanged.connect(
        lambda: multiply(self, self.ui.cucTocup1label, self.ui.spinBox_cuc1, 1, 24, False, self.value_changed_signal))
    self.ui.spinBox_cuc3.valueChanged.connect(
        lambda: multiply(self, self.ui.cucTocup3label, self.ui.spinBox_cuc3, 3, 24, False, self.value_changed_signal))
    self.ui.spinBox_cuc5.valueChanged.connect(
        lambda: multiply(self, self.ui.cucTocup5label, self.ui.spinBox_cuc5, 5, 24, False, self.value_changed_signal))
    self.ui.spinBox_cuc10.valueChanged.connect(
        lambda: multiply(self, self.ui.cucTocup10label, self.ui.spinBox_cuc10, 10, 24, False,
                         self.value_changed_signal))
    self.ui.spinBox_cuc20.valueChanged.connect(
        lambda: multiply(self, self.ui.cucTocup20label, self.ui.spinBox_cuc20, 20, 24, False,
                         self.value_changed_signal))
    self.ui.spinBox_cuc50.valueChanged.connect(
        lambda: multiply(self, self.ui.cucTocup50label, self.ui.spinBox_cuc50, 50, 24, False,
                         self.value_changed_signal))
    self.ui.spinBox_cuc100.valueChanged.connect(
        lambda: multiply(self, self.ui.cucTocup100label, self.ui.spinBox_cuc100, 100, 24, False,
                         self.value_changed_signal))

    # cup to cup column
    self.ui.spinBox_cup1.valueChanged.connect(
        lambda: multiply(self, self.ui.label_cup1, self.ui.spinBox_cup1, 1, 1, False, self.value_changed_signal))
    self.ui.spinBox_cup3.valueChanged.connect(
        lambda: multiply(self, self.ui.label_cup3, self.ui.spinBox_cup3, 3, 1, False, self.value_changed_signal))
    self.ui.spinBox_cup5.valueChanged.connect(
        lambda: multiply(self, self.ui.label_cup5, self.ui.spinBox_cup5, 5, 1, False, self.value_changed_signal))
    self.ui.spinBox_cup10.valueChanged.connect(
        lambda: multiply(self, self.ui.label_cup10, self.ui.spinBox_cup10, 10, 1, False, self.value_changed_signal))
    self.ui.spinBox_cup20.valueChanged.connect(
        lambda: multiply(self, self.ui.label_cup20, self.ui.spinBox_cup20, 20, 1, False, self.value_changed_signal))
    self.ui.spinBox_cup50.valueChanged.connect(
        lambda: multiply(self, self.ui.label_cup50, self.ui.spinBox_cup50, 50, 1, False, self.value_changed_signal))
    self.ui.spinBox_cup100.valueChanged.connect(
        lambda: multiply(self, self.ui.label_cup100, self.ui.spinBox_cup100, 100, 1, False, self.value_changed_signal))
    self.ui.spinBox_cup200.valueChanged.connect(
        lambda: multiply(self, self.ui.label_cup200, self.ui.spinBox_cup200, 200, 1, False, self.value_changed_signal))
    self.ui.spinBox_cup500.valueChanged.connect(
        lambda: multiply(self, self.ui.label_cup500, self.ui.spinBox_cup500, 500, 1, False, self.value_changed_signal))
    self.ui.spinBox_cup1000.valueChanged.connect(
        lambda: multiply(self, self.ui.label_cup1000, self.ui.spinBox_cup1000, 1000, 1, False,
                         self.value_changed_signal))
    self.ui.doubleSpinBox_dineroEsperado.valueChanged.connect(lambda: show_totals(self))
    self.value_changed_signal.connect(lambda: show_totals(self))
    self.ui.checkBox_use_calculator.clicked.connect(
        lambda: self.ui.frame_calculator.setEnabled(self.ui.checkBox_use_calculator.isChecked())
    )


def show_totals(self):
    cuc_parcial = sum([
        multiply(self, self.ui.cuc5centsumlabel, self.ui.spinBox_cuc5cent, 0.05, 1, False),
        multiply(self, self.ui.cuc10centsumlabel, self.ui.spinBox_cuc10cent, 0.1, 1, False),
        multiply(self, self.ui.cuc25centsumlabel, self.ui.spinBox_cuc25cent, 0.25, 1, False),
        multiply(self, self.ui.cuc50centsumlabel, self.ui.spinBox_cuc50cent, 0.5, 1, False),
        multiply(self, self.ui.cuc1sumlabel, self.ui.spinBox_cuc1, 1, 1, False),
        multiply(self, self.ui.cuc3sumlabel, self.ui.spinBox_cuc3, 3, 1, False),
        multiply(self, self.ui.cuc5sumlabel, self.ui.spinBox_cuc5, 5, 1, False),
        multiply(self, self.ui.cuc10sumlabel, self.ui.spinBox_cuc10, 10, 1, False),
        multiply(self, self.ui.cuc20sumlabel, self.ui.spinBox_cuc20, 20, 1, False),
        multiply(self, self.ui.cuc50sumlabel, self.ui.spinBox_cuc50, 50, 1, False),
        multiply(self, self.ui.cuc100sumlabel, self.ui.spinBox_cuc100, 100, 1, False)
    ])
    cuc_convertido = sum([
        multiply(self, self.ui.cucTocup5centlabel, self.ui.spinBox_cuc5cent, 0.05, 24, False),
        multiply(self, self.ui.cucTocup10centlabel, self.ui.spinBox_cuc10cent, 0.1, 24, False),
        multiply(self, self.ui.cucTocup25centlabel, self.ui.spinBox_cuc25cent, 0.25, 24, False),
        multiply(self, self.ui.cucTocup50centlabel, self.ui.spinBox_cuc50cent, 0.5, 24, False),
        multiply(self, self.ui.cucTocup1label, self.ui.spinBox_cuc1, 1, 24, False),
        multiply(self, self.ui.cucTocup3label, self.ui.spinBox_cuc3, 3, 24, False),
        multiply(self, self.ui.cucTocup5label, self.ui.spinBox_cuc5, 5, 24, False),
        multiply(self, self.ui.cucTocup10label, self.ui.spinBox_cuc10, 10, 24, False),
        multiply(self, self.ui.cucTocup20label, self.ui.spinBox_cuc20, 20, 24, False),
        multiply(self, self.ui.cucTocup50label, self.ui.spinBox_cuc50, 50, 24, False),
        multiply(self, self.ui.cucTocup100label, self.ui.spinBox_cuc100, 100, 24, False)
    ])
    cup_parcial = sum([
        multiply(self, self.ui.label_cup1, self.ui.spinBox_cup1, 1, 1, False),
        multiply(self, self.ui.label_cup3, self.ui.spinBox_cup3, 3, 1, False),
        multiply(self, self.ui.label_cup5, self.ui.spinBox_cup5, 5, 1, False),
        multiply(self, self.ui.label_cup10, self.ui.spinBox_cup10, 10, 1, False),
        multiply(self, self.ui.label_cup20, self.ui.spinBox_cup20, 20, 1, False),
        multiply(self, self.ui.label_cup50, self.ui.spinBox_cup50, 50, 1, False),
        multiply(self, self.ui.label_cup100, self.ui.spinBox_cup100, 100, 1, False),
        multiply(self, self.ui.label_cup200, self.ui.spinBox_cup200, 200, 1, False),
        multiply(self, self.ui.label_cup500, self.ui.spinBox_cup500, 500, 1, False),
        multiply(self, self.ui.label_cup1000, self.ui.spinBox_cup1000, 1000, 1, False)
    ])
    total = sum([cuc_convertido, cup_parcial])
    esperado = self.ui.doubleSpinBox_dineroEsperado.value()
    diferencia = 0
    palabra = ''
    if math.fabs(total - esperado) >= 0.01:
        palabra = 'sobra' if total > esperado else 'falta'
        diferencia = (total - esperado) if total > esperado else (esperado - total)
    # -----------------
    self.ui.label_montoCUCparcial.setText(locale.format_string('$ %.2f', cuc_parcial, True, True))
    self.ui.label_montoCUCconvertido.setText(locale.format_string('$ %.2f', cuc_convertido, True, True))
    self.ui.label_montoCUPparcial.setText(locale.format_string('$ %.2f', cup_parcial, True, True))
    self.ui.label_monto_total_calculator.setText(locale.format_string('$ %.2f', total, True, True))
    self.ui.label_sobra_falta_palabra.setText(palabra)
    self.ui.label_sobra_falta_cantidad.setText(locale.format_string('%.2f', diferencia, True, True))


def reset_calc(self):
    reset_text = '$ 0.00'
    self.operation = ''

    self.ui.spinBox_cup1.setValue(0)
    self.ui.spinBox_cup3.setValue(0)
    self.ui.spinBox_cup5.setValue(0)
    self.ui.spinBox_cup10.setValue(0)
    self.ui.spinBox_cup20.setValue(0)
    self.ui.spinBox_cup50.setValue(0)
    self.ui.spinBox_cup100.setValue(0)
    self.ui.spinBox_cup200.setValue(0)
    self.ui.spinBox_cup500.setValue(0)
    self.ui.spinBox_cup1000.setValue(0)

    self.ui.spinBox_cuc5cent.setValue(0)
    self.ui.spinBox_cuc10cent.setValue(0)
    self.ui.spinBox_cuc25cent.setValue(0)
    self.ui.spinBox_cuc50cent.setValue(0)
    self.ui.spinBox_cuc1.setValue(0)
    self.ui.spinBox_cuc3.setValue(0)
    self.ui.spinBox_cuc5.setValue(0)
    self.ui.spinBox_cuc10.setValue(0)
    self.ui.spinBox_cuc20.setValue(0)
    self.ui.spinBox_cuc50.setValue(0)
    self.ui.spinBox_cuc100.setValue(0)

    self.ui.doubleSpinBox_dineroEsperado.setValue(0)

    self.ui.label_cup1.setText(reset_text)
    self.ui.label_cup3.setText(reset_text)
    self.ui.label_cup5.setText(reset_text)
    self.ui.label_cup10.setText(reset_text)
    self.ui.label_cup20.setText(reset_text)
    self.ui.label_cup50.setText(reset_text)
    self.ui.label_cup100.setText(reset_text)
    self.ui.label_cup200.setText(reset_text)
    self.ui.label_cup500.setText(reset_text)
    self.ui.label_cup1000.setText(reset_text)

    self.ui.cuc5centsumlabel.setText(reset_text)
    self.ui.cuc10centsumlabel.setText(reset_text)
    self.ui.cuc25centsumlabel.setText(reset_text)
    self.ui.cuc50centsumlabel.setText(reset_text)
    self.ui.cuc1sumlabel.setText(reset_text)
    self.ui.cuc3sumlabel.setText(reset_text)
    self.ui.cuc5sumlabel.setText(reset_text)
    self.ui.cuc10sumlabel.setText(reset_text)
    self.ui.cuc20sumlabel.setText(reset_text)
    self.ui.cuc50sumlabel.setText(reset_text)
    self.ui.cuc100sumlabel.setText(reset_text)

    self.ui.cucTocup5centlabel.setText(reset_text)
    self.ui.cucTocup10centlabel.setText(reset_text)
    self.ui.cucTocup25centlabel.setText(reset_text)
    self.ui.cucTocup50centlabel.setText(reset_text)
    self.ui.cucTocup1label.setText(reset_text)
    self.ui.cucTocup3label.setText(reset_text)
    self.ui.cucTocup5label.setText(reset_text)
    self.ui.cucTocup10label.setText(reset_text)
    self.ui.cucTocup20label.setText(reset_text)
    self.ui.cucTocup50label.setText(reset_text)
    self.ui.cucTocup100label.setText(reset_text)

    self.ui.label_monto_total_calculator.setText(reset_text)
    self.ui.label_montoCUCconvertido.setText(reset_text)
    self.ui.label_montoCUCparcial.setText(reset_text)
    self.ui.label_montoCUPparcial.setText(reset_text)
