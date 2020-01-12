#  5. Осуществлять подсчёт количества букв в тексте, текст брать из файла или просить пользователя вводить.
#   На выходе - словарь. Ключ - буква лат алфавита, значение - количество, сколько раз она встречалась в тексте. 
#   Брать только буквы, приводить в нижний регистр, все остальные символы - игнорировать, в т ч пробелы. 
# ** Подготовить информацию чуть более усложнённо, ключ - буква, значение - список слов, где она встречается.

import string
import os

def make_normal_list_from_str (my_str):
    letter_list = [i for i in my_str.strip().lower() if i in string.ascii_letters]
    return(letter_list)

def make_list_of_lette(text_inputed):
    text = []
    if os.path.exists(text_inputed):
        with open (text_inputed,'r') as file:
            for line in file:
                text.extend(make_normal_list_from_str(line))
        return(text)
    text = make_normal_list_from_str(text_inputed)
    return(text)


def make_dict_of_letter (srs_txt):
    dict_of_letter = {}
    for i in srs_txt:
        if i not in dict_of_letter:
            dict_of_letter[i] = 1
        else:
            dict_of_letter[i] += 1
    return(dict_of_letter)

sours_text = input('Введите текст или имя файла: ')

# sours_text = 'sВdD ffgf gxvsdbtz упамыфу'
# sours_text = 'payments2.txt'

text_list = make_list_of_lette(sours_text)
text_list.sort()
letter_dict = {}
letter_dict = make_dict_of_letter(text_list)
print (letter_dict)
