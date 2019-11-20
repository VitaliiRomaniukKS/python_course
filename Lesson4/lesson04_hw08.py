import string
my_string = str(input('Введите имя и фамилию работника, его должность, зарплату, возраст'))
my_string = my_string.strip()
f_name, l_name, position, salary, age, *other = my_string.split() 

print(dir(string))
print(type(f_name))
f_name = f_name.title()
l_name = l_name.title()
salary = float(salary)
print(f'Имя: {f_name}, Фамилия: {l_name}, Должность: {position}, Зарплата: {salary}, Возраст: {age}.')