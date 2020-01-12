#  5. Осуществлять подсчёт количества букв в тексте, текст брать из файла или просить пользователя вводить.
#   На выходе - словарь. Ключ - буква лат алфавита, значение - количество, сколько раз она встречалась в тексте. 
#   Брать только буквы, приводить в нижний регистр, все остальные символы - игнорировать, в т ч пробелы. 
# ** Подготовить информацию чуть более усложнённо, ключ - буква, значение - список слов, где она встречается.

import string
import os


def make_wordlist_from_str (my_str):
    my_str = my_str.lower()
    word_list = my_str.split()
    print(word_list)
    return(word_list)

def make_list_of_word(text_inputed):
    text = []
    if os.path.exists(text_inputed):
        with open (text_inputed,'r') as file:
            for line in file:
                text.extend(make_wordlist_from_str(line))
        return(text)
    text = make_wordlist_from_str(text_inputed)
    return(text)


def make_dict_of_word (srs_txt):
    dict_of_word = {}
    for i in srs_txt:
        k = list(i)
        for j in k:
            if j in string.ascii_letters:
                if j not in dict_of_word:
                    dict_of_word[j] = i
                else:
                    dict_of_word[j] += ', ' + i
    return(dict_of_word)   

# sours_text = input('Введите текст или имя файла: ')

# sours_text = 'sВdD ffgf gxvsdbtz упамыфу'
sours_text = 'payments2.txt'

text_list = make_list_of_word(sours_text)
letter_dict = {}
letter_dict = make_dict_of_word(text_list)
print('**************')
print (letter_dict)
