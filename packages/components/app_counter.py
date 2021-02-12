def update_counter(self):
    old_counter = self.status.get('counter')
    new_counter = old_counter + 1
    self.status.update({'counter': new_counter})
    return

'''
counter logic:
the counter is a text string created by joining
    the session date with format yyyymmdd (no dashes)
    un dash -
    an int var n , that grows as n+1

    * when formatting the string , n should be formatted a secuence of 6 decimal ciphers
    in order to ensure a proper sort and alllows 1*10⁶ ops per session
example: yyyymmdd-nnnnnn   
       : 20210119-0001025
       : 20210119-0401426

el contador es una cadena de texto que se crea con:
    la fecha de la sesion en formato yyyymmdd
    un dash -
    un entero n que va creciendo n+1

    * a la hora de formatear la cadena, el entero se pone como una secuencia de 
    6 lugares, de esa manera aseguramos un sort adecuado, y nos permite  1*10⁶
    operaciones por sesion (fecha) 
ejemplo  yyyymmdd-nnnnnn   
       : 20210119-0001025
       : 20210119-0401426
so we have to create a class prop named self.counter = 0
initialize it on every session to zero, if date changes, if date is the same, no initialize it
with any entry, the props increases in +1 
we also have to create a class prop named  self.last_date
this prop keeps the current date in order to know if we have opened the app many times in a same day
in order to know when to initialze the counter or not. WARNING: always use the actual date, not the session date
because it can be retroactive and can cause errors

every time we enter data to diary, counter must be updated, and saved on the app status (many write and updates)'''

'----------------------------------------------------------------------------------------------'

'''
la logica del contador:

para ello se va a crear una propiedad de clase llamada self.counter = 0
esta propiedad se inicializa a cero y se le va sumando uno con cada entrada
tambien vamos a crear una porp en el status self.last_date que registre la ultima fecha abierta en la aplicacion,
de esta manera podemos mantener control de si la fecha cambia o no

* advertencia, la fecha que se usa en el contador siempre es la fecha real, no puede usarse la de la sesion 
porque puede ser retroactiva y puede dar errores en el registro correcto dl contador

cada vez que se entre una operacion se debe actualizar el contador (n+1)
se guarda en el estado de la aplicacion
el ultimo valor del contador por si se abren dos veces el mismo dia la aplicacion
de esta manera se evita que ell contador se reinicie de manera no deseada


'''


def entry_counter_creator(self):
    # this function only woks on diary entries, so it can be directly coded over this template
    # STEPS:
    #   reads the actual counter, and last_date from status
    #   uses it on the logic (formatting as a string and adds the date)
    #   emits signal for launch counter updating
    # returns

    last_date, counter_value = \
        self.status.get('last_date'), self.status.get('counter')

    entry_counter = '{}-{:06n}'.format(''.join(last_date.split('-')),
                                       counter_value)
    print('debug: entry counter is: {}'.format(entry_counter))
    self.counter_updated_signal.emit()
    return entry_counter

