import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    a = random_small_letters(number_of_small_letters)
    b = random_digits(number_of_digits)
    c = random_chars(number_of_special_chars, allowed_special_chars)
    d = random_capital_letters(number_of_capital_letters)
    result = a + b + c + d
    result_list = list(result)
    random.shuffle(result_list)
    final = ''.join(item for item in result_list)
    return final

def random_small_letters(string_lenght):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range (string_lenght))

def random_capital_letters(string_lenght):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range (string_lenght))

def random_digits(number):
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(number))

def random_chars(number, allowed_special_chars):
    chars_list = []
    for i in list(allowed_special_chars):
        chars_list.append(i)
    x = random.randint(0, (len(chars_list) - 1))
    return ''.join(chars_list[x] for i in range(number))