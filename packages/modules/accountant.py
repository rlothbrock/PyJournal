# this module handles the auxiliar tables (sales, stock, statistics, )
from packages.modules.crud_sqlite import crud_driver
from packages.modules.db_templates_manager import \
    get_index_in_template as g_i, get_template_fields, get_index_in_template, \
    on_diary_table_find_index_and_fields_of


def calculate_auxiliar_tabs(self):
    # print('recalculating auxiliar tables...')
    calculate_sales(self)
    calculate_stock(self)
    calculate_capital(self)
    # calculate_statistics(self) : this one is only called on index 2 activated
    return


def calculate_sales(self):
    try:
        diary_data_for_sales = crud_driver(self, 'diary', 'read', {
            'pick_all': False,
            'multi': False,
            'pick_cols': ['*'],
            'field': 'amount',
            'operator': '=',
            'order_by': ['id', 'date'],
            'order_': ['ASC', 'ASC'],
            'sort': True,
            'value': (0,)
        })
        sales_data = translate_diary_data_to_table(self, 'sales', diary_data_for_sales)
        crud_driver(self, 'sales', 'delete', None)
        crud_driver(self, 'sales', 'create', {
            'multi': True,
            'fields': get_template_fields('sales'),
            'value_list': sales_data
        })
        return
    except BaseException as err:
        print('error on generating sales table: {}'.format(err))
        raise Exception(str(err))


def calculate_stock(self):
    try:
        diary_data_for_stock = crud_driver(self, 'diary', 'read', {
            'pick_all': False,
            'multi': False,
            'pick_cols': ['*'],
            'field': 'item_code',
            'operator': '<>',
            'order_by': ['is_new', 'date'],
            'order_': ['DESC', 'ASC'],       # is_new is mandatory to be sorted desc
            'sort': True,
            'value': ('',)
        })
        data_tuples_for_stock = data_tuple_for_stock_builder(self, diary_data_for_stock)
        crud_driver(self, 'stock', 'delete', None)
        crud_driver(self, 'stock', 'create', {
            'multi': True,
            'fields': get_template_fields('stock'),
            'value_list': data_tuples_for_stock
        })
        return
    except BaseException as err:
        print('error on generating sales table: {}'.format(err))
        raise Exception(str(err))


def calculate_capital(self):
    try:
        diary_data_for_capital = crud_driver(self, 'diary', 'read', {
            'pick_all': False,
            'multi': False,
            'pick_cols': ['*'],
            'field': 'amount',
            'operator': '<>',
            'order_by': ['id', 'date'],
            'order_': ['ASC', 'ASC'],
            'sort': True,
            'value': (0,)
        })
        capital_data = translate_diary_data_to_table(self, 'capital', diary_data_for_capital)
        crud_driver(self, 'capital', 'delete', None)
        crud_driver(self, 'capital', 'create', {
            'multi': True,
            'fields': get_template_fields('capital'),
            'value_list': capital_data
        })
        return
    except BaseException as err:
        print('error on generating sales table: {}'.format(err))
        raise Exception(str(err))


def calculate_statistics(self):
    try:
        last_row_on_diary = crud_driver(self, 'diary', 'read', {})[-1]
        capital_total = last_row_on_diary[get_index_in_template('diary', 'total_')]
        capital_invertido = last_row_on_diary[get_index_in_template('diary', 'invested_')]
        cash_en_caja = last_row_on_diary[get_index_in_template('diary', 'cash_')]

        session_resume = crud_driver(self, 'diary', 'raw_exec', {
            'raw_exec': 'SELECT TOTAL(sell_price), TOTAL(price), TOTAL(salary) FROM diary WHERE is_sale = ? AND date = ? ',
            'value': (True, self.date_session)})[0]

        session_consignations = crud_driver(self, 'diary', 'raw_exec', {
            'raw_exec': 'SELECT TOTAL(price) FROM diary WHERE is_consignation = ? AND is_sale = ? AND date = ? ',
            'value': (True, True, self.date_session)
        })[0][0]

        ventas_del_dia = session_resume[0] if session_resume[0] is not None else 0
        retorno_inversion = (float(session_resume[1]) - float(session_consignations)) if session_resume[
                                                                                             1] is not None else 0
        ganancias_netas = float(ventas_del_dia) - float(retorno_inversion) - float(session_consignations)
        salario_total = session_resume[2] if session_resume[2] is not None else 0
        renta = 125  # ajustar este valor luego desde el dialog
        ganancias_reales_comun = ganancias_netas - renta - float(salario_total)
        ganancias_reales_parte = ganancias_reales_comun / 2
        compras_del_dia = crud_driver(self, 'diary', 'raw_exec', {
            'raw_exec': 'SELECT  TOTAL(total_per_item(price,quantity)) FROM diary WHERE is_sale = ? AND is_consignation = ? AND date = ? AND item_code <> ? ',
            'value': (False, False, self.date_session, '')})[0][0]
        compras_del_dia = compras_del_dia if compras_del_dia is not None else 0

        # todo a la hora de implementar los filtros de tiempo en los datos de las estadisticas
        #   es aqui donde se deben manipular los datos para lograr que dichos filtros funcionen.
        totals_resume = crud_driver(self, 'diary', 'raw_exec', {
            'raw_exec': 'SELECT TOTAL(sell_price), TOTAL(price), TOTAL(salary) FROM diary WHERE is_sale = ?',
            'value': (True,)})[0]

        __rent_tot = crud_driver(self, 'diary', 'raw_exec', {
            'raw_exec': 'SELECT COUNT( DISTINCT date) FROM diary '})[0][0]

        ventas_totales = float(totals_resume[0]) if totals_resume[0] is not None else 0
        __invert_tot = float(totals_resume[1]) if totals_resume[1] is not None else 0
        __sal_tot = float(totals_resume[2]) if totals_resume[2] is not None else 0

        ganancias_totales = ventas_totales - __invert_tot
        ganancias_reales_totales = ganancias_totales - __sal_tot - 125 * __rent_tot
        invertido_total = last_row_on_diary[get_index_in_template('diary', 'total_')]
        capital_de_robert = last_row_on_diary[get_index_in_template('diary', 'robert_')]
        capital_de_ariadna = last_row_on_diary[get_index_in_template('diary', 'ariadna_')]

        return (capital_total, capital_invertido, cash_en_caja, ventas_del_dia, retorno_inversion, ganancias_netas,
                salario_total, renta, ganancias_reales_comun, ganancias_reales_parte, compras_del_dia,
                ventas_totales, ganancias_totales, ganancias_reales_totales, invertido_total, capital_de_robert,
                capital_de_ariadna, session_consignations)
    except:
        return tuple((0 / i for i in range(1, 19)))


def translate_diary_data_to_table(self, table: str, diary_data):  # only for sales and capital tables
    if table in ['stock', 'statistics', 'diary']:
        raise ValueError(
            'the table {} is not supported by <translate_diary_data_to_table>  method'.format(table))
    tuple_idx, ____ = on_diary_table_find_index_and_fields_of(self, table)
    table_x_data = list((tuple((row[index] for index in tuple_idx)) for row in diary_data))
    return table_x_data


def data_tuple_for_stock_builder(self, data):
    # index on diary table:
    id__ = get_index_in_template('diary', 'id')
    date__ = get_index_in_template('diary', 'date')
    is_new__ = get_index_in_template('diary', 'is_new')
    is_sale__ = get_index_in_template('diary', 'is_sale')
    is_consignation__ = get_index_in_template('diary', 'is_consignation')
    quantity__ = get_index_in_template('diary', 'quantity')
    item_name__ = get_index_in_template('diary', 'item_name')
    price__ = get_index_in_template('diary', 'price')
    sell_price__ = get_index_in_template('diary', 'sell_price')
    item_code__ = get_index_in_template('diary', 'item_code')

    stock_item_codes = set(
        filter(
            lambda item: item is not None and item != '',
            (row[item_code__] for row in data))
    )
    data_of_items = dict(
        ((name, [1, 'date', 'consig', 'code', 'name', 'price', 0, 0, 0, 'sell_price']) for
         name in stock_item_codes)
    )
    for row in data:
        if row[item_code__] in stock_item_codes:
            current_data_row = data_of_items.get(row[item_code__])
            if row[is_new__]:
                current_data_row[g_i('stock', 'id')] = row[id__]
                current_data_row[g_i('stock', 'date')] = row[date__]
                current_data_row[g_i('stock', 'is_consignation')] = row[is_consignation__]
                current_data_row[g_i('stock', 'item_code')] = row[item_code__]
                current_data_row[g_i('stock', 'item_name')] = row[item_name__]
                current_data_row[g_i('stock', 'price')] = row[price__]
                current_data_row[g_i('stock', 'sell_price')] = row[sell_price__]
                current_data_row[g_i('stock', 'total')] = int(row[quantity__])
                current_data_row[g_i('stock', 'sold')] = 0
                current_data_row[g_i('stock', 'on_stock')] = int(row[quantity__])
            elif row[is_sale__]:
                current_data_row[g_i('stock', 'sold')] = \
                    current_data_row[g_i('stock', 'sold')] + int(row[quantity__])
                current_data_row[g_i('stock', 'on_stock')] = \
                    current_data_row[g_i('stock', 'on_stock')] - int(row[quantity__])
            else:
                new_total =  current_data_row[g_i('stock', 'total')] + int(row[quantity__])
                new_on_stock =  current_data_row[g_i('stock', 'on_stock')] + int(row[quantity__])
                current_data_row[g_i('stock', 'total')] = new_total
                current_data_row[g_i('stock', 'on_stock')] = new_on_stock

            # updating the dict values
            data_of_items.update({row[item_code__]: current_data_row})
    return list((tuple(row) for row in data_of_items.values()))
