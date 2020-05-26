from simialex.com.github.model import data_manager
from simialex.com.github.view import terminal as view
from simialex.com.github.model import util
from datetime import datetime

def read(datafile, headers):
    temp_list = data_manager.read_table_from_file(datafile)
    # temp_list.insert(0,headers)
    view.print_table(temp_list, headers)


def create(datafile, headers):
    temp_list = data_manager.read_table_from_file(datafile)
    temp_list.append(view.get_inputs(headers[1:]))
    id = util.generate_id()
    last_list = temp_list[len(temp_list) - 1]
    last_list.insert(0, id)
    data_manager.write_table_to_file(datafile, temp_list)


def update(datafile, headers):
    temp_list = data_manager.read_table_from_file(datafile)
    row = view.get_inputs(headers)
    marker = 0
    for i in range(len(temp_list)):
        if temp_list[i][0] == row[0]:
            marker += 1
            temp_list[i] = row
            data_manager.write_table_to_file(datafile, temp_list)
            view.print_message('Update successful')
            break
    if marker == 0:
        view.print_error_message('Update failed')


def delete(datafile, headers):
    temp_list = data_manager.read_table_from_file(datafile)
    item_to_delete = view.get_input("Please enter an id to delete ")
    marker = 0
    for item in temp_list:
        if item_to_delete == item[0]:
            temp_list.remove(item)
            data_manager.write_table_to_file(datafile, temp_list)
            view.print_message('Delete successful')
            marker += 1
            break
    if marker == 0:
        view.print_error_message('Delete failed')

def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False