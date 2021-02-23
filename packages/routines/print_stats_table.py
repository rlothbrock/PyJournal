from PySide2 import QtGui

from packages.components.data_printer import data_printer
from packages.components.status import current_date
from packages.modules.accountant import calculate_statistics


def draw_printable(data):
    map_data = tuple(map(
        lambda item: '${:,.2f}'.format(item) if isinstance(item,float) else item ,
        data
    ))
    stats_html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        .bordered {
            border-width: 1px;
            border-style: solid;
            border-color: black;
            padding: 5px;
        }'''+'''
    </style>
</head>
<body>
    <div>
        <h1> Resumen Estadistico</h1>
        <h4>Solicitado con fecha {}</h4>
        <hr>
        <div class="bordered">
            <p> Capital Total en el negocio: {}</p>
            <p> Capital Invertido en el negocio: {}</p>
            <p> Capital en efectivo en el negocio: {}</p>
        </div>
        <h3> Estadisticas del día</h3>
        <div>
            <div class="bordered">
                <p> Ventas del dia: {}</p>
                <p> Retorno de inversion del dia: {}</p>
                <p> Ganancias netas del dia: {}</p>
                <p> Salario del dia: {}</p>
                <p> Renta del dia: {}</p>
                <p> Ganancias totales del dia: {}</p>
                <p> Ganancias de parte del dia: {}</p>
                <p> Compras del dia: {}</p>
                <p> Pagos a Consignacion del dia: {}</p>
            </div>
        <h3> Acumulados</h3>

            <div class="bordered">
                <p> Ventas: {}</p>
                <p> Ganancias: {}</p>
                <p> Ganancias Reales: {}</p>
                <p> Capital invertido: {}</p>
                <p> Capital de Robert: {}</p>
                <p> Capital de Ariadna: {}</p>
                <p> Dias trabajados: {}</p>
                <p>Promedio de Ganancias por Dias Trabajados: {}</p>
            </div>
        </div>


    </div>
    <br>
    <hr>
    <div>
    <footer>
        <small> printed using <b>PyJournal&copy;</b> on: {} </small>
    </footer></div>
</body>
</html>
    '''.format(
        current_date,
        *map_data,
        current_date)
    printable_template = QtGui.QTextDocument()
    printable_template.setHtml(stats_html)
    return printable_template


def print_stats_table_routine(self):
    data__ = calculate_statistics(self)
    data_printer(self,data__,draw_printable)
    


