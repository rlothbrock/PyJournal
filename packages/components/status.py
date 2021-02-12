import datetime

current_date = datetime.datetime.now().__str__().split(' ')[0]

default_status = {
    'connected_to': 'cellsDB.db',
    'active_tab': 0,
    'width': 1000,
    'height': 650,
    'counter': 0,
    'last_date': current_date
}

status_props = list(default_status.keys())
initial_values = list(default_status.values())

z = [
    'cellsDB.db', 0, 1000, 650, 0,
    datetime.datetime.now().__str__().split(' ')[0]
]

status_table_template = ['''CREATE TABLE saved_status (
                connected_to TEXT ,
                active_tab INTEGER,
                width INTEGER,
                height INTEGER,
                counter INTEGER,
                last_date TEXT)
                ''']
