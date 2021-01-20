import datetime
import os

from PySide2.QtWidgets import QFileDialog

from dialogs.auxiliar_dialogs import MessageBox, selfCloseInterface
from modules.db_templates_manager import table_templates


# raw imports/exports returns data/or file but always silent

def import_data(self, with_headers=True):
    # this functions reads the file and retrieves data as structured array to self.imported_data property
    print('preparing for importing...')
    filename = QFileDialog.getOpenFileName(self, 'Open CSV File: ', os.pardir, '*.csv')
    print('collecting data from {}'.format(filename))
    data_to_import = open(filename[0]).readlines()
    contents = data_to_import[1:] if not with_headers else data_to_import
    # todo delete all this prints after debugging phase **
    print('contents: ', contents)  # todo **
    imported_data = list((tuple(content_.split('\n')[0].split(';')) for content_ in contents))
    print('val_list: ', imported_data)  # todo **
    self.imported_data = imported_data
    return


def export_data(self, source=None, with_headers=True):
    # this function returns the name of destination for the alert in further pipe
    db_group = self.status.get('connected_to').split('.')[0]
    exported_table_filename = 'exported {}-{}-{}.csv'.format(
        db_group,
        self.table_on_target,
        datetime.datetime.now().__str__().replace('-', '').replace(' ', '-').replace('.', '').replace(':', '')
    )
    # tries to crate folder
    try:
        saving_dir = os.path.join(os.pardir, 'Exported Tables')
        os.mkdir(saving_dir)
    except FileExistsError as error:
        print('info on saving dir: %s' % error)
    try:
        saving_dir = os.path.join(os.pardir, 'Exported Tables', db_group)
        os.mkdir(saving_dir)
    except FileExistsError as error:
        print('info on saving dir child: %s' % error)
    try:
        prime_data = self.data_to_export if source is None else source
        data = csv_data_maker(self, prime_data, with_headers)
        dst = os.path.join(os.pardir, 'Exported Tables', db_group, exported_table_filename)
        exported_file = open(dst,'w')
        exported_file.write(data)
        exported_file.close()
        return dst
    except FileNotFoundError as fileError:
        raise Exception(fileError)


def csv_data_maker(self, data, with_headers = True):
    csv_string = csv_header_builder(self) if with_headers else ''
    for row in data:
        quoted_fields = ('"%s"' % field if isinstance(field, str) else '%s' % field for field in row)
        csv_string = csv_string+str.join(';', list(quoted_fields))+'\n'
    print('csv_string:{}'.format(csv_string)) # todo erase this line after debug
    return csv_string


def csv_header_builder(self):
    table_name = self.table_on_target
    table_dict = None
    for table_ in table_templates:
        if table_.get('name') == table_name:
            table_dict = table_
            break
    header = ';'.join('"%s"' % field.get('name') for field in table_dict.get('fields')) \
        if table_dict is not None else ''
    header += '\n'
    print('table: {}, header:{}'.format(table_name, header))
    return header

# dedicated imports functions

def import_data_to_diary(self):
    # steps:
    # 1- import the data itlself
    # 2- append the data to the array
    #  the data must be added as a bulk insertion to the table
    #  in order to data get entry_count property
    # 5- sort the information, as a part of the bulk insertion
    try:
        import_data(self, False)
        # todo... not finished, check the steps
        selfCloseInterface('Data imported to Diary Table',3,1,'Import Success')
        return
    except BaseException as error:
        selfCloseInterface('Failed on Importing Data to Diary Table',3,2,'Import Failed')
        print('failed raw import of data')
        raise error
    # todo create a bulk insertion process on table diary
    # todo emit an autocloseable alert showing success


def export_data_from_diary(self):
    # steps:
    # 1- read the diary table
    # 2- export the data using export function.
    try:
        filename_path = export_data(self, self.diary_list)
        print('data saved on {}'.format(filename_path))
        selfCloseInterface('Diary Table Data Exported ', 3, 1, 'Export Success',
                           'Data saved on: {}'.format(filename_path))
        return
    except BaseException as error:
        print('export failed : {}'.format(error))
        selfCloseInterface('Failed on Exporting Data from Diary Table', 3, 2, 'Export Failed')
        raise Exception(error)


