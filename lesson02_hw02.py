import math
my_numb = input ('Введите число ')
my_grade = input ('Введите степень ')
my_numb = int(my_numb)
my_grade = int(my_grade)
result1 = my_numb**my_grade
result2 = math.pow ( my_numb, my_grade)
print ('Результа возведения в степень с использованием **:', result1, 'с типом', type(result1))
print ('Результа возведения в степень с использованием math.pow:', result2, 'с типом', type(result2))
print ('Результаты идентичны: ', result1 == result2)