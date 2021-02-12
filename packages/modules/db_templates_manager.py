import os
import re
import sqlite3

from PySide2.QtWidgets import QApplication
from packages.dialogs.auxiliar_dialogs import selfCloseInterface

statusDB_name = 'appStatusDB.db'

cells_formats = {
    'currency': lambda v__, __: '$ {:,.2f}'.format(return_float_or_zero(v__)),
    'bool': lambda v__, key_word: '{}'.format(key_word if return_int_or_zero(v__) == 1 else ''),
    'text': lambda v__, __: '{}'.format(v__),
    'integer': lambda v__, __: '{}'.format(return_int_or_zero(v__))
}


def return_int_or_zero(value):
    try:
        return int(value)
    except:
        return 0


def return_float_or_zero(value):
    try:
        return float(value)
    except:
        return 0


table_templates = [
    {
        'name': 'sales',
        'fields': [
            {'name': 'id', 'props': ['TEXT', 'PRIMARY KEY'], 'format_like': 'text'},
            {'name': 'date', 'props': ['TEXT', 'NOT NULL'], 'format_like': 'text'},
            {'name': 'is_new', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'bool', 'key_word': 'Nuevo'},
            {'name': 'is_sale', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'bool', 'key_word': 'Venta'},
            {'name': 'is_consignation', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'bool', 'key_word': 'Consignacion'},
            {'name': 'quantity', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'integer'},
            {'name': 'item_name', 'props': ['TEXT', 'NOT NULL'], 'format_like': 'text'},
            {'name': 'price', 'props': ['REAL', 'NOT NULL'], 'format_like': 'currency'},
            {'name': 'sell_price', 'props': ['REAL', 'NOT NULL', ], 'format_like': 'currency'},
            {'name': 'comments', 'props': ['TEXT'], 'format_like': 'text'},
            {'name': 'item_code', 'props': ['TEXT', 'NOT NULL'], 'format_like': 'text'},
            {'name': 'salary', 'props': ['REAL'], 'format_like': 'currency'}
        ],
        'checks': {'name': 'CHECK', 'props': ['(sell_price > price AND price > 0) ']}

    }, {
        'name': 'stock',
        'fields': [
            {'name': 'id', 'props': ['TEXT', 'PRIMARY KEY'], 'format_like': 'text'},
            {'name': 'date', 'props': ['TEXT'], 'format_like': 'text'},
            {'name': 'is_consignation', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'bool', 'key_word': 'Consignacion'},
            {'name': 'item_code', 'props': ['TEXT', 'NOT NULL', 'UNIQUE'], 'format_like': 'text'},
            {'name': 'item_name', 'props': ['TEXT', 'NOT NULL'], 'format_like': 'text'},
            {'name': 'price', 'props': ['REAL', 'NOT NULL'], 'format_like': 'currency'},
            {'name': 'total', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'integer'},
            {'name': 'sold', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'integer'},
            {'name': 'on_stock', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'integer'},
            {'name': 'sell_price', 'props': ['REAL', 'NOT NULL'], 'format_like': 'currency'}
        ],
        'checks': {'name': 'CHECK', 'props': [
            '(total >= 0 AND sold >=0 AND on_stock >=0 AND sell_price > price AND price > 0 ) ']}

    }, {
        'name': 'capital',
        'fields': [
            {'name': 'id', 'props': ['TEXT', 'PRIMARY KEY', 'NOT NULL'], 'format_like': 'text'},
            {'name': 'date', 'props': ['TEXT', 'NOT NULL'], 'format_like': 'text'},
            {'name': 'amount', 'props': ['REAL', 'NOT NULL'], 'format_like': 'currency'},
            {'name': 'owner', 'props': ['TEXT', 'NOT NULL'], 'format_like': 'text'},
            {'name': 'robert_', 'props': ['REAL'], 'format_like': 'currency'},
            {'name': 'ariadna_', 'props': ['REAL'], 'format_like': 'currency'},
            {'name': 'invested_', 'props': ['REAL', 'NOT NULL'], 'format_like': 'currency'},
            {'name': 'cash_', 'props': ['REAL'], 'format_like': 'currency'},
            {'name': 'total_', 'props': ['REAL', 'NOT NULL'], 'format_like': 'currency'},
            {'name': 'comments', 'props': ['TEXT'], 'format_like': 'text'},
        ],
        'checks': {'name': 'CHECK', 'props': [
            '(total_ >= 0 AND robert_ >= 0 AND ariadna_ >= 0 AND amount > 0 ) ']}
    }, {
        'name': 'statistics',
        'fields': [
            {'name': 'id', 'props': ['TEXT', 'PRIMARY KEY'], 'format_like': 'text'},
            {'name': 'date', 'props': ['TEXT'], 'format_like': 'text'},
            {'name': 'total_sales', 'props': ['INTEGER'], 'format_like': 'currency'},
            {'name': 'total_inv', 'props': ['INTEGER'], 'format_like': 'currency'},
            {'name': 'consignation_payments', 'props': ['INTEGER'], 'format_like': 'currency'},
            {'name': 'net_utilities', 'props': ['INTEGER'], 'format_like': 'currency'},
            {'name': 'salary', 'props': ['INTEGER'], 'format_like': 'currency'},
            {'name': 'real_utilities', 'props': ['INTEGER'], 'format_like': 'currency'},
            {'name': 'stock_entries', 'props': ['INTEGER'], 'format_like': 'currency'},
            {'name': 'capital_entries', 'props': ['INTEGER'], 'format_like': 'currency'},
            {'name': 'total_', 'props': ['INTEGER'], 'format_like': 'currency'},
            {'name': 'cash', 'props': ['INTEGER'], 'format_like': 'currency'},

        ]
    }, {
        'name': 'diary',
        'fields': [
            {'name': 'id', 'props': ['TEXT'], 'format_like': 'text'},
            {'name': 'entry_counter', 'props': ['TEXT'], 'format_like': 'text'},
            {'name': 'date', 'props': ['TEXT', 'NOT NULL'], 'format_like': 'text'},
            {'name': 'is_new', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'bool', 'key_word': 'Nuevo'},
            {'name': 'is_sale', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'bool', 'key_word': 'Venta'},
            {'name': 'is_consignation', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'bool', 'key_word': 'Consignacion'},
            {'name': 'quantity', 'props': ['INTEGER', 'NOT NULL'], 'format_like': 'integer'},
            {'name': 'item_name', 'props': ['TEXT', 'NOT NULL'], 'format_like': 'text'},
            {'name': 'price', 'props': ['REAL', 'NOT NULL'], 'format_like': 'currency'},
            {'name': 'sell_price', 'props': ['REAL', 'NOT NULL', ], 'format_like': 'currency'},
            {'name': 'comments', 'props': ['TEXT'], 'format_like': 'text'},
            {'name': 'item_code', 'props': ['TEXT', 'NOT NULL'], 'format_like': 'text'},
            {'name': 'salary', 'props': ['REAL'], 'format_like': 'currency'},
            {'name': 'amount', 'props': ['REAL', 'NOT NULL'], 'format_like': 'currency'},
            {'name': 'owner', 'props': ['TEXT', 'NOT NULL'], 'format_like': 'text'},
            {'name': 'robert_', 'props': ['REAL'], 'format_like': 'currency'},
            {'name': 'ariadna_', 'props': ['REAL'], 'format_like': 'currency'},
            {'name': 'invested_', 'props': ['REAL', 'NOT NULL'], 'format_like': 'currency'},
            {'name': 'cash_', 'props': ['REAL'], 'format_like': 'currency'},
            {'name': 'total_', 'props': ['REAL', 'NOT NULL'], 'format_like': 'currency'},
            {'name': 'unique_id', 'props': ['REAL', 'UNIQUE'], 'format_like': 'text'}
        ]
    }
]


# ----sqlite user defined functions: must review
def regexp(expression, context, engine=re.search):
    # print('searching expression: < %s > in context: < %s >' % (expression, context))
    try:
        return 1 if engine(str(expression), str(context)) else 0
    except BaseException as error:
        print('failed regexp operation due: \n{}'.format(error))


def total_per_item(amount, price):
    try:
        return amount * price
    except BaseException as e:
        print('error while finding total price per item:', e)


def find_profit(is_sale, amount, sell_price, price):
    if not is_sale: return 0
    try:
        return sell_price * amount - price * amount
    except BaseException as error:
        print('error finding real profit: ', error)


# ---------sqlite user defined aggregations


def get_table_template(index_or_name):
    if isinstance(index_or_name, int):
        if index_or_name not in range(len(table_templates)):
            raise ValueError('No Table for index %s', index_or_name)
        return table_templates[index_or_name]
    if isinstance(index_or_name, str):
        # keys = {'sales': 0, 'stock': 1, 'capital': 2, 'statistics': 3 }
        names = list((t.get('name') for t in table_templates))
        keys = dict(((name, index) for (index, name) in enumerate(names)))
        return table_templates[keys.get(index_or_name)]
    else:
        raise TypeError('this function does not support args of type: < %s > ' % type(index_or_name))


def get_template_fields(index_or_name, no_id=False):  # returns ['field_name'...]
    table_template = get_table_template(index_or_name)
    return list((field.get('name') for field in table_template.get('fields')))[1:] if no_id \
        else list((field.get('name') for field in table_template.get('fields')))


def get_index_in_template(table: str, field_name: str):
    fields = get_template_fields(table)
    return fields.index(field_name)


def get_format_of_field(table: str, field_or_index_in_table): # returns a function
    if isinstance(field_or_index_in_table, (str, int)):
        table_template__ = get_table_template(table)
        fields__ = table_template__.get('fields')
        if isinstance(field_or_index_in_table, str):
            field = next(filter(
                lambda i: i is not None,
                (item if item.get('name') == field_or_index_in_table else None for item in fields__)
            ))
        else:
            field = fields__[field_or_index_in_table]

        format_like__ = field.get('format_like')
        key_word__ = field.get('key_word')
        return lambda value__: cells_formats.get(format_like__)(value__, key_word__)

    else:
        raise Exception(
            'get_format_of_field called with wrong <field_or_index> argument type <{}>'.format(
                type(field_or_index_in_table)
            )
        )



def on_diary_table_find_index_and_fields_of(self, table: str):
    # returns a tuple [x_field_index_on_diary...],[field_name...]
    diary_fields = get_template_fields('diary')
    x_fields = get_template_fields(table)
    x_field_index_on_diary = list(filter(lambda item: item is not None, map(
        lambda item: get_index_in_template('diary', item) if item in diary_fields else None,
        x_fields)))
    x_field_on_diary = list(filter(lambda item: item is not None, map(
        lambda item: item if item in diary_fields else None,
        x_fields)))
    return x_field_index_on_diary, x_field_on_diary


# sqlite3  related functions.....

def initialize_cursor(self):
    self.cursor = self.connection.cursor()
    return


def close_cursor(self):
    try:
        self.cursor.close()
        self.cursor = None
        # print('debug: cursor has been closed')
        return
    except:
        print('info: close_cursor was not executed')
        return


def _close_db(self):
    try:
        self.connection.close()
        self.connection = None
        print('db has been closed')
        return
    except:
        print('info: close_db was not executed')
        return


def create_connection(self, db_name):
    try:
        self.connection = sqlite3.connect(os.path.join(os.curdir, 'databases', db_name))
        if db_name != statusDB_name:
            self.connection.create_function('REGEXP', 2, regexp)
            self.connection.create_function('total_per_item', 2, total_per_item)
            self.connection.create_function('find_profit', 4, find_profit)
            self.status.update({"connected_to": db_name})
        initialize_cursor(self)
        self.connected_signal.emit(db_name)
        # print('debug: successfully connected to {}'.format(db_name))
    except sqlite3.Error as error:
        print('error while trying to connect to {}  details:\n {}'.format(db_name, error))
        selfCloseInterface('Failed on Connecting To Database {}'.format(db_name), 3, 3, 'Critical Error',
                           'Closing App...')
        QApplication.quit()


def connect_toDB(self, db_name, create_tables=True, silent=False):
    create_connection(self, db_name)
    print('connected to: %s...' % db_name)
    if create_tables:
        create_tables_onDb(self)
    if not silent:
        selfCloseInterface(
            'Estas conectado a la base de datos: {}'.format(db_name),
            title='Conectado a la Base de Datos')
        # changed by autocloseable alert
        # connection_alert = MessageBox(
        #     lambda: print('ok'),
        #     'Now, you\'re connected to: %s' % db_name,
        #     'i', 'Connection Success')
        # connection_alert.show()
    if db_name != statusDB_name:
        self.recalculate_tables_signal.emit()
    return


def close_connection(self):
    close_cursor(self)
    _close_db(self)
    print('connection to db has been shutted down')
    return


def cursor_execution(self, query_list, message='cursor executed'):
    # action -> CRUD operations
    try:
        for query in query_list:
            self.cursor.execute(query)
            print(message)
    except sqlite3.Error as error:
        print('warning on curson execution: %s' % error)
        return
    finally:
        self.connection.commit()
        print('commited to db')
        close_cursor(self)
        return


def create_table_templates():
    cursor_commands = []
    for template in table_templates:
        command = 'CREATE TABLE {} ('.format(template.get('name'))
        fields = template.get('fields')
        for field in fields:
            if fields.index(field) > 0:
                command += ','
            command += ' {} '.format(field.get('name'))
            props = field.get('props')
            for prop in props:
                # if props.index(prop) > 0:
                #    command += ' '
                command += ' {} '.format(prop)
        command += ' )'
        cursor_commands.append(command)
    return cursor_commands


def create_tables_onDb(self, template=[]):
    t_temp = template if len(template) > 0 else create_table_templates()
    return cursor_execution(self, t_temp, 'tables created successfully')
