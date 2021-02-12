import sqlite3

from packages.dialogs.auxiliar_dialogs import selfCloseInterface
from packages.extras.error_utils import type_checker, condition_checker, ConditionFailedException
from packages.modules.db_templates_manager import close_cursor, initialize_cursor

sqlite_query_operators = [
    '=', '>', '<', '<=', '>=', '<>', '!=', 'ALL', 'AND', 'ANY',
    'BETWEEN', 'EXISTS', 'IN', 'LIKE', 'NOT', 'OR', 'REGEXP'
]
sqlite_logic_joiners = ['AND', 'OR']

sqlite_update_keys = ['SET']


def _insert_on_db(self, table, options):
    # options: dict
    # | {   multi: boolean,
    # |     fields: list<str>
    # |     value: tuple
    # |     value_list: list< tuple >
    # |     ...
    default_options = {
        'value': None,
        'multi': False,
        'fields': [],
        'value_list': [],
    }
    default_options.update(options)

    value = default_options.get('value')
    multi = default_options.get('multi')
    fields = default_options.get('fields')
    value_list = default_options.get('value_list')

    type_checker(self, multi, bool)
    condition_checker(self, all((type_checker(self, field, str) for field in fields)), True)

    if multi:
        type_checker(self, value_list, type(None), TypeError, False)
        condition_checker(self,
                              all((len(fields) == len(x) for x in value_list)),
                              True,
                                      'not enough fields for values or vice versa'
                              )

    if not multi:
        condition_checker(self,
                              all([
                                          type_checker(self, value, tuple),
                                          len(value) == len(fields)
                                      ]), True,
                                      'not enough fields for values or vice versa'
                              )

    fields_str = str.join(', ', fields)
    q_mark = str.join(', ', ('? ' for i in range(len(fields))))
    command = 'INSERT INTO ' + table + ' (' + fields_str + ') VALUES (' + q_mark + ')'

    # execution phase
    # print(command)
    if multi:
        self.cursor.executemany(command, value_list)
        self.connection.commit()
        return
    if not multi:
        self.cursor.execute(command, value)
        self.connection.commit()
        return


def _select_on_db(self, table, options):
    # print('crud_driver: selecting table %s' % table)
    # print('with options %s' % str(options))
    # options: dict {
    # |     pick_all: bool
    # |     multi: bool (if True uses many conditions when querying results)
    # |     pick_cols: list (cols showed on result)
    # |     field: str (field to build the comparison upon)
    # |     field_list: list<str> (list of fields for perform comparison multifield)
    # |     join_with: str in ['AND', 'OR']
    # |     operator: str
    # |     operator_list: list<str> (list of operators for perform comparison multifield)
    # |     order_by: ['id', 'date'],
    # |     order_: ['ASC', 'ASC']
    # |     sort: True.
    # |     value: tuple()...
    default_options = {
        'pick_all': True,
        'multi': False,
        'join_with': None,
        'pick_cols': ['*'],
        'field': None,
        'field_list': None,
        'operator': None,
        'operator_list': None,
        'value': None,
        'order_by': ['date'],
        'order_': ['ASC'],
        'sort': False
    }
    default_options.update(options)
    pick_all = default_options.get('pick_all')
    multi = default_options.get('multi')
    pick_cols = default_options.get('pick_cols')
    value = default_options.get('value')
    cols = '*'

    order = '' if not default_options.get('sort') else ' ORDER BY ' + ', '.join(list(('{} {}'.format(
        default_options.get('order_by')[i],
        default_options.get('order_')[i]
    ) for i in range(len(default_options.get('order_by'))))))

    # print('sort this table : ', order)

    type_checker(self, pick_all, bool),
    if pick_all:
        command = 'SELECT ' + cols + ' FROM ' + table + order

        # print('command to be executed on current operation: ', command)
        self.cursor.execute(command)
        return
    if all([
        type_checker(self, pick_cols, list),
        all((type_checker(self, col, str) for col in pick_cols)),
        len(pick_cols) >= 1
    ]):
        cols = str.join(', ', (col for col in pick_cols))

    command = 'SELECT ' + cols + ' FROM ' + table
    if default_options.get('field') is None and default_options.get('field_list') is None:
        command += order
        # print('command to be executed on current operation: ', command)
        self.cursor.execute(command)
        return

    type_checker(self, multi, bool)
    if multi:
        join_with = default_options.get('join_with')
        field_list = default_options.get('field_list')
        operator_list = default_options.get('operator_list')
        condition_checker(self,
                              len(field_list) == len(operator_list), True,
                                      'discordance between fields and operators'
                              )
        condition_checker(self,
                              join_with in sqlite_logic_joiners,
                              True,
                                      'must define a join operator for multi where clauses'
                              )
        condition_checker(self, all(
            (type_checker(self, field, str) for field in field_list)
        ), True, 'fields should be a string')
        condition_checker(self, all(
            (type_checker(self, operator, str) for operator in operator_list)
        ), True, 'operators should be a string')

        compound_filter = str.join(
            ' %s ' % join_with,
            ('%s %s ?' % (field_list[index], operator_list[index]) for index in range(len(field_list)))
        )
        command = command + ' WHERE ' + compound_filter + order +';'
        # print('debug: inside branch multi command to be executed on current operation: ', command)
    if not multi:  # single query conditions
        field = options.get('field')
        operator = options.get('operator')
        type_checker(self, operator, str)
        type_checker(self, field, str)
        condition_checker(self, operator in sqlite_query_operators, True,
                                      'operator < %s > not supported' % operator)
        command = command + ' WHERE ' + field + ' ' + operator + ' ?' + order +' ;'
        # print('debug: inside branch multi command to be executed on current operation: ', command)

    # print('command to be executed on current operation: ', command)
    type_checker(self, value, tuple)
    condition_checker(self, len(value) == str.count(command, '?'))
    self.cursor.execute(command, value)

    return


def _update_on_db(self, table, options):
    # | action: str in ['SET', ??? ]
    # | slave_col: str
    # | slave_op: str in query operators
    # | slave_col_list: list<str>        >> used when many rows to update
    # | slave_op_list: list<str> in query operators >> idem above
    # | value: tuple
    # | value_list: list<tuple>
    # | master_col: str >> name of the master_col slave_col, the one that defines the comparison parameter
    # | master_op: >> str in query operators, this one discriminates the query results
    # | master_col_list: list<str>  >> list with name of the master_col used on many cols updating
    # | master_op_list: >> list<str> in query operators, this one discriminates the query results
    # | bulk_updating: bool >> defines if updating one or many rows in a single query
    # | multi_cols: bool >> defines if updating one or many cols in a single query
    # | multi_filter: bool >> defines if use one or many cols for filter the query
    # | join_with: str in ['AND', 'OR']
    # | ...
    default_options = {'action': None,
                       'slave_col': None, 'slave_op': None,
                       'master_col': None, 'master_op': None, 'value': None,
                       'slave_col_list': [None], 'slave_op_list': [None],
                       'master_col_list': [None], 'master_op_list': [None], 'value_list': [None],
                       'bulk_updating': False, 'multi_cols': False, 'multi_filter': False, 'join_with': None
                       }

    default_options.update(options)

    action = default_options.get('action')
    bulk_updating = default_options.get('bulk_updating')
    multi_cols = default_options.get('multi_cols')
    multi_filter = default_options.get('multi_filter')
    # -----just 4 ref:  these statements are used only inside the branch that needs it
    # slave_col = default_options.get('slave_col')
    # slave_op = default_options.get('slave_op')
    # slave_col_list = default_options.get('slave_col_list')
    # slave_op_list = default_options.get('slave_op_list')
    # value = default_options.get('value')
    # value_list = default_options.get('value_list')
    # master_col = default_options.get('master_col')
    # master_op = default_options.get('master_op')
    # master_col_list = default_options.get('master_col_list')
    # master_op_list = default_options.get('master_op_list')
    # join_with = default_options('join_with')

    condition_checker(self, action in sqlite_update_keys)
    type_checker(self, multi_cols, bool)
    type_checker(self, bulk_updating, bool)
    type_checker(self, multi_filter, bool)

    command = 'UPDATE ' + table + ' ' + action

    if multi_cols:  # update many slave_cols per row
        slave_col_list = default_options.get('slave_col_list')
        slave_op_list = default_options.get('slave_op_list')

        type_checker(self, slave_col_list, list)
        type_checker(self, slave_op_list, list)
        condition_checker(self, all([
            all((type_checker(self, slave_col, str) for slave_col in slave_col_list)),
            all((type_checker(self, slave_op, str) for slave_op in slave_op_list)),
            all((condition_checker(self, slave_op in sqlite_query_operators) for slave_op in
                 slave_op_list)),
            len(slave_col_list) == len(slave_op_list)
        ]))

        slave_col_parameter = str.join(', ',
                                       (' %s %s ? ' % (slave_col_list[index], slave_op_list[index]) for index in
                                        range(len(slave_col_list)))
                                       )
        command += slave_col_parameter

    if not multi_cols:  # update a single slave_col per row
        slave_col = default_options.get('slave_col')
        slave_op = default_options.get('slave_op')

        condition_checker(self, all([
            type_checker(self, slave_col, str),
            type_checker(self, slave_op, str),
            condition_checker(self, slave_op in sqlite_query_operators)
        ]))
        slave_col_parameter = '%s %s ? ' % (slave_col, slave_op)
        command += slave_col_parameter

    command += 'WHERE '

    if multi_filter:  # use many master_cols for filter the query before updating rows
        master_col_list = default_options.get('master_col_list')
        master_op_list = default_options.get('master_op_list')
        join_with = default_options.get('join_with')

        condition_checker(self, all([
            join_with in sqlite_logic_joiners,
            type_checker(self, master_col_list, list),
            type_checker(self, master_op_list, list),
            len(master_col_list) == len(master_op_list),
            all((type_checker(self, master_col, str) for master_col in master_col_list)),
            all((type_checker(self, master_op, str) for master_op in master_op_list)),
            all((condition_checker(self, master_op in sqlite_query_operators) for master_op in
                 master_op_list))

        ]))

        compound_filter = str.join(
            ' %s ' % join_with,
            ('%s %s ?' % (master_col_list[index], master_op_list[index]) for index in range(len(master_col_list)))
        )

        command += compound_filter

    if not multi_filter:  # use just one master_col for filter the query before updating rows
        master_col = default_options.get('master_col')
        master_op = default_options.get('master_op')

        condition_checker(self, all([
            type_checker(self, master_col, str),
            type_checker(self, master_op, str),
        ]))

        compound_filter = '%s %s ?' % (master_col, master_op)

        command += compound_filter

    # --- execution phase ----
    if bulk_updating:  # perform many updating in a single query with executemany
        value_list = default_options.get('value_list')
        occurrences = str.count(command, '?')
        type_checker(self, value_list, list)
        condition_checker(self, any(
            (len(value_tuple) != occurrences for value_tuple in value_list)
        ), False)

        # print(command)
        self.cursor.executemany(command, value_list)
        self.connection.commit()
        return

    if not bulk_updating:  # perform a single update with execute
        value = default_options.get('value')
        occurrences = str.count(command, '?')
        type_checker(self, value, tuple)
        condition_checker(self, len(value) == occurrences)

        # print(command)
        self.cursor.execute(command, value)
        self.connection.commit()
        return
    raise Exception('must define bulk updating parameter before proceed...')


def _delete_on_db(self, table, options):
    if options is None:
        command = 'DELETE FROM ' + table
        # print(command)
        self.cursor.execute(command)
        self.connection.commit()
        return
    # -> este metodo admite multi master_col
    # -> admite multi row con execute many...
    # | master_col: str >> this col determines the value for perform the comparison on
    # | master_op: str >> str in sqlite query operators. define how to compare the value
    # | master_col_list: list<str>  >> this col determines the value for perform the comparison on
    # | master_op_list: list<str>   >> str in sqlite query operators. define how to compare the value
    # | multi_filter: bool >> determines if using a single col for filtering or many
    # | bulk_updating: bool >> this prop determines if use execute or executemany ...
    # | value: tuple >> the value for set the filter
    # | value_list: list<tuple>  >> the list with values for perform a multi delete in a single  query
    # | join_with: str >> str in sqlite joiners  ...
    default_options = {
        'master_col': None,
        'master_op': None,
        'master_col_list': [None],
        'master_op_list': [None],
        'bulk_updating': False,
        'value': None,
        'join_with': None,
        'value_list': [None],
        'multi-filter': False

    }
    default_options.update(options)

    bulk_updating = default_options.get('bulk_updating')
    multi_filter = default_options.get('multi_filter')
    # for ref purposes--- this props are defined only inside the corresponding branch if executed
    # value = default_options.get('value')
    # value_list = default_options.get('value_list')
    # join_with = default_options.get('join_with')
    # master_col = default_options.get('master_col')
    # master_op = default_options.get('master_op')
    # master_col_list = default_options.get('master_col_list')
    # master_op_list = default_options.get('master_op_list')

    condition_checker(self, all([
        type_checker(self, bulk_updating, bool),
        type_checker(self, multi_filter, bool)
    ]))

    command = 'DELETE FROM ' + table + ' WHERE'

    if multi_filter:
        master_col_list = default_options.get('master_col_list')
        master_op_list = default_options.get('master_op_list')
        join_with = default_options.get('join_with')

        condition_checker(self, join_with in sqlite_logic_joiners)
        type_checker(self, master_op_list, list)
        type_checker(self, master_col_list, list)
        condition_checker(self, all([
            len(master_col_list) == len(self, master_op_list),
            all((type_checker(self, master_col, str) for master_col in master_col_list)),
            all((type_checker(self, master_op, str) for master_op in master_op_list)),
            all((condition_checker(self, master_op in sqlite_query_operators) for master_op in
                 master_op_list))
        ]))

        compound_filter = str.join(
            ' %s ' % join_with,
            (' %s %s ?' % (master_col_list[index], master_op_list[index]) for index in range(len(master_col_list)))
        )

        command = command + compound_filter + ' ;'

    if not multi_filter:
        master_col = default_options.get('master_col')
        master_op = default_options.get('master_op')

        condition_checker(self, all([
            type_checker(self, master_col, str),
            type_checker(self, master_op, str),
            condition_checker(self, master_op in sqlite_query_operators),
        ]))

        command = command + ' ' + master_col + ' ' + master_op + ' ? ;'

    if bulk_updating:
        value_list = default_options.get('value_list')

        condition_checker(self, all([
            type_checker(self, value_list, list),
            condition_checker(self, all(
                (type_checker(self, value_tuple, tuple) for value_tuple in value_list)
            )),
            condition_checker(self, all(
                (type_checker(self, value_tuple, tuple) for value_tuple in value_list)
            )),
            condition_checker(self, all(
                (len(tuple_value) == str.count(command, '?') for tuple_value in value_list)
            ))
        ]))

        # print(command)
        self.cursor.executemany(command, value_list)
        self.connection.commit()
        return

    if not bulk_updating:
        value = default_options.get('value')

        type_checker(self, value, tuple)
        condition_checker(self, len(value) == str.count(command, '?'))

        # print(command)
        self.cursor.execute(command, value)
        self.connection.commit()
        return
    raise Exception('must define bulk_updating property to <bool>')


def crud_driver(self, table, operation, options):
    type_checker(self, options, dict)
    type_checker(self, table, str)
    data = None
    try:
        if self.cursor is not None:
            close_cursor(self)
        initialize_cursor(self)
        if operation == 'create':
            _insert_on_db(self, table, options)
        if operation == 'read':
            _select_on_db(self, table, options)
        if operation == 'update':
            _update_on_db(self, table, options)
        if operation == 'delete':
            _delete_on_db(self, table, options)
        if operation == 'raw_exec':
            # print('debug: ejecutando raw execution with:')
            # print('debug: query: ',options.get('raw_exec'))
            # print('debug: values: ',options.get('value'))
            if any([
                isinstance(options.get('value'), list),
                isinstance(options.get('value'), tuple)
            ]) and len(options.get('value')) > 0:
                self.cursor.execute(options.get('raw_exec'), options.get('value'))
            else:
                self.cursor.execute(options.get('raw_exec'))
    except sqlite3.Error as error:
        # print('error inside crud driver: ', error)
        selfCloseInterface('error on Database Process',alert_level=3,title='DB Error',info=str(error))
        # raise error

    except ConditionFailedException as error2:
        # print(str(error2))
        # alert_on_error = MessageBox(lambda: # print(str(error)), str(error2), 'e', 'DB error')
        # alert_on_error.show()
        raise error2
    finally:
        if operation in ['raw_exec', 'read']:
            data = self.cursor.fetchall()
            close_cursor(self)
            # print('data from %s operation: ' % operation, data)
            return data

        if self.cursor is not None:
            close_cursor(self)


# ----aggregations
def find_total(self, table, slave, master, values, multi_filter=False, regexp=False):
    # this function returns only the first (and unique? ) result
    # so far regexp only works on single filter executions
    type_checker(self, values, tuple)
    total = 0
    operator = '=' if not regexp else 'REGEXP'
    if not multi_filter:
        type_checker(self, master, str)
        raw_execution_string = 'SELECT total(' + slave + ') FROM '+table+' WHERE ' + master + ' '+operator+' ? ;'
        total = crud_driver(self, table, 'raw_exec', {
            'raw_exec': raw_execution_string,
            'value': values
        })
    if multi_filter:
        type_checker(self, master, list)
        master_list = list(map(lambda i: ' '+str(i)+' '+operator+' ?', master))
        suffix = str.join(' AND ', master_list)
        total = crud_driver(self, table, 'raw_exec', {
            'raw_exec': 'SELECT total(' + slave + ') FROM ' + table + ' WHERE ' + suffix + ' ;',
            'value': values
        })
            # todo elaborar mapeo de ulti filter
    # print(total)
    return total[0][0] if total[0][0] is not None else 0
