import datetime
import os
import shutil

from packages.dialogs.auxiliar_dialogs import selfCloseInterface


def database_saver_routine(self, silent=False):
    database_name, saving_date, suffix = self.status.get("connected_to").split('.')[0], \
                                         datetime.datetime.now().__str__() \
                                             .replace('-', '') \
                                             .replace(' ', '-') \
                                             .replace('.', '-') \
                                             .replace(':', ''), 'Saved-'
    try:
        saving_dir = os.path.join(os.pardir, 'saved databases')
        os.mkdir(saving_dir)
    except FileExistsError as error:
        print('info: on saving dir: %s' % error)
    try:
        saving_dir = os.path.join(os.pardir, 'saved databases', database_name)
        os.mkdir(saving_dir)
    except FileExistsError as error:
        print('warning on saving dir child: %s' % error)
    try:
        src = os.path.join(os.curdir, 'databases',  '{}.db'.format(database_name))
        dst = os.path.join(
            os.pardir,
            'saved databases',
            database_name,
            '{}-{}-{}'.format(suffix, database_name, saving_date)
        )
        shutil.copy(src, dst)
        if not silent:
            selfCloseInterface(
            'Database {} guardada en {}'.format(database_name,dst),
            title='Base de Datos Guardada')
    except FileNotFoundError as fileError:
        print('error: %s' % fileError)
        selfCloseInterface('Fallo a la hora de guardar la base de datos',
                           title='Salva Fallida', alert_level=2)
        # no_db_alert = MessageBox(
        #     lambda: print('error: %s' % fileError),
        #     'the saving process has failed!!',
        #     'e',
        #     'DB Saving Failed',
        #     str(fileError)
        # )
        # no_db_alert.show()
        return
