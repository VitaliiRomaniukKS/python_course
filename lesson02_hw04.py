import math
my_numb = input ('Введите число:')
my_numb = float (my_numb)
my_numb = math.floor(my_numb)
print ('В в 16ти-ричном представлении число', my_numb, 'будет выглядеть как:', hex(my_numb))
print ('В в 8ми-ричном представлении число', my_numb, 'будет выглядеть как:', oct(my_numb))