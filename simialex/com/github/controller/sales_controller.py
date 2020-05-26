from simialex.com.github.model.sales import sales
from simialex.com.github.view import terminal as view
from simialex.com.github.model import data_manager
from simialex.com.github.controller import CRUD
from datetime import datetime


def list_transactions():
    CRUD.read(sales.DATAFILE, sales.HEADERS)


def add_transaction():
    CRUD.create(sales.DATAFILE, sales.HEADERS)


def update_transaction():
    CRUD.update(sales.DATAFILE, sales.HEADERS)


def delete_transaction():
    CRUD.delete(sales.DATAFILE, sales.HEADERS)


def get_biggest_revenue_transaction():
    temp_list = data_manager.read_table_from_file(sales.DATAFILE)
    revenues = []
    for item in temp_list:
        revenues.append(float(item[3]))
    max_revenue_index = revenues.index(max(revenues))
    id = 0
    id_max_revenue_transaction = temp_list[max_revenue_index][id]
    view.print_message(f'\nBiggest revenue transaction is {id_max_revenue_transaction}')


def get_biggest_revenue_product():
    temp_list = data_manager.read_table_from_file(sales.DATAFILE)
    revenues = []
    for item in temp_list:
        revenues.append(float(item[3]))
    max_revenue_index = revenues.index(max(revenues))
    id = 2
    id_max_revenue_transaction = temp_list[max_revenue_index][id]
    view.print_message(f'\nBiggest revenue product is {id_max_revenue_transaction}')


def count_transactions_between():
    temp_list = data_manager.read_table_from_file(sales.DATAFILE)
    start_date = view.get_input('Enter start date YYYY-MM-DD and press enter ')
    while not CRUD.validate(start_date):
        start_date = view.get_input('Enter start date YYYY-MM-DD and press enter ')
        CRUD.validate(start_date)
    end_date = view.get_input('Enter end date YYYY-MM-DD and press enter ')
    while not CRUD.validate(end_date):
        end_date = view.get_input('Enter end date YYYY-MM-DD and press enter ')
        CRUD.validate(end_date)
    counter = 0
    for item in temp_list:
        if start_date <= item[4] <= end_date:
            counter += 1
    view.print_message(f'The number of transactions between {start_date} and {end_date} is {counter}')


def sum_transactions_between():
    temp_list = data_manager.read_table_from_file(sales.DATAFILE)
    start_date = view.get_input('Enter start date YYYY-MM-DD and press enter ')
    while not CRUD.validate(start_date):
        start_date = view.get_input('Enter start date YYYY-MM-DD and press enter ')
        CRUD.validate(start_date)
    end_date = view.get_input('Enter end date YYYY-MM-DD and press enter ')
    while not CRUD.validate(end_date):
        end_date = view.get_input('Enter end date YYYY-MM-DD and press enter ')
        CRUD.validate(end_date)
    sum = 0
    for item in temp_list:
        if start_date <= item[4] <= end_date:
            sum += float(item[3])
    view.print_message(f'The sum of transactions between {start_date} and {end_date} is {sum}')


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum number of transactions between"]
    view.print_menu('\nSales', options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
