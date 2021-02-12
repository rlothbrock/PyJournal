from packages.components.app_counter import entry_counter_creator
from packages.components.data_display_tab import execute_display_table
from packages.modules.crud_sqlite import crud_driver
from packages.modules.db_templates_manager import get_index_in_template, get_template_fields
from packages.routines.create_unique_id import unique_id_creator


def append_data_to_diary_routine(self,data):
    data[get_index_in_template('diary','entry_counter')] = entry_counter_creator(self)
    data[get_index_in_template('diary','id')] = unique_id_creator(self)
    data[get_index_in_template('diary','unique_id')] = unique_id_creator(self)
    crud_driver(self,'diary','create',{
        'multi': False,
        'fields': get_template_fields('diary'),
        'value': tuple(data)
    })
    self.recalculate_tables_signal.emit()
    execute_display_table(self, 'diary')
    return
