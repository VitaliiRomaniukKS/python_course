# Осуществить парсинг файла с информацией о температуре воздуха. 
# Вывести дату(хотя бы одну) минимальной температуры и само значение температуры, 
# дату максимальной температуры и значение. Вывести среднее значение температуры за месяц. 
# * Если минимальная или максимальная температура была не один день, то вывести все даты, 
# когда была зафиксирована такая температура.


min_temperature = 100
max_temperature = -100
average_temperature = 0
sum_temperature = 0
day_count = 0
dict_temperature = {}

with open('weather.txt', 'r') as my_file:
    for line in my_file:
        data, temp = line.split(';')
        temp = int(temp)
        dict_temperature.update({data:temp})
        if temp < min_temperature:
            min_temperature = temp
        if temp > max_temperature:
            max_temperature = temp
        sum_temperature = sum_temperature + temp
        day_count = day_count +1

average_temperature = sum_temperature / day_count
print( min_temperature , max_temperature, average_temperature )

print(f'Минимальная температура {min_temperature} была: ')
for d, t in dict_temperature.items():
    if t == min_temperature:
        print(d)

print(f'Максимальная температура {max_temperature} была: ')
for d, t in dict_temperature.items():
    if t == max_temperature:
        print(d)

print(f'Средная температура {average_temperature: .2f}')

     