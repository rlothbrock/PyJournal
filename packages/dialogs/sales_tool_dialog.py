from PySide2.QtWidgets import QDialog, QDialogButtonBox

from packages.UI.sales_form import Ui_Dialog_sales_form
from packages.dialogs.auxiliar_dialogs import selfCloseInterface, MessageBox
from packages.dialogs.common_tool_dialogs import build_data_template, build_salary, buddy_sync
from packages.modules.crud_sqlite import crud_driver
from packages.modules.db_templates_manager import get_template_fields, get_index_in_template


class SalesFormDialog(QDialog):
    def __init__(self, parent):
        super(SalesFormDialog, self).__init__(parent)
        self.ui = Ui_Dialog_sales_form()
        self.ui.setupUi(self)

        self.combo_data = []
        self.closeButton = self.ui.buttonBox.button(QDialogButtonBox.Close)
        self.applyButton = self.ui.buttonBox.button(QDialogButtonBox.Apply)
        self.resetButton = self.ui.buttonBox.button(QDialogButtonBox.Reset)

        self.applyButton.clicked.connect(lambda: self.apply_routine(parent))
        self.closeButton.clicked.connect(self.cancel_routine)
        self.resetButton.clicked.connect(lambda: self.clean_form(parent))
        self.init_ui(parent)
        # ----

    def apply_routine(self, parent):

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
        salary__ = get_index_in_template('diary', 'salary')
        invested__ = get_index_in_template('diary', 'invested_')
        cash__ = get_index_in_template('diary', 'cash_')
        total__ = get_index_in_template('diary', 'total_')
        parts__ = [get_index_in_template('diary', 'robert_'), get_index_in_template('diary', 'ariadna_')]

        last_row_data__ = crud_driver(parent, 'diary', 'read', {})
        last_row_data = build_data_template() if len(last_row_data__) == 0 else last_row_data__[-1]
        last_row_data = build_data_template() if len(data_len__) > len(last_row_data) else last_row_data
        data = build_data_template()

        # this block  is for preventing sales form to be submitted with  invalid data
        # protect against zero items sale
        if self.ui.cantidadVendidaComboBox.currentIndex() == 0:
            selfCloseInterface(
                'No esta permitido vender "cero" {},defina una cantidad adecuada antes de hacer la operacion'.format(
                    self.ui.nombreDelProductoComboBox.currentText()),
                8, 3, 'Venta Denegada: CANTIDAD INCORRECTA',
                'la menor cantidad admitida es 1, si no puede, significa que el producto se ha agotado')
            self.init_ui(parent)  # init ui for clean zero items...
            return
            # protect against low price sales
        minimum_sell_price = self.ui.cantidadVendidaComboBox.currentIndex() * float(
            self.combo_data[self.ui.codigoDelProductoComboBox.currentIndex()][3])
        if self.ui.precioDeVentaDoubleSpinBox.value() < minimum_sell_price:
            low_price_switch = {'switch': False}
            low_price_warn = MessageBox(
                lambda: low_price_switch.update({'switch': True}),
                'Esta seguro de que desea vender {} {} por ${:,.2f} ??'
                '\nel precio minimo para esta cantidad es ${:,.2f}.'
                '\nSi realiza la venta a este precio ocasiona perdidas !!'.format(
                    self.ui.cantidadVendidaComboBox.currentText(),
                    self.ui.nombreDelProductoComboBox.currentText(),
                    self.ui.precioDeVentaDoubleSpinBox.value(), minimum_sell_price
                ), 'w',
                'Advertencia: Venta por debajo del precio de costo',
                '\n\n Esta accion es intencional y desea continuar??'
            )
            low_price_warn.show()
            if not low_price_switch.get('switch'):
                return
                # protect against sale more than on_stock
        on_stock__ = int(crud_driver(parent, 'stock', 'read', {
            'field': 'item_code',
            'operator': '=',
            'value': (self.ui.codigoDelProductoComboBox.currentText(),)
        })[0][get_index_in_template('stock', 'on_stock')])
        if on_stock__ < 1:
            selfCloseInterface(
                'El producto {} no existe en el inventario en este momento,'
                'revise el nombre del producto antes de hacer la operacion'.format(
                    self.ui.nombreDelProductoComboBox.currentText()),
                8, 3, 'Venta Denegada: PRODUCTO NO EXISTE',
                'Es muy probable que el producto se haya agotado en la ultima entrada. Verifique el nombre otra vez')
            self.init_ui(parent)  # init ui for clean zero items...
            return

        data[date__] = parent.date_session
        data[is_new__] = False
        data[is_sale__] = True
        data[is_consignation__] = self.ui.codigoDelProductoComboBox.currentText()[0] == 'c'
        data[quantity__] = self.ui.cantidadVendidaComboBox.currentIndex()
        data[item_name__] = self.ui.nombreDelProductoComboBox.currentText()
        data[price__] = minimum_sell_price
        data[sell_price__] = self.ui.precioDeVentaDoubleSpinBox.value()
        data[comments__] = self.ui.comentariosLineEdit.text()
        data[item_code__] = self.ui.codigoDelProductoComboBox.currentText()
        data[salary__] = build_salary(parent,data[sell_price__],minimum_sell_price)
        # capital cells # touches invested
        data[parts__[0]] = last_row_data[parts__[0]]
        data[parts__[1]] = last_row_data[parts__[1]]
        data[total__] = float(last_row_data[total__])

        data[invested__] = float(last_row_data[invested__]) if \
            data[is_consignation__] else (float(last_row_data[invested__]) - data[price__])

        data[cash__] = data[total__] - data[invested__]

        # this is the secure entry block
        msg_str = 'vender {} {} por ${:,.2f}'.format(data[quantity__], data[item_name__], data[sell_price__])
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

    def cancel_routine(self):
        self.clean_form(kill=True)
        self.reject()

    def clean_form(self, parent=None, kill=False):
        self.ui.comentariosLineEdit.clear()
        self.ui.precioDeVentaDoubleSpinBox.clear()
        if not kill:
            self.data_loader(parent)
            self.combo_filler()
            self.quantity_combo_filler()
        return

    def init_ui(self, parent):
        self.data_loader(parent)
        self.combo_filler()
        self.quantity_combo_filler()
        self.ui.nombreDelProductoComboBox.currentIndexChanged.connect(
            lambda: buddy_sync(
                self.ui.nombreDelProductoComboBox,
                self.ui.codigoDelProductoComboBox,
            )
        )
        self.ui.codigoDelProductoComboBox.currentIndexChanged.connect(
            lambda: buddy_sync(
                self.ui.codigoDelProductoComboBox,
                self.ui.nombreDelProductoComboBox,
            )
        )
        self.ui.nombreDelProductoComboBox.currentIndexChanged.connect(
            self.quantity_combo_filler
        )
        self.ui.codigoDelProductoComboBox.currentIndexChanged.connect(
            self.quantity_combo_filler
        )

    def data_loader(self, parent):
        self.combo_data.clear()
        self.combo_data.extend(
            crud_driver(parent, 'stock', 'read', {
                'pick_all': False,
                'pick_cols': ['item_code', 'item_name', 'on_stock', 'price'],
                'field': 'on_stock',
                'operator': '>=',
                'sort': True,
                'order_by': ['item_name'],
                'order_': ['ASC'],
                'value': (1,)
            }))

    def combo_filler(self):
        self.ui.nombreDelProductoComboBox.clear()
        self.ui.nombreDelProductoComboBox.addItems(
            list((t[1] for t in self.combo_data))
        )
        self.ui.codigoDelProductoComboBox.clear()
        self.ui.codigoDelProductoComboBox.addItems(
            list((t[0] for t in self.combo_data))
        )
        return

    def quantity_combo_filler(self):
        i = self.ui.codigoDelProductoComboBox.currentIndex()
        self.ui.cantidadVendidaComboBox.clear()
        self.ui.cantidadVendidaComboBox.addItems(
            list((str(n) for n in range(int(self.combo_data[i][2]) + 1)))
        )
        return

