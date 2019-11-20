import string
atribute_list = list(dir(string))
my_tuple = tuple(atribute_list[-5:])
print(my_tuple)
new_list = list (my_tuple)
new_list.insert (2,'capwords')
new_list = tuple(new_list)
print (new_list)
