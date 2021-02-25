from packages.dialogs.stats_external_dialog import ExternalStatsDialog
from packages.modules.crud_sqlite import crud_driver


def find_totals_untill(self, date):
    print('debug using date: {}'.format(date))
    worked_days = crud_driver(self, 'diary', 'raw_exec', {  # (WD, )
        'raw_exec': 'SELECT COUNT ( DISTINCT date ) FROM diary WHERE date <= ?', 'value': (date,)
    })[0][0] or (0,)[0]
    total_sales, cost_price = crud_driver(self, 'diary', 'raw_exec', {
        'raw_exec': 'SELECT TOTAL(sell_price), TOTAL(price) FROM diary WHERE date <= ? AND is_sale = ?',
        'value': (date, True)})[0] or (0, 0, 0)

    capital, rob, ary = crud_driver(self, 'diary', 'raw_exec', {
        'raw_exec': 'SELECT invested_,robert_,ariadna_  FROM diary WHERE date <= ?', 'value': (date,)
    })[-1] or (0, 0, 0)

    rent = 125.00 # todo ajustar este valor mediante dialogo y almacenarla en app.status.props
    salary = crud_driver(self, 'diary', 'raw_exec', {
        'raw_exec': 'SELECT TOTAL(salary) FROM diary WHERE is_sale = ? AND date = ? ',
        'value': (True, date)})[0][0]
    net_proffit = total_sales - cost_price
    real_proffit = total_sales - rent * worked_days - cost_price - salary
    media_income = real_proffit / worked_days

    data = (total_sales, net_proffit, real_proffit, capital, rob, ary, worked_days, media_income)
    return data


def calculate_totals_on_statistics(self):
    headers = list((item[0] for item in crud_driver(self, 'diary', 'raw_exec', {
        'raw_exec': 'SELECT DISTINCT date FROM diary '})))
    headers.sort()

    data = list((find_totals_untill(self, date) for date in headers))
    return headers, data


def generate_table_all_days_routine(self):
    print(9)


def generate_table_totales(self):
    h_headers, data__ = calculate_totals_on_statistics(self)
    data_name = 'Totales'
    scope__ = self.ui.comboBox_ambito_de_tabla.currentText()
    table_dialog = ExternalStatsDialog(self, h_headers, totals_vertical_header_templates, data__, data_name, scope__)
    table_dialog.exec_()
    return


diary_vertical_headers_template = [
    'Ventas', 'Retorno de la Inversion', 'Ganancias Netas',
    'Salario', 'Renta', 'Ganancias Totales', 'Ganancias de la parte',
    'Compras del Dia', 'Pagos a Consignacion del Dia'
]

totals_vertical_header_templates = [
    'Ventas', 'Ganancias', 'Ganancias Totales', 'Capital Invertido Total',
    'Capital de Robert', 'Capital de Ariadna', 'Dias Trabajados',
    'Promedio de Ganancias por Dia Trabajado'
]

# todo
#  la idea aqui es elaborar una tabla donde los headers sean verticales (una column de headers),
#  esto hace que a la hora de imprimir, se deba revisar el html para que muestre la tabla de manera vertical
#
#  los pasos de la tabla diarios serian:
#     obtener los dias (que seran los headers horizontales de la tabla)
#     [Days, 2021-01-01,2021-01-02] vease que celda(0,0) tiene el valor Days
#     luego en cada row se coloca el header respectivo y se calcula estadisticas por dia
#     para ello debo modificar la funcion de calculo de estaditicas para que trabaje con dias
#     que sean diferentes de el ultimo.
