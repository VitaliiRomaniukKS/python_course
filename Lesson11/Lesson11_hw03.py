# 3. Есть список функций funcs. Необходимо выводить пользователю информацию (doc-строку) по каждой функции, 
# выбирая ее случайным образом до тех пор, пока пользователь либо не введет ’stop’ или не закончатся все функции. 
# Отображать информацию о функции и ожидать ввода пользователем чего-либо. Код для формирования списка функций funcs 
# (просто скопируйте его в свой скрипт):

import random

lst = dir(__builtins__)[80:] 
lst.remove('copyright')
lst.remove('credits') 
funcs = [getattr(__builtins__, attr) for attr in lst]
# print(funcs)

my_str = ''
while (my_str != 'stop') and  funcs:
    func_ran = random.choice(funcs)
    print(func_ran, func_ran.__doc__)
    funcs.remove(func_ran)
    my_str = input('Введите stop, если хотите выйти: ')
