# Распарсить файл с информацией о платежах, но использовать только те,
# где тип платежа out, также не все строки могут быть в корректном формате. 
# Кто совершал больше всего покупок? На наибольшую сумму? Файл: 

out_trans_list = []

with open('payments.txt', 'r') as payments_f:
    for line in payments_f:
        new_trans = line.split(';')
        if (len(new_trans) == 5) and (new_trans[-2] == 'out'):
            # print(new_trans)
            new_trans.remove(new_trans[4])
            out_trans_list.append(new_trans)

print(out_trans_list)
payments_d = {}
for i in out_trans_list:
    summa = float (i[1].split()[0].replace(',','.'))
    if i[0] not in payments_d:
        payments_d[i[0]] = [summa]
    else:
        payments_d[i[0]].append(summa)    

print()
print(payments_d)

max_pay = [0,0]
max_sum = [0,0]
max_price = [0,0]
for name, p_count in payments_d.items():
    if len(p_count) > max_pay[1]:
        max_pay = [name,len(p_count)]
    if sum(p_count) > max_sum[1]:
        max_sum = [name, sum(p_count)]
    if max(p_count) > max_price[1]:
        max_price = [name,max(p_count)]   

print(max_pay)
print(max_sum)
print(max_price)
