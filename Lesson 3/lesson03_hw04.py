my_string= input ('Введите строку ')
string_long = len(my_string)
string_half = string_long//2
print('Первая половина строки', my_string[:string_half])
print('Вторая половина строки', my_string[-string_half:])