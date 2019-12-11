# 3. Сделать парсинг файла логов сервера, подготовить информацию в разрезе ip - 
# в какое время с каждого ip были зафиксированы запросы. 
# (Подсказка - на выходе - словарь, ключ - ip,  значение - список времен)

log_dict = {}

with open('app.log', 'r') as my_file:
    for line in my_file:
        ip, *data = line.split(' ')
        data = ' '.join(data[:2])
        if ip not in log_dict.keys():
            log_dict.update({ip:[data]})
        else:
            log_dict[ip].append(data)

print(log_dict)