from simialex.com.github.controller import CRUD
from datetime import datetime

def print_menu(title, list_options):
    print(title,'\n')
    for i in range(len(list_options)):
        print(str(i)+') '+list_options[i])


def print_message(message):
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


def print_table(list, HEADERS):
    alist = []
    list_of_max_col = []
    if len(HEADERS) == 5:
        for i in range (len(list[0])):
            alist.append(len(HEADERS[i]))
            for item in list:
                alist.append(len(item[i]))
            list_of_max_col.append(max(alist))
            alist.clear()

        print('-' * (sum(list_of_max_col) + 16))
        print('|',HEADERS[0].center(list_of_max_col[0]), '|',HEADERS[1].center(list_of_max_col[1]), '|',HEADERS[2].center(list_of_max_col[2]), '|',HEADERS[3].center(list_of_max_col[3]), '|',HEADERS[4].center(list_of_max_col[4]), '|')
        print('-' * (sum(list_of_max_col) + 16))
        for item in list:
            print('|',item[0].ljust(list_of_max_col[0]), '|',item[1].ljust(list_of_max_col[1]), '|',item[2].ljust(list_of_max_col[2]), '|',item[3].ljust(list_of_max_col[3]), '|',item[4].ljust(list_of_max_col[4]), '|')
        print('-' * (sum(list_of_max_col) + 16))
    else:
        for i in range (len(list[0])):
            alist.append(len(HEADERS[i]))
            for item in list:
                alist.append(len(item[i]))
            list_of_max_col.append(max(alist))
            alist.clear()

        print('-' * (sum(list_of_max_col) + 13))
        print('|',HEADERS[0].center(list_of_max_col[0]), '|',HEADERS[1].center(list_of_max_col[1]), '|',HEADERS[2].center(list_of_max_col[2]), '|',HEADERS[3].center(list_of_max_col[3]), '|')
        print('-' * (sum(list_of_max_col) + 13))
        for item in list:
            print('|',item[0].ljust(list_of_max_col[0]), '|',item[1].ljust(list_of_max_col[1]), '|',item[2].ljust(list_of_max_col[2]), '|',item[3].ljust(list_of_max_col[3]), '|')
        print('-' * (sum(list_of_max_col) + 13))

def get_input(label):
    return input(label)


def get_inputs(labels):
    list_of_inputs = []
    for item in labels:
        while True:
            user_input = input(f'Enter {item} ')
            input_list = list(user_input)
            if item == 'Name' or item == 'Department' or item == 'Customer':
                name_input = user_input.replace(' ','')
                if name_input.isalpha():
                    list_of_inputs.append(user_input)
                    break
                else:
                    print('Invalid Input!')
                    continue
            elif item == 'Email':
                if '@' in input_list and '.' in input_list and input_list.index('@') < input_list.index('@') + 1 < input_list.index('.') and input_list[-1] != '.':
                    list_of_inputs.append(user_input)
                    break
                else:
                    print('Invalid Email!')
                    continue
            elif item == 'subscribed':
                valid_inputs = ['0','1']
                if user_input in valid_inputs:
                    list_of_inputs.append(user_input)
                    break
                else:
                    print('Invalid Input')
                    continue
            elif item == 'Date of birth' or item == 'Date':
                if CRUD.validate(user_input):
                    list_of_inputs.append(user_input)
                    break
                else:
                    print('Invalid input')
                    continue
            elif item == 'Clearance':
                valid = ['0','1','2','3','4','5','6','7']
                if user_input in valid:
                    list_of_inputs.append(user_input)
                    break
                else:
                    print('Invalid Input')
                    continue
            elif item == 'Price':
                try:
                    float(user_input)
                    list_of_inputs.append(user_input)
                    break
                except ValueError:
                    print('Invalid Input')
                    continue
            else:
                list_of_inputs.append(user_input)
                break

    return list_of_inputs

def print_error_message(message):
    print(message)