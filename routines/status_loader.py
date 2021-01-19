from modules.crud_sqlite import crud_driver
from modules.db_templates_manager import connect_toDB, statusDB_name


def status_loader_routine(self):
    print('loading previous status....')
    try:
        connect_toDB(self, statusDB_name, False, True)
        status = crud_driver(self, 'saved_status', 'read', {'pick_all': True})
        print('done.....')
        connect_toDB(self, status[-1][0],True,False)
        return dict(list(zip(status_props,status[-1])))
    except BaseException as err:
        print('not found....\nreturning default values')
        return dict(list(zip(status_props, initial_values)))


status_props = ['connected_to', 'active_tab', 'width', 'height']
initial_values = ['cellsDB.db', 0, 1000, 650]

# ~~~~~~~~~~~~~~~~~~~~4
