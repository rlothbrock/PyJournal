import datetime
import os

from PySide2.QtWidgets import QFileDialog
from packages.components.app_counter import entry_counter_creator
from packages.dialogs.auxiliar_dialogs import selfCloseInterface
from packages.modules.crud_sqlite import crud_driver
from packages.modules.db_templates_manager import table_templates, get_index_in_template, get_template_fields


# possible args:
# data_target: 'diary',
# field_to_change: 'entry_counter'
# data_pipe: entry_counter_creator.
def transform_imported_data(
        self,
        data_destination: str,
        field_to_change: str,
        data_pipe
):
    # this block adds a new entry counter ,even if it already has
    data_to_transform, value_to_update, field_index_to_update = \
        self.imported_data.copy(), \
        data_pipe(self), \
        get_index_in_template(data_destination, field_to_change)
    for tuple_index, data_tuple in enumerate(data_to_transform):
        t_row = list(data_tuple)
        t_row[field_index_to_update] = value_to_update
        data_to_transform[tuple_index] = tuple(t_row)
    self.imported_data = data_to_transform.copy()
    return


def import_data(self, with_headers=True):
    # this functions reads the file and retrieves data as structured array to self.imported_data property
    # print('preparing for importing...')
    filename = QFileDialog.getOpenFileName(self, 'Open CSV File: ', os.pardir, '*.csv')
    # print('collecting data from {}'.format(filename))
    data_to_import = open(filename[0]).readlines()
    contents = data_to_import[1:] if not with_headers else data_to_import
    imported_data = list((tuple(content_.split('\n')[0].split(';')) for content_ in contents))
    self.imported_data = imported_data.copy()
    return


def export_data(self, source=None, with_headers=True):
    global dst
    # this function returns the name of destination for the alert in further pipe
    db_group = self.status.get('connected_to').split('.')[0]
    exported_table_filename = 'exported {}-{}-{}.csv'.format(
        db_group,
        self.table_on_target,
        datetime.datetime.now().__str__().replace('-', '').replace(' ', '-').replace('.', '').replace(':', '')
    )
    default_source = os.path.join(os.pardir, 'Exported Tables')

    try:
        dst = QFileDialog.getExistingDirectory(
            self, 'Select Export Folder:', default_source
        )
        if len(dst) == 0: raise Exception('no dst')
        dst = os.path.join(dst, exported_table_filename)
    except:
        # tries to create folder
        try:
            os.mkdir(default_source)
        except FileExistsError as error:
            print('info on saving dir: %s' % error)
        try:
            saving_dir = os.path.join(default_source, db_group)
            os.mkdir(saving_dir)
        except FileExistsError as error:
            print('info on saving dir child: %s' % error)
        dst = os.path.join(default_source, db_group, exported_table_filename)
    finally:
        try:
            prime_data = self.data_to_export if source is None else source
            data = csv_data_maker(self, prime_data, with_headers)
            exported_file = open(dst, 'w')
            exported_file.write(data)
            exported_file.close()
            return dst
        except FileNotFoundError as fileError:
            raise Exception(fileError)


def csv_data_maker(self, data, with_headers=True):
    csv_string = csv_header_builder(self) if with_headers else ''
    for row in data:
        quoted_fields = ('"%s"' % field if isinstance(field, str) else '%s' % field for field in row)
        csv_string = csv_string + str.join(';', list(quoted_fields)) + '\n'
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
    # print('table: {}, header:{}'.format(table_name, header))
    return header


# dedicated imports functions

def import_data_to_diary(self):
    try:
        import_data(self, False)  # imports the data and writes the array self.imported_data
        transform_imported_data(self,'diary','entry_counter',entry_counter_creator)
        data_to_import = self.imported_data.copy()
        crud_driver(self,'diary','create',{
            'fields': get_template_fields('diary'),
            'value_list': data_to_import,
            'multi': True
        })
        self.display_table_signal.emit()
        selfCloseInterface('Data imported to Diary Table', 3, 1, 'Import Success')
        return
    except BaseException as error:
        selfCloseInterface('Failed on Importing Data to Diary Table', 3, 2, 'Import Failed',str(error))
        print('failed import of data')
        raise error


def export_data_from_diary(self):
    # steps:
    # 1- read the diary table
    # 2- export the data using export function.
    try:
        filename_path = export_data(self, crud_driver(self, 'diary', 'read', {'pick_all': True}))
        print('data saved on {}'.format(filename_path))
        selfCloseInterface('Diary Table Data Exported ', 6, 1, 'Export Success',
                           'Data saved on: {}'.format(filename_path))
        return
    except BaseException as error:
        print('export failed : {}'.format(error))
        selfCloseInterface('Failed on Exporting Data from Diary Table', 4, 2, 'Export Failed')
        raise Exception(error)


def export_data_displayed_on_tab1(self):
    try:
        filename_path = export_data(self, self.data_to_display_on_tab1.copy() )
        print('data saved on {}'.format(filename_path))
        selfCloseInterface('Diary Table Data Exported ', 6, 1, 'Export Success',
                           'Data saved on: {}'.format(filename_path))
        return
    except BaseException as error:
        print('export failed : {}'.format(error))
        selfCloseInterface('Failed on Exporting Data from Diary Table', 4, 2, 'Export Failed')
        raise Exception(error)

