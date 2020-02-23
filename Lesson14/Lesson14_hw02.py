# Переписать игру Угадай число с помощью механизма исключений. В коде указан пример, как создавать собственные исключения.
#  https://gist.github.com/kryskaks/881e9b8f04bda87e2e7acd5808e11618. 
# Затем достаточно просто делать raise ValueTooBig(), где необходимо. 
# Необходимо будет как разить исключения, так и обрабатывать их.


class ValueTooBig(ValueError):
    '''raise it when input number is too big'''
    pass


class ValueTooSmall(ValueError):
    '''raise it when input number is too small'''
    pass

import random

def check_num(custom_num, random_num):
    try:
        if not custom_num.isdigit():
            raise TypeError()
        custom_num = int(custom_num)
        if custom_num > random_num:
            raise ValueTooBig()
        if custom_num < random_num:
            raise ValueTooSmall()
    except TypeError:
        print ('Ну это не число')
    except ValueTooBig:
        print('Многовато')
    except ValueTooSmall:
        print('Маловато')
    else:
        return custom_num
    

    


random_num = random.randint(1,100)
print (random_num)
custom_num = 0
while custom_num != random_num:
    custom_num = input('ВВедите число от 1 до 100: ')
    custom_num = check_num(custom_num, random_num)
print ('УРА!!!')