# Попросите пользователя ввести имя файла. Поддерживаемые расширения - txt, log, py. 
# Если введено неподдерживаемое расширение, отображать ошибку. 
# Подсчитать количество слов в файле, предварительно убедившись, 
# что файл существует с помощью функции модуля os, os.path.exists. Если файл не существует, отображать ошибку
# Пример использования функции
# import os
# print(‘Файл test.txt существует?: ’, os.path.exists(‘test.txt’))

import os

f_name = input('Введитее имя файла: ')
other = []
other.extend(f_name.split('.'))
print(other)
f_type = ['txt', 'log', '.py']
my_list = []
if other[-1] in f_type:
    if os.path.exists(f_name):
        with open(f_name, 'r') as my_file:
            for line in my_file:
                my_list.extend(line.split(' '))
                print
    else:
        print('Фаил не найден')
else:
    print('Данный тип файла не поддерживается')

my_list.remove('\n')
count = 0
for i in my_list:
    count = count + 1
print(my_list)
print(count)