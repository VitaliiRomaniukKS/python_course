# Написать скрипт парсинга файла с информацией о балансах пользователей 
# https://drive.google.com/open?id=1iItMYUF0Uwb-qB0epNTLRnJpKRU6joGV balances.txt
# Затем просить пользователей ввести номер аккаунта, а в ответ выводить ему баланс этого пользователя. 
# С помощью механизма исключений и обработки исключений, предусмотреть варианты - 
# что пользователь введет вместо номера аккаунта не числа. А также, что будет введен несуществующий номер аккаунта.

class AccountNotFount(ValueError):
    '''raise it Account Not Fount'''
    pass



def create_acc_dict (file):
    accounts = {}
    with open (file, 'r') as file:
        for line in file:
            account, balance = (line.strip().split(';'))
            accounts[account] = balance
    return accounts


def find_account(account):
    try:
        if not account.isdigit():
            raise TypeError()
        if account not in account_dict:
            raise AccountNotFount()
        return account_dict[account]
    except AccountNotFount:
        return 'Account Not Fount'
    except TypeError:
        return 'Wrong format'



account_dict = create_acc_dict('balances.txt')
account = input('Enter account: ')
print(find_account(account))
