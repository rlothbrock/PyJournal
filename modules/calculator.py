event_keys = {
    '48': '0',
    '49': '1',
    '50': '2',
    '51': '3',
    '52': '4',
    '53': '5',
    '54': '6',
    '55': '7',
    '56': '8',
    '57': '9',
    '46': '.',
    '43': ' + ',
    '45': ' - ',
    '42': ' * ',
    '47': ' / ',
    '61': '=',
    '16777221': 'ENTER',
    '16777220': 'ENTER',
    '16777219': 'BACKSPACE',
    '16777223': 'DELETE'
}

codes = list(event_keys.keys())
symbols = list(event_keys.values())


def set_calculator(self):
    print('loading calculator module... done')
    self.ui.label_calc_result.setText('0')
    self.ui.label_calc_operation.setText('0')
    self.ui.pushButton_calc_0.clicked.connect(lambda: operation_builder(self, '0'))
    self.ui.pushButton_calc_1.clicked.connect(lambda: operation_builder(self, '1'))
    self.ui.pushButton_calc_2.clicked.connect(lambda: operation_builder(self, '2'))
    self.ui.pushButton_calc_3.clicked.connect(lambda: operation_builder(self, '3'))
    self.ui.pushButton_calc_4.clicked.connect(lambda: operation_builder(self, '4'))
    self.ui.pushButton_calc_5.clicked.connect(lambda: operation_builder(self, '5'))
    self.ui.pushButton_calc_6.clicked.connect(lambda: operation_builder(self, '6'))
    self.ui.pushButton_calc_7.clicked.connect(lambda: operation_builder(self, '7'))
    self.ui.pushButton_calc_8.clicked.connect(lambda: operation_builder(self, '8'))
    self.ui.pushButton_calc_9.clicked.connect(lambda: operation_builder(self, '9'))
    self.ui.pushButton_calc_cents.clicked.connect(lambda: operation_builder(self, '.00'))
    self.ui.pushButton_calc_float.clicked.connect(lambda: operation_builder(self, '.'))
    self.ui.pushButton_calc_plus.clicked.connect(lambda: operation_builder(self, ' + '))
    self.ui.pushButton_calc_minus.clicked.connect(lambda: operation_builder(self, ' - '))
    self.ui.pushButton_calc_multiply.clicked.connect(lambda: operation_builder(self, ' * '))
    self.ui.pushButton_calc_divide.clicked.connect(lambda: operation_builder(self, ' / '))
    self.ui.pushButton_calc_equal.clicked.connect(lambda: operation_resolver(self))
    self.ui.pushButton_calc_delete.clicked.connect(lambda: operation_delete_last_character(self))
    self.ui.pushButton_calc_clear.clicked.connect(lambda: operation_clearer(self))
    self.key_pressed_signal.connect(lambda code: key_react_calculator(self, code))


def operation_builder(self, modifier: str):
    self.operation += modifier
    print(self.operation)
    self.ui.label_calc_operation.setText(self.operation)
    try:
        if self.operation == '':
            self.ui.label_calc_result.setText(str(0))
            return
        if self.operation[-2] in ['+', '-']:
            partial_result = eval('%s 0 ' % self.operation)
            self.ui.label_calc_result.setText(str(partial_result))
            return
        if self.operation[-2] in ['*', '/']:
            partial_result = eval('%s 1 ' % self.operation)
            self.ui.label_calc_result.setText(str(partial_result))
            return
        partial_result = eval(self.operation)
        self.ui.label_calc_result.setText(str(partial_result))
        return
    except:
        return


def operation_clearer(self):
    self.ui.label_calc_result.setText(str(0))
    self.ui.label_calc_operation.setText(str(0))
    self.operation = ''
    return


def operation_resolver(self):
    print('operation to eval: ', self.operation)
    result = eval(self.operation)
    print(result)
    self.ui.label_calc_result.setText(str(result))
    self.ui.doubleSpinBox_dineroEsperado.setValue(result)  # this line trigger multiply --> deactivates the calc
    operation_clearer(self)


def operation_delete_last_character(self):
    oper = self.operation[:-1]
    self.operation = oper
    # self.ui.label_calc_operation.setText(oper)
    return operation_builder(self, '')


def key_react_calculator(self, code):
    print('code is: ', code)
    if not self.ui.checkBox_use_calculator.isChecked():
        return
    symbol = symbol_translator(code)
    print('symbol is {}: {}'.format(symbol, type(symbol)))
    if symbol in ['=', 'ENTER', 'DELETE', 'BACKSPACE']:
        if symbol == '=':
            return key_react(lambda: operation_resolver(self))
        if symbol == 'ENTER':
            return key_react(lambda: operation_resolver(self))
        if symbol == 'DELETE':
            return key_react(lambda: operation_clearer(self))
        if symbol == 'BACKSPACE':
            return key_react(lambda: operation_delete_last_character(self))

    if symbol in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' / ', ' + ', ' - ', ' * ', '.']:
        return key_react(lambda: operation_builder(self, symbol))


def code_translator(value: str):
    # takes the symbol of the button, and returns the belonging key
    return int(codes[symbols.index(value)]) if value in symbols else None


def symbol_translator(value: int):
    # takes the key and returns the symbol
    # debug print('{}: {}'.format(symbols[codes.index(str(value))],type(symbols[codes.index(str(value))])))
    return symbols[codes.index(str(value))] if str(value) in codes else None


def key_react(reaction, condition=True):
    if not condition:  # self.ui.checkBox_use_calculator.isChecked() for calculator
        return
    return reaction()
