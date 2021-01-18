import os
import re
import sqlite3

# TODO añadir checks para que haga chequeo de campos en la db
from dialogs.auxiliar_dialogs import MessageBox

statusDB = 'appStatusDB.db'

table_templates = [
    {
        'name': 'sales',
        'fields': [
            {'name': 'id', 'props': ['INTEGER', 'PRIMARY KEY']},
            {'name': 'date', 'props': ['TEXT', 'NOT NULL']},
            {'name': 'is_new', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'is_sale', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'is_consignation', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'quantity', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'item_name', 'props': ['TEXT', 'NOT NULL']},
            {'name': 'price', 'props': ['REAL', 'NOT NULL']},
            {'name': 'sell_price', 'props': ['REAL', 'NOT NULL', ]},
            {'name': 'comments', 'props': ['TEXT']},
            {'name': 'item_code', 'props': ['TEXT', 'NOT NULL']},
            {'name': 'salary', 'props': ['REAL']}
        ],
        'checks': {'name': 'CHECK', 'props': ['(sell_price > price AND price > 0) ']}

    }, {
        'name': 'stock',
        'fields': [
            {'name': 'id', 'props': ['INTEGER', 'PRIMARY KEY']},
            {'name': 'date', 'props': ['TEXT']},
            {'name': 'is_consignation', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'item_code', 'props': ['TEXT', 'NOT NULL', 'UNIQUE']},
            {'name': 'item_name', 'props': ['TEXT', 'NOT NULL']},
            {'name': 'price', 'props': ['REAL', 'NOT NULL']},
            {'name': 'total', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'sold', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'on_stock', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'sell_price', 'props': ['REAL', 'NOT NULL']}
        ],
        'checks': {'name': 'CHECK', 'props': [
            '(total >= 0 AND sold >=0 AND on_stock >=0 AND sell_price > price AND price > 0 ) ']}

    }, {
        'name': 'capital',
        'fields': [
            {'name': 'id', 'props': ['INTEGER', 'PRIMARY KEY', 'NOT NULL']},
            {'name': 'date', 'props': ['TEXT', 'NOT NULL']},
            {'name': 'amount', 'props': ['REAL', 'NOT NULL']},
            {'name': 'owner', 'props': ['TEXT', 'NOT NULL']},
            {'name': 'robert_', 'props': ['REAL']},
            {'name': 'ariadna_', 'props': ['REAL']},
            {'name': 'invested_', 'props': ['REAL', 'NOT NULL']},
            {'name': 'cash_', 'props': ['REAL']},
            {'name': 'total_', 'props': ['REAL', 'NOT NULL']},
            {'name': 'comments', 'props': ['TEXT']},
        ],
        'checks': {'name': 'CHECK', 'props': [
            '(total_ >= 0 AND robert_ >= 0 AND ariadna_ >= 0 AND amount > 0 ) ']}
    }, {
        'name': 'statistics',
        'fields': [
            {'name': 'id', 'props': ['INTEGER', 'PRIMARY KEY']},
            {'name': 'date', 'props': ['TEXT']},
            {'name': 'total_sales', 'props': ['INTEGER']},
            {'name': 'total_inv', 'props': ['INTEGER']},
            {'name': 'consignation_payments', 'props': ['INTEGER']},
            {'name': 'net_utilities', 'props': ['INTEGER']},
            {'name': 'salary', 'props': ['INTEGER']},
            {'name': 'real_utilities', 'props': ['INTEGER']},
            {'name': 'stock_entries', 'props': ['INTEGER']},
            {'name': 'capital_entries', 'props': ['INTEGER']},
            {'name': 'total_', 'props': ['INTEGER']},
            {'name': 'cash', 'props': ['INTEGER']},

        ]
    }, {
        'name': 'diary',
        'fields': [
            {'name': 'id', 'props': ['INTEGER', 'PRIMARY KEY']},
            {'name': 'entry_count', 'props':['TEXT']},
            {'name': 'date', 'props': ['TEXT', 'NOT NULL']},
            {'name': 'is_new', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'is_sale', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'is_consignation', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'quantity', 'props': ['INTEGER', 'NOT NULL']},
            {'name': 'item_name', 'props': ['TEXT', 'NOT NULL']},
            {'name': 'price', 'props': ['REAL', 'NOT NULL']},
            {'name': 'sell_price', 'props': ['REAL', 'NOT NULL', ]},
            {'name': 'comments', 'props': ['TEXT']},
            {'name': 'item_code', 'props': ['TEXT', 'NOT NULL']},
            {'name': 'salary', 'props': ['REAL']},
            {'name': 'amount', 'props': ['REAL', 'NOT NULL']},
            {'name': 'owner', 'props': ['TEXT', 'NOT NULL']},
            {'name': 'robert_', 'props': ['REAL']},
            {'name': 'ariadna_', 'props': ['REAL']},
        ]
    }
]


# ----sqlite user defined functions:
def regexp(expression, context, engine=re.search):
    print('searching expression: < %s > in context: < %s >' % (expression, context))
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


def get_template_fields(index_or_name, no_id=False):
    table_template = get_table_template(index_or_name)
    return list((field.get('name') for field in table_template.get('fields')))[1:] if no_id \
        else list((field.get('name') for field in table_template.get('fields')))


def get_index_in_template(table: str, field_name: str):
    fields = get_template_fields(table)
    return fields.index(field_name)


def initialize_cursor(self):
    if self.cursor is None:
        print('debug: initializing cursor')
        self.cursor = self.current_connection.cursor()
    return


def close_cursor(self):
    try:
        self.cursor.close()
        self.cursor = None
        print('cursor has been closed')
        return
    except:
        print('info: close cursor was not executed')
        return

def _close_db(self):
    try:
        self.current_connection.close()
        self.current_connection = None
        print('db has been closed')
        return
    except:
        print('info: close_db was not executed')
        return


def launch_connection(self, db_name):
    print('attempting to connect to %s' % db_name)
    try:
        self.current_connection = sqlite3.connect(os.path.join(os.pardir,'databases', db_name))
        if db_name != statusDB:
            self.current_connection.create_function('REGEXP', 2, regexp)
            self.current_connection.create_function('total_per_item', 2, total_per_item)
            self.current_connection.create_function('find_profit', 4, find_profit)
        initialize_cursor(self)
        self.status.update({"connected_to": db_name})
        self.connected_signal.emit(db_name)
        print('successfully connected to {}'.format(db_name))
    except sqlite3.Error as error:
        print('error while trying to connect to {}  details:\n {}'.format(db_name, error))
        # todo show no buttons message for showing error and
        #  >> quit the app (done )
        self.fatal_error.emit()


def connect_toDB(self, db_name, init_form=True, create_tables=True, silent=False): # todo refactorize
    # todo extract form initialization from this logic,
    if init_form:
        # init.initializeForm(self)
        pass
    launch_connection(self, db_name)
    print('connected to: %s...' % db_name)
    self.connected_signal.emit(db_name)
    if not silent:
        connection_alert = MessageBox(
            lambda: print('ok'),
            'Now, you\'re connected to: %s' % db_name,
            'i', 'Connection Success')
        connection_alert.show()
    if create_tables:
        create_tables_onDb(self)
    return


def close_connection(self):
    close_cursor(self)
    _close_db(self)
    print('connection to db has been shutted down')
    return

# todo this whole section must be refactored
#  for using the new methods crud driver or call directly the method on sqlite
def cursor_execution(self, query_list, action, multi=False, message='cursor executed'):
    # action -> CRUD operations
    print('calling execution on current cursor')
    if self.cursor is not None:
        print('force cursor closing inside cursor_execution because cursor initial value was not None')
        close_cursor(self)
    initialize_cursor(self)
    try:
        if not multi:
            if not isinstance(query_list, type([])):
                raise TypeError('when option multi is False (default), must pass list [str]')
                # if multi =False query list will be a list of strings and  loop execution (less performant)
            for query in query_list:
                self.cursor.execute(query)
                print(message)
        elif multi:
            if not isinstance(query_list, type(('a', []))):
                raise TypeError('when option multi is set to True, must pass tuple: \'str\',\'list\'')
            # cursor execution will be a tuple with (string,list of tuples), bulk execution
            self.cursor.executemany(query_list[0], query_list[1])
    except sqlite3.Error as error:
        print('warning on curson execution: %s' % error)
        return
    finally:
        if action == 'insert':
            self.current_connection.commit()
            print('commited to db')
            close_cursor(self)
            return
        if action == 'select':
            record = self.cursor.fetchall()
            return record
        print('warning: operation was not defined')
        return


def _create_table_templates():
    # TODO: debo implementar la funcion del Check de las tablas que esta albergado
    #  en propiedad aparte en los dictionaries
    cursor_commands = []
    for template in table_templates:
        command = 'CREATE TABLE %s (' % template.get('name')
        fields = template.get('fields')
        for field in fields:
            if fields.index(field) > 0:
                command += ','
            command += ' %s ' % field.get('name')
            props = field.get('props')
            for prop in props:
                # if props.index(prop) > 0:
                #    command += ' '
                command += ' %s ' % prop
        command += ' )'
        cursor_commands.append(command)
    return cursor_commands


def create_tables_onDb(self, template=[]):
    if len(template) > 0:
        return cursor_execution(self, template, 'insert', False, 'tables created successfully')
    return cursor_execution(self, _create_table_templates(), 'insert', False, 'tables created successfully')
