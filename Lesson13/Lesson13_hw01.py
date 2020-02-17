# 1. Попросите пользователя ввести имя файла. Поддерживаемые расширения - txt, log, py. 
# Если введено неподдерживаемое расширение, кидать исключение. Если введенный файл не существует, кидать исключение.
#  Подсчитать количество слов в файле.

import os

extention = ('.txt', '.log', '.py')

def verify_file(file_name):
    if not file_name.endswith(extention):
        raise ValueError ('Wrong extention')
    if not os.path.exists(file_name):
        raise FileNotFoundError ('File not found')
    pass  # проверка разрешения и существования файла, райзинг исключений , если что-то не так


def calc_words(file_name): 
    verify_file(file_name)
    words_count = 0
    with open (file_name, 'r') as file:
        for line in file:
            words_count += len(list(line.split()))
    return words_count
    pass  # в тексте функции calc_words вызываем функцию проверки файла verify_file


file_name = input ('Input file name: ')
words_count = calc_words(file_name)
print(words_count)