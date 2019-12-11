
def return_type (type_in_str):
    resalt_type = type_in_str.lower()[0]
    return(resalt_type)

my_num = int(input('Ведите число '))
my_type = (input ('''Введите тип, в котором нужно вывести число 
(b или В - в бинарном. Если o, O - 8-миричном, h или H - 16-ричном)'''))

my_dict = {'b': bin, 'o': oct, 'h': hex}
my_type = return_type(my_type)

if my_type in my_dict:
    
    my_funk = my_dict[my_type]
    print(my_funk(my_num))
else:
    print('error')

print('До свиданья!')