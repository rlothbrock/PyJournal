from packages.components.status import current_date
from packages.dialogs.auxiliar_dialogs import selfCloseInterface
from packages.modules.accountant import calculate_statistics
from packages.modules.data_import_export import set_export


def display_statistics_on_tab(self):
    data = calculate_statistics(self)
    self.ui.label_plac_capital_total.setText('$ {:,.2f}'.format(data[0]))
    self.ui.label_plac_capital_invertido.setText('$ {:,.2f}'.format(data[1]))
    self.ui.label_plac_cash_en_caja.setText('$ {:,.2f}'.format(data[2]))
    self.ui.label_plac_day_ventas.setText('$ {:,.2f}'.format(data[3]))
    self.ui.label_plac_day_inversion.setText('$ {:,.2f}'.format(data[4]))
    self.ui.label_plac_day_net_proffit.setText('$ {:,.2f}'.format(data[5]))
    self.ui.label_plac_day_salary.setText('$ {:,.2f}'.format(data[6]))
    self.ui.label_plac_day_rent.setText('$ {:,.2f}'.format(data[7]))
    self.ui.label_plac_day_real_proffit.setText('$ {:,.2f}'.format(data[8]))
    self.ui.label_plac_day_part_proffit.setText('$ {:,.2f}'.format(data[9]))
    self.ui.label_plac_day_compras.setText('$ {:,.2f}'.format(data[10]))
    self.ui.label_plac_total_ventas.setText('$ {:,.2f}'.format(data[11]))
    self.ui.label_plac_total_net_proffit.setText('$ {:,.2f}'.format(data[12]))
    self.ui.label_plac_total_real_proffit.setText('$ {:,.2f}'.format(data[13]))
    self.ui.label_plac_total_capital_low.setText('$ {:,.2f}'.format(data[14]))
    self.ui.label_plac_total_rob_capital.setText('$ {:,.2f}'.format(data[15]))
    self.ui.label_plac_total_ary_capital.setText('$ {:,.2f}'.format(data[16]))
    self.ui.label_plac_day_consignation.setText('$ {:,.2f}'.format(data[17]))
    self.ui.label_plac_total_dias_trabajados.setText('{:n}'.format(data[18]) or '0')
    self.ui.label_plac_total_gan_per_day.setText('$ {:,.2f}'.format(data[19]))


def export_statistics_page(self):
    data = calculate_statistics(self)
    try:
        filename_path = set_export(
            self, [data], True,
            '{} exported statistics.csv'.format(current_date),
            ['Capital Total en el negocio','Capital Invertido','Efectivo','Ventas','Retorno de la inversion','Ganancias Netas',
             'Salario','Renta','Ganancias Totales','Ganancias de la parte',
             'Compras del dia', 'Pagos a Consignacion del dia','Ventas',
             'Ganancias','Ganancias Reales','Capital Invertido Total',
             'Capita de Robert', 'Capital de Ariadna', 'Dias Trabajados',
             'Promedio de Ganancias por Dia Trabajado']
        )
        if filename_path is None:
            return
        else:
            print('data saved on {}'.format(filename_path))
            selfCloseInterface('Diary Table Data Exported ', 6, 1, 'Export Success',
                               'Data saved on: {}'.format(filename_path))
            return
    except BaseException as error:
        print('export failed : {}'.format(error))
        selfCloseInterface('Failed on Exporting Data from Diary Table', 4, 2, 'Export Failed')
        raise Exception(error)
