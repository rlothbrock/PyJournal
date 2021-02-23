def generate_table_all_days_routine(self):
    print(9)

def generate_table_totales(self):
    print(12)




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