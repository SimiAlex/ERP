from simialex.com.github.model.crm import crm
from simialex.com.github.view import terminal as view
from simialex.com.github.controller import CRUD
from simialex.com.github.model import data_manager


def list_customers():
    CRUD.read(crm.DATAFILE, crm.HEADERS)


def add_customer():
    CRUD.create(crm.DATAFILE, crm.HEADERS)


def update_customer():
    CRUD.update(crm.DATAFILE, crm.HEADERS)


def delete_customer():
    CRUD.delete(crm.DATAFILE, crm.HEADERS)


def get_subscribed_emails():
    temp_list = data_manager.read_table_from_file(crm.DATAFILE)
    print('Subscribed Customers emails')
    for item in temp_list:
        if item[3] == '1':
            print(item[2])


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)