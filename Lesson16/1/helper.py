#  1. Написать два модуля. Один, модуль helper, куда поместить несколько функций: 
# - функция get_random_list(n, a, b) для генерации списка из n случайных чисел в заданном диапазоне (a, b); 
# - функция get_random_password(n) генерации пароля - формирует пароль из n символов - буквы, большие, маленькие, цифры; 
# - функция подсчет слов в тексте get_words_count(text)
# - функция получения списка слов (без знаков препинания и тп) get_words(file_name) из файла.
# В каждой функции указать doc-строку.
# Если модуль запускается на выполнение, печатать название каждой функции и ее doc строку.
# Второй модуль - main. В нем импортировать модуль helper и вызывать функци, выводить на печать результат.

import string
import random

def get_random_list(n=2, a=1, b=10):
    """функция get_random_list(n, a, b) 
    для генерации списка из n случайных чисел в заданном диапазоне (a, b); 
    """
    lst = [random.randint(a, b) for _ in range(n)]
    return lst


def get_random_password(n=12):
    """функция get_random_password(n) генерации пароля 
    формирует пароль из n символов - буквы, большие, маленькие, цифры;
    """
    lst = string.ascii_letters + string.digits
    passwd = [random.choice(lst) for _ in range(n)]
    passwd = ''.join(passwd)
    return passwd
    

def get_words_count(text='hello word'):
    """функция  get_words_count для подсчет слов в тексте
    """
    lst = list(text.split(' '))
    return len(lst)


def get_words(file_name='app2.log'):
    """функция get_words(file_name) для получения списка слов (без знаков препинания и тп) из файла 
    """
    count = 0
    with open (file_name, 'r') as file:
        for line in file:
            lst = list(line.strip().split(' '))  # у меня не работает strip(',.!:?')
            count += len(lst)
    return count


if __name__ == "__main__":
    print(get_random_list.__name__,  get_random_list.__doc__)
    print(get_random_password.__name__, get_random_password.__doc__)
    print(get_words_count.__name__, get_words_count.__doc__)
    print(get_words.__name__, get_words.__doc__)