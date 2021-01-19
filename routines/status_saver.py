import sqlite3

from modules.crud_sqlite import crud_driver
from modules.db_templates_manager import close_connection, statusDB_name, connect_toDB, create_tables_onDb

status_query = ['''CREATE TABLE saved_status (
                connected_to TEXT ,
                active_tab INTEGER,
                width INTEGER,
                height INTEGER )
                ''']


# def pick_status(self):
#     initial_status = {}
#     print('attempting to load previous status...')
#     if self.connection is not None:
#         db.close_connection(self)
#     if self.cursor is not None:
#         db.close_cursor(self)
#     db.create_connection(self, actions.statusDB)
#     # saved_status = db.cursor_execution(
#     #     self,
#     #     ['SELECT * FROM saved_status'],
#     #     'select',
#     #     False,
#     #     'status loaded....')
#     saved_status = crud_driver(self, 'saved_status', 'read', {
#         'pick_all': True
#     })
#     if len(saved_status) > 0:
#         print('returning saved status')
#         index = (len(saved_status) - 1)
#         status_data_tuple = saved_status[index]
#         gen = (value for value in status_data_tuple)
#         for key in status_props:
#             initial_status.update({key: next(gen)})
#     else:
#         init_val_gen = (key for key in initial_values)
#         for key in status_props:
#             initial_status.update({key: next(init_val_gen)})
#     db.close_connection(self)
#     return initial_status


# refactored with crud driver
def status_saver_routine(self):
    current_database = self.status.get('connected_to')
    print('debug: conectando a la database statusDB')
    connect_toDB(self, statusDB_name, False, True)
    try:
        print('debug: attempting to create new table for saving app status')
        create_tables_onDb(self, status_query)
    except sqlite3.Error as error:
        print('fail on creating table')
        print('info: %s' % error)

    self.status.update({'connected_to': current_database})  # if this step is ommited c_to  is appStatus
    crud_driver(self, 'saved_status', 'delete', None)
    crud_driver(self, 'saved_status', 'create', {
        'multi': False,
        'fields': list((field for field in self.status.keys())),
        'value': tuple((value for value in self.status.values()))
    })
    print('status saved....')
    print('changing connection to: ', current_database)
    connect_toDB(self, current_database, False, False)
    return
