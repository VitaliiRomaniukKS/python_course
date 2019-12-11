# 4. Написать игру Угадай число. Скрипт генерирует случайное целое число, 
# диапазон на выбор разработчика. Пользователю предлагается вводить числа. 
# Если угадал, то выход с отображением надписи - Поздравляю! 
# Если не угадал, отображать подсказку, больше или меньше введенное число искомого.

import random

my_num = random.randint(1,100)
custom_num = 0
while custom_num != my_num:
    custom_num = input('ВВедите число от 1 до 100: ')
    if custom_num.isdigit():
        custom_num = int(custom_num)
        if custom_num > my_num:
            print('Многовато')
        elif custom_num < my_num:
            print('Маловато')
        else:
            print('Поздравляю!')
    else:
        print ('Ну это не число')