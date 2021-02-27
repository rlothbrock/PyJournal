import datetime

current_date = datetime.datetime.now().__str__().split(' ')[0]

default_status = {
    'connected_to': 'cellsDB.db',
    'active_tab': 0,
    'width': 1000,
    'height': 650,
    'counter': 0,
    'last_date': current_date,
    'exc_rate': 1.0,
    'daily_rent': 125.0,
    'salary_rate': 10,
    'rate_over': 1    # (fixed_rate: 0, rate_over_sales: 1, rate_over_proffit: 2)
}

status_props = list(default_status.keys())
initial_values = list(default_status.values())
status_table_template = ['''CREATE TABLE saved_status (
                connected_to TEXT ,
                active_tab INTEGER,
                width INTEGER,
                height INTEGER,
                counter INTEGER,
                last_date TEXT,
                exc_rate REAL,
                daily_rent REAL,
                salary_rate REAL,
                rate_over INTEGER
                )
                ''']
