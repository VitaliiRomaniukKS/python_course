# 1. Написать скрипт для Парсинга файла логов, для получения информации об ошибках.  
# Ошибкой считать запись в файле логов, если в качестве уровня логирования указан [ERROR]. 
# Данные об ошибках должны быть сохранена в новый файл, errors.log, 
# в нем должна быть следующая информация: ip адрес, с которого пришел запрос, дата и время ошибки, текст ошибки.


def create_err_list (file):
    error_list = []
    with open (file, 'r') as file:
        for line in file:
            line = str(line)
            ip , date, time, err_type, *err_text = line.split()
            if err_type == '[ERROR]':
                error_list.append([ip, date, time, ('ErrorText: ' + ' '.join(err_text[2:]))])
    return error_list


def list_to_file(error_list, file_name='errors.log'):
    with open (file_name, 'w') as file:
        for line in error_list:
            file.writelines(' '.join(line) + '\n')
    return


error_list = create_err_list('app.log')
error_list = sorted(error_list, key=lambda x: x[0])
list_to_file(error_list)