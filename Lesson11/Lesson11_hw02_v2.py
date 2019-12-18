# Распарсить файл с информацией о платежах, но использовать только те,
# где тип платежа out, также не все строки могут быть в корректном формате. 
# Кто совершал больше всего покупок? На наибольшую сумму? Файл: 

def out_by_func (funk,my_dict):
    max_func = [0,0]
    for name, summs in my_dict.items():
        if funk(summs) > max_func[1]:
            max_func = [name,funk(summs)]
    return(max_func)

out_trans_list = []

with open('payments.txt', 'r') as payments_f:
    for line in payments_f:
        new_trans = line.split(';')
        if (len(new_trans) == 5) and (new_trans[-2] == 'out'):
            new_trans.remove(new_trans[4])
            out_trans_list.append(new_trans)

payments_d = {}
for i in out_trans_list:
    summa = float (i[1].split()[0].replace(',','.'))
    if i[0] not in payments_d:
        payments_d[i[0]] = [summa]
    else:
        payments_d[i[0]].append(summa)    

print('Максимальное количество покупок: ', out_by_func(len, payments_d))
print('Максимальная сумма за все покупки: ', out_by_func(sum, payments_d))
print('Максимальная цена одной покупоки: ', out_by_func(max, payments_d))
