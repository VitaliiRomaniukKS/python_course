import random
def ran_max(my_type):
    my_nubm = random.randint(2, 100)
    print(my_type, "число определяется в диапазоне ( 1 :", my_nubm, ")")
    return my_nubm

a_int = random.randint(1, ran_max('Целое'))
print('Выбранное целое число:', a_int)
b_float = random.uniform(1, ran_max('Дробное'))
print('Выбранное дробное число:', b_float)
if a_int > b_float:
    print ('Целое больше',)
else:
    print('Больше дробное')
print('Is int number bigger than float number? :', a_int > b_float )

c_bool = a_int > b_float
print('Случайное булевое значение:', c_bool)
