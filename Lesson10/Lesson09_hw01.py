# 1. Попросить пользователя ввести строку и зашифровать ее шифром Цезаря со сдвигом 4. 
# Если пользователь вводит пустую строку (то есть просто нажимает Enter или один символ, 
# то просить его вводить строку пока не введет минимум 2 символа). 
# Код для реализации шифра Цезаря, могу скинуть кому нужно.

import string

sourse_population = list(string.ascii_letters)
dect_caesar = {}
step = 4
for i in sourse_population:
    dect_caesar[i] = sourse_population[sourse_population.index(i) + step - len(sourse_population)]

my_string = input('Введите стороку: ')
while len(my_string) < 2:
    print('длина строки должна быть более 2-х символов.')
    my_string = input('Введите стороку: ')

new_str = ''
for i in my_string:
    new_str = new_str + dect_caesar[i]
print(new_str)