input_string = str(input('Введите строку:'))
input_list = list(input_string)
input_list.sort()
print(''.join(input_list))
input_list.sort(reverse=True)
print(''.join(input_list))