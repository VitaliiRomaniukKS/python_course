# 4. Задание с парсингом файла с платежами, переписать с помощью функций. 
# Сделать имя файла значением по умолчанию. А также учитывать актуальную валюту, приводить все к USD. 
# То есть если сумма в файле в евро, то пересчитать ее в доллар по курсу 1.11. 
# И найти кто тратил больше всех по разным показателям, как было в задании.

def make_list_from_file (file_name):
    with open(file_name, 'r') as payments_f:
        for line in payments_f:
            new_trans = line.strip().split(';')
            if (len(new_trans) == 5) and (new_trans[-2] == 'out'):
                new_trans.remove(new_trans[4])
                out_trans_list.append(new_trans)
    return (out_trans_list)

def print_by_func (funk,my_dict):
    max_func = [0,0]
    for name, summs in my_dict.items():
        if funk(summs) > max_func[1]:
            max_func = [name,funk(summs)]
    return(max_func)

def summa_in_usd (summ_str):
    amount, curr = summ_str.split(' ')
    amount = float(amount.replace(',','.'))
    if curr == 'EUR': amount = amount * 1.11
    return(amount)

def make_dict_of_accaunt (trans_list):
    for i in trans_list:
        summa = summa_in_usd(i[1])
        if i[0] not in payments_d:
            payments_d[i[0]] = [summa]
        else:
            payments_d[i[0]].append(summa)
    return(payments_d)


out_trans_list = []
out_trans_list = make_list_from_file('payments.txt')

payments_d = {}
payments_d = make_dict_of_accaunt(out_trans_list)

print('************')
print(f'Максимальное количество покупок у {print_by_func(len, payments_d)[0]}: {print_by_func(len, payments_d)[1]} ')
print(f'Максимальная сумма за все покупки у {print_by_func(sum, payments_d)[0]}: {print_by_func(sum, payments_d)[1]: .2f} USD')
print(f'Максимальная цена одной покупоки у {print_by_func(max, payments_d)[0]}: {print_by_func(max, payments_d)[1]: .2f} USD')