import sqlite3

from packages.components.status import status_table_template
from packages.modules.crud_sqlite import crud_driver
from packages.modules.db_templates_manager import statusDB_name, connect_toDB, create_tables_onDb


# refactored with crud driver
def status_saver_routine(self,silent=False):
    current_database = self.status.get('connected_to')
    connect_toDB(self, statusDB_name, False, True)
    try:
        # print('debug: attempting to create new table for saving app status')
        create_tables_onDb(self, status_table_template)
    except sqlite3.Error as error:
        print('info: %s' % error)

    self.status.update({'connected_to': current_database})  # if this step is ommited c_to  is appStatus
    crud_driver(self, 'saved_status', 'delete', None)
    crud_driver(self, 'saved_status', 'create', {
        'multi': False,
        'fields': list(self.status.keys()),
        'value': tuple(self.status.values())
    })
    print('status saved....')
    connect_toDB(self, current_database, False, silent)
    return
