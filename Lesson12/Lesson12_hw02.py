#  2. Написать функцию  get_result, у которой обязательный аргумент func - это одна из функций -  
#  min, max, sum, len, а дальше следуют неограниченное количество числовых аргументов или числовых строк. 
#  Результатом выполнения функции get_result - это результат применения аргумента func к остальным аргументам.  
#  Обязательно проверять func, чтоб нельзя было передать иную функцию. 
#  В скрипте сделать также вызовы описанной функции. Примеры вызова : get_result(sum, 1,2,3,’4’), get_result(len) и тп.

# **  добавить значение по умолчанию для параметра func - len, проверить работу функции для разных вариантов.


def get_result(func=len, *args):
    print(args)
    func_dict = {sum, min, max, len}
    if func not in func_dict:
        return('Функция не верна')
    args_list = [int(i) for i in args]
    return(func.__name__, func(args_list))

test_list = [1, -2, '3', 4, '23']
print(get_result(dir, 1, 2, '3', 4))
print(get_result(len, 1, 2, '3', 4, '5'))
print(get_result(sum, 1, 2, '3', 4))
print(get_result(max, 1, 2, '3', 4, '23'))
print(get_result(min, *test_list))
print(get_result())

# не смог вызвать get_result без указания функции, но с аргументами
