import string
atribute_string = list(dir(string))
revers_atribute_string = atribute_string.copy()
atribute_string.sort()
revers_atribute_string.sort(reverse=True)
print(atribute_string)
print(revers_atribute_string)