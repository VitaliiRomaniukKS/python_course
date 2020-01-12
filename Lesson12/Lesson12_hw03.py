#  3. Задание по парсингу файла с погодой и получение информации о мин, макс и средней, 
#  а также дат - сделать с применением функций.


def make_dict (file_name):
    dict_temperature = {}
    with open(file_name, 'r') as my_file:
        for line in my_file:
            data, temp = line.split(';')
            temp = int(temp)
            dict_temperature.update({data:temp})
    return(dict_temperature)

dict_temp = make_dict('weather.txt')

min_temperature = min(dict_temp.values())
min_temp_data = [d for d, t in dict_temp.items() if t == min_temperature]

max_temperature = max (dict_temp.values())
max_temp_data = [d for d, t in dict_temp.items() if t == max_temperature]

average_temperature = sum(dict_temp.values()) / len(dict_temp)

print()
print(f'Минимальная температура {min_temperature} была: {min_temp_data}')
print(f'Максимальная температура {max_temperature} была: {max_temp_data}')
print(f'Средная температура {average_temperature: .2f}')
print()