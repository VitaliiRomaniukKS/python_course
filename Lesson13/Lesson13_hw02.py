# 2. Просить пользователя ввести данные о себе - имя, дату рождения, профессию. 
# При вводе имени, проверять, что введено имя и фамилия, через пробел. 
# Если нет, кидать исключение с нужным текстом. 
# При вводе даты рождения, просить вводить по отдельности - год, месяц и число. 
# Если при вводе какого-то параметра введены символы, отличные от цифр, кидать исключение с нужным текстом.
#  Если год больше 2000 - кидать ошибку. Если месяц больше 12, кидать ошибку. 
# Если число больше 31, кидать ошибку ( ** добавить проверку, что в определенных месяцах дней может быть меньше 31). 
# Сохранять данные в файл с названием {name}.txt, в формате : {name};{bith date};{profession}\n 

month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}


def check_name(name):
    if len(list(name.split(' ')))!=2:
        raise Exception('Введите имя и фамилию через пробел')


def check_date(date, max_num):
    if not date.isdigit():
        raise Exception('Введите число')
    if int(date) > max_num:
        raise ValueError(f'Неверные данные. Максимальное значение: {max_num}')

def hi_year (year):
    i = 1
    if year % 4: 
        i = 0
    return i

def count_day_in_month(year, month):
    month = int(month)
    year = int (year)
    return month_dict[month] + hi_year(year)


def name_input():
    name = input('Введите имя и фамилию: ')
    check_name(name)
    return name

def b_date_input():
    b_year = input('Введите год рождения: ')
    check_date(b_year, 2000)
    b_month = input('Введите месяц рождения: ')
    check_date(b_month, 12)
    b_day = input('Введите день рождения: ')
    day_in_month = count_day_in_month(b_year, b_month)
    check_date(b_day, day_in_month)
    b_date = [b_day, b_month, b_year]
    b_date = '.'.join(b_date)
    return b_date

def person_to_file(name, person):
    file_name = name + '.txt'
    with open (file_name, 'w') as file:
        file.writelines(person + '\n')

name = name_input()
b_date = b_date_input()
profession = input('Введите професию: ')
person = [name, b_date, profession]
person = ';'.join(person)
person_to_file(name, person)

