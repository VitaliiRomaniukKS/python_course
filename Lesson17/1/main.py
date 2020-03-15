# 1. Написать два модуля.
# Первый checkers.py, содержит функции проверки - имени(check_name), даты рождения(check_bdate), 
# а также функцию test без параметров. (Функция test вызывается в случае запуска модуля в интерпретаторе, 
# в ней происходит вызов каждой описанной в модуле функции с корректными значениями). Функции check_name, 
# check_bdate проверяют корректность переданных аргументов и кидают исключения с текстом, если что-то не соответствует норме.
# 
# Второй модуль - main.py, импортирует модуль проверок checkers и просит пользователя ввести имя, 
# год, месяц, день рождения и проверяет введенные данные с помощью функций модуля checkers.py.
# Запускать модуль main и checkers.

import checkers as ch

def name_input():
    flag = False
    while not flag:
        name = input('Введите имя и фамилию: ')
        flag = ch.check_name(name)
    return name

def b_date_input():
    flag = False
    while not flag:
        b_date = input('Введите дату в формате ДД.ММ.ГГГГ: ')
        flag = ch.check_bdate(b_date)
    return b_date

if __name__ == "__main__":
    name = name_input()
    b_date = b_date_input()
    print(name, b_date)
