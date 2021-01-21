# this module handles the auxiliar tables (sales, stock, statistics, )
from modules.crud_sqlite import crud_driver
from modules.db_templates_manager import get_index_in_template as g_i


def get_diary_data(self):
    return crud_driver(self,'diary','read',{'pick_all': True})


def calculate_auxiliar_tabs(self):
    print('recalculating auxiliar tables...')
    calculate_sales(self)
    calculate_stock(self)
    calculate_capital(self)
    calculate_statistics(self)
    return

def calculate_sales(self):
    # steps:
    #   get the data (diary)
    #   get the necessary fields
    #   create the [tuple...]
    #   make a bulk insertion.

    diary_data = get_diary_data(self)


    pass

def calculate_stock(self):
    pass

def calculate_capital(self):
    pass

def calculate_statistics(self):
    pass