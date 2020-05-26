from model.hr import hr
from view import terminal as view
from controller import CRUD
from model import data_manager
import datetime


def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def dates_between(date1, date2, date3):
    a = (date1.month, date1.day)
    b = (date2.month, date2.day)
    c = (date3.month, date3.day)
    if a < b < c:
        return True
    else:
        return False

def list_employees():
    CRUD.read(hr.DATAFILE, hr.HEADERS)


def add_employee():
    CRUD.create(hr.DATAFILE, hr.HEADERS)


def update_employee():
    CRUD.update(hr.DATAFILE, hr.HEADERS)


def delete_employee():
    CRUD.delete(hr.DATAFILE, hr.HEADERS)


def get_oldest_and_youngest():
    temp_list = data_manager.read_table_from_file(hr.DATAFILE)
    print('\nYoungest Employee\n')
    sorted_list = []
    for item in temp_list:
        sorted_list.append(item[2])
    sorted_list.sort()
    for item in temp_list:
        for j in item:
            if j == sorted_list[0]:
                print(item[1])

    print('\nOldest Employee\n')
    sorted_list1 = []
    for item in temp_list:
        sorted_list1.append(item[2])
    sorted_list1.sort(reverse= True )
    for item in temp_list:
        for j in item:
            if j == sorted_list1[0]:
                print(item[1])
    print('\n')

def get_average_age():
    temp_list = data_manager.read_table_from_file(hr.DATAFILE)
    birthdays = []
    dates = []
    ages = []
    x = 0
    for item in temp_list:
        birthdays.append(item[2])
    for item in birthdays:
        dates.append(datetime.datetime.strptime(item, "%Y-%M-%d").date())
    for item in dates:
        ages.append(calculate_age(item))
    for i in range(len(ages)):
        x += ages[i]
    avg = x/len(ages)
    print('\nAvarage Age is : \n')
    print(avg)


def next_birthdays():
    temp_list = data_manager.read_table_from_file(hr.DATAFILE)
    dates = []
    bdays = []
    today = (datetime.datetime.today()).date()
    two_weeks = (datetime.timedelta(days=14) + datetime.datetime.today()).date()
    for item in temp_list:
        dates.append(item[2])
    for item in dates:
        bdays.append(datetime.datetime.strptime(item, "%Y-%m-%d").date())
    print('\nBirthdays in the next two weeks: \n')
    for i in range(len(bdays)):
        if dates_between(today, bdays[i], two_weeks):
            for item in temp_list:
                if datetime.datetime.strptime(item[2], "%Y-%m-%d").date() == bdays[i]:
                    print(item[1], bdays[i])


def count_employees_with_clearance():
    temp_list = data_manager.read_table_from_file(hr.DATAFILE)
    user_input = input('\nSelect Clearance Level: ')
    count = 0
    for item in temp_list:
        if item[4] == str(user_input):
            count += 1
    print('\nNumber of employees with clearance level ',user_input,' is :',count)


def count_employees_per_department():
    temp_list = data_manager.read_table_from_file(hr.DATAFILE)
    deps = {}
    for item in temp_list:
        if item[3] in deps:
            deps[item[3]] += 1
        else:
            deps[item[3]] = 1
    for key,value in deps.items():
        print(key,': ',value)



def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)