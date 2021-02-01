from PySide2.QtWidgets import QDialog, QDialogButtonBox
from UI.purchases_form import Ui_Dialog_purchases_form
from dialogs.auxiliar_dialogs import selfCloseInterface, MessageBox
from dialogs.common_tool_dialogs import build_data_template, build_item_code, buddy_sync
from modules.crud_sqlite import crud_driver
from modules.db_templates_manager import get_template_fields, get_index_in_template


class PurchasesFormDialog(QDialog):
    def __init__(self, parent):
        super(PurchasesFormDialog, self).__init__(parent)
        self.ui = Ui_Dialog_purchases_form()
        self.ui.setupUi(self)

        # buttons
        self.combo_data = []
        self.closeButton = self.ui.buttonBox.button(QDialogButtonBox.Close)
        self.applyButton = self.ui.buttonBox.button(QDialogButtonBox.Apply)
        self.resetButton = self.ui.buttonBox.button(QDialogButtonBox.Reset)

        # behavior of buttons
        self.applyButton.clicked.connect(lambda: self.accept_routine(parent))
        self.closeButton.clicked.connect(self.reject_routine)

        #
        self.init_ui(parent)

    def accept_routine(self, parent):
        # props alias...
        data_len__ = get_template_fields('diary')
        date__ = get_index_in_template('diary', 'date')
        is_new__ = get_index_in_template('diary', 'is_new')
        is_sale__ = get_index_in_template('diary', 'is_sale')
        is_consignation__ = get_index_in_template('diary', 'is_consignation')
        quantity__ = get_index_in_template('diary', 'quantity')
        item_name__ = get_index_in_template('diary', 'item_name')
        price__ = get_index_in_template('diary', 'price')
        sell_price__ = get_index_in_template('diary', 'sell_price')
        comments__ = get_index_in_template('diary', 'comments')
        item_code__ = get_index_in_template('diary', 'item_code')

        # --
        invested__ = get_index_in_template('diary', 'invested_')
        cash__ = get_index_in_template('diary', 'cash_')
        total__ = get_index_in_template('diary', 'total_')
        parts__ = [get_index_in_template('diary', 'robert_'), get_index_in_template('diary', 'ariadna_')]

        last_row_data__ = crud_driver(parent, 'diary', 'read', {})
        last_row_data = build_data_template() if len(last_row_data__) == 0 else last_row_data__[-1]
        last_row_data = build_data_template() if len(data_len__) > len(last_row_data) else last_row_data
        data = build_data_template()

        # this block  is for preventing purchases with no cash
        if last_row_data[cash__] <= 0:
            selfCloseInterface(
                'No esta permitido comprar cuando el saldo de caja es cero, agregue saldo a su caja antes de hacer esta operacion',
                8, 3, 'Compras Denegadas: SIN EFECTIVO',
                'Vaya a:\nMenu Herramientas > Modificar la Inversion\nO presione: CTRL+ALT+M \ny agregue efectivo antes de comprar')
            self.reject()
            parent.ui.actionModificar_la_inversion.trigger()
            return

        data[date__] = parent.date_session
        data[is_new__] = self.ui.nuevoItemPurchaseCheckBox.isChecked()
        data[is_sale__] = False
        data[is_consignation__] = self.ui.itemAConsignacionCheckBox.isChecked()
        data[quantity__] = self.ui.totalDeItemsCompradosSpinBox.value()
        data[item_name__] = self.ui.nombreDelItemIncrementadoComboBox.currentText() \
            if not data[is_new__] else self.ui.nombreDelItemCompradoLineEdit.text()
        data[price__] = (self.ui.precioTotalPagadoPorLaCompraDoubleSpinBox.value() / data[quantity__]) \
            if data[is_new__] else self.ui.precioTotalPagadoPorLaCompraDoubleSpinBox.value()

        if any([len(data[item_name__]) < 3, data[price__] == 0]):
            selfCloseInterface(
                'Los datos son incorrectos. Revise la informacion antes de realizar una entrada',
                8, 2, 'Entrada Fallida: DATOS INCORRECTOS',
                'REVISE:\n1- Que el precio no sea cero\n2- Que el articulo tenga un nombre apropiado (mas de 3 letras)'
            )
            return
        data[sell_price__] = 0
        data[comments__] = self.ui.comentariosDeEntradaLineEdit.text()
        data[item_code__] = self.ui.codigoDelItemIncrementadoComboBox.currentText() \
            if not data[is_new__] else build_item_code(data[price__],self.ui.itemAConsignacionCheckBox.isChecked())

        # capital cells # touches invested
        data[parts__[0]] = last_row_data[parts__[0]]
        data[parts__[1]] = last_row_data[parts__[1]]
        data[total__] = float(last_row_data[total__])

        data[invested__] = float(last_row_data[invested__]) if data[is_consignation__] else\
            float(last_row_data[invested__]) + data[quantity__] * data[price__]

        data[cash__] = data[total__] - data[invested__]

        # this block prevents for goes negative funds after purchasing something
        if data[cash__] < 0:
            selfCloseInterface(
                'No esta permitido comprar cuando el monto es mayor que el saldo de caja, agregue saldo a su caja antes de hacer esta operacion',
                8, 3, 'Compras Denegadas: CAPACIDAD EXCEDIDA',
                'Vaya a:\nMenu Herramientas > Modificar la Inversion\nO presione: CTRL+ALT+M \ny agregue efectivo antes de comprar\n\nO reduzca la cantidad de articulos comprados')
            self.reject()
            return

        # this is the secure entry block
        msg_str = 'comprar {} {} por ${:,.2f} cada uno'.format(data[quantity__], data[item_name__], data[price__])
        if parent.use_secure_entry:
            confirm = MessageBox(
                lambda: parent.append_data_to_diary(data),
                'Desea confirmar la Entrada?', 'q', 'Confirmar Entrada', msg_str
            )
            confirm.show()
        else:
            parent.append_data_to_diary(data)
            selfCloseInterface(msg_str, 4, 1, 'Operacion Realizada',
                               'Cambios Insertados en la Base de Datos')

        self.init_ui(parent)
        return

    def reject_routine(self):
        self.clean_form()
        self.reject()

    def clean_form(self):
        self.ui.itemAConsignacionCheckBox.setChecked(False)
        self.ui.nuevoItemPurchaseCheckBox.setChecked(False)
        self.ui.nombreDelItemCompradoLabel.setEnabled(False)
        self.ui.nombreDelItemCompradoLineEdit.setEnabled(False)
        self.ui.nombreDelItemIncrementadoLabel.setEnabled(True)
        self.ui.nombreDelItemIncrementadoComboBox.setEnabled(True)
        self.ui.codigoDelItemIncrementadoLabel.setEnabled(True)
        self.ui.codigoDelItemIncrementadoComboBox.setEnabled(True)
        self.ui.totalDeItemsCompradosSpinBox.setValue(1)
        self.ui.precioTotalPagadoPorLaCompraDoubleSpinBox.setValue(0)
        self.ui.comentariosDeEntradaLineEdit.clear()

    def init_ui(self, parent):
        self.data_loader(parent)
        self.ui.nuevoItemPurchaseCheckBox.stateChanged.connect(self.field_disabler_on_new_items)
        self.ui.nombreDelItemIncrementadoComboBox.currentIndexChanged.connect(
            lambda: buddy_sync(
                self.ui.nombreDelItemIncrementadoComboBox,
                self.ui.codigoDelItemIncrementadoComboBox,
                self.ui.precioTotalPagadoPorLaCompraDoubleSpinBox,
                self.combo_data[self.ui.nombreDelItemIncrementadoComboBox.currentIndex()][2])
        )
        self.ui.nombreDelItemIncrementadoComboBox.currentIndexChanged.connect(
            lambda: buddy_sync(
                self.ui.nombreDelItemIncrementadoComboBox,
                None,
                self.ui.nombreDelItemCompradoLineEdit,
                self.ui.nombreDelItemIncrementadoComboBox.currentText(), True,
                not self.ui.nuevoItemPurchaseCheckBox.isChecked()
            )
        )
        self.ui.codigoDelItemIncrementadoComboBox.currentIndexChanged.connect(
            lambda: buddy_sync(
                self.ui.codigoDelItemIncrementadoComboBox,
                self.ui.nombreDelItemIncrementadoComboBox,
                self.ui.precioTotalPagadoPorLaCompraDoubleSpinBox,
                self.combo_data[self.ui.nombreDelItemIncrementadoComboBox.currentIndex()][2]
            )
        )

    def data_loader(self, parent):
        self.combo_data.clear()
        self.combo_data.extend(
            crud_driver(parent, 'stock', 'read', {
                'pick_all': False,
                'pick_cols': ['item_code', 'item_name', 'price'],
            }))
        self.ui.codigoDelItemIncrementadoComboBox.clear()
        self.ui.codigoDelItemIncrementadoComboBox.addItems(
            list((r[0] for r in self.combo_data))
        )
        self.ui.nombreDelItemIncrementadoComboBox.clear()
        self.ui.nombreDelItemIncrementadoComboBox.addItems(
            list((r[1] for r in self.combo_data))
        )

    def field_disabler_on_new_items(self):
        x = self.ui.nuevoItemPurchaseCheckBox.isChecked()
        self.ui.nombreDelItemCompradoLabel.setEnabled(x)
        self.ui.nombreDelItemCompradoLineEdit.setEnabled(x)
        self.ui.codigoDelItemIncrementadoLabel.setEnabled(not x)
        self.ui.codigoDelItemIncrementadoComboBox.setEnabled(not x)
        self.ui.nombreDelItemIncrementadoLabel.setEnabled(not x)
        self.ui.nombreDelItemIncrementadoComboBox.setEnabled(not x)
        self.ui.precioTotalPagadoPorLaCompraLabel.setEnabled(x)
        self.ui.precioTotalPagadoPorLaCompraDoubleSpinBox.setEnabled(x)
        # reset on checks
        self.ui.nombreDelItemIncrementadoComboBox.setCurrentIndex(0)
        return
