# Первый checkers.py, содержит функции проверки - имени(check_name), даты рождения(check_bdate), 
# а также функцию test без параметров. (Функция test вызывается в случае запуска модуля в интерпретаторе, 
# в ней происходит вызов каждой описанной в модуле функции с корректными значениями). Функции check_name, 
# check_bdate проверяют корректность переданных аргументов и кидают исключения с текстом, если что-то не соответствует норме.

class WrongFormat(ValueError):
    '''raise it format wrong'''
    pass


month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} # количество дней в месяце
max_val = {'m':12, 'y':2019} # максимально допустимые значения месяца и года



def hi_year (year):
    """ Если год высокосный, возвращает 1
    """
    i = 1
    if year % 4: 
        i = 0
    return i


def count_day_in_month(year, month):
    """ Расчитывает количество дней в месяце указанного года
    """
    month = int(month)
    year = int (year)
    return month_dict[month] + hi_year(year)


def check_format(b_date):
    """ Проверяет соответствию формата даты ДД.ММ.ГГГГ
    """
    b_d_lst = b_date.split('.')
    if len(b_d_lst) != 3:
        return False
    if (len(b_d_lst[0]) > 2) or (len(b_d_lst[1]) > 2) or (len(b_d_lst[2]) != 4):
        return False
    return True


def check_name(name='Vitalii Romaniuk'):
    """ Проверяет что введено имя и фамилию
    """
    try:
        if len(list(name.split(' ')))!=2:
            raise Exception()
    except Exception:
        print('Введите имя и фамилию через пробел')
        return False
    else:
        return True


def check_bdate(b_date='21.04.1982'): 
    """ Проверяет корректность введеной даты в формате ДД.ММ.ГГГГ
    """   
    try:
        if not check_format(b_date):
            print(check_format(b_date))
            raise WrongFormat()
        b_d_lst = b_date.split('.')
        b_d_lst.reverse()
        b_date = dict(zip(('y', 'm', 'd'), b_d_lst))
        for k,v in b_date.items():
            if not v.isdigit():
                raise TypeError()
            if k == 'd':
                max_value = count_day_in_month(b_date['y'], b_date['m'])
            else:
                max_value = max_val[k]
            if int(v) > max_value:
                raise ValueError()
        return True
    except WrongFormat:
        print('Неверный формат даты, введите дату в формате ДД.ММ.ГГГГ')
        return False        
    except ValueError:
        print('Неверное значение')
        return False
    except TypeError:
        print ('Введите число')
        return False

def test():
    print('Vitalii Rovfniuk - ', check_name('Vitalii Rovfniuk'))
    print('Birthday: 21.04.1982 - ', check_bdate('21.04.1982'))

if __name__ == "__main__":
    test()
