import string
import random
k = random.randint (10,20)                              # длинна пароля
my_popul = list(string.ascii_letters + string.digits)   # формирования популяции символов
secret_key = list(random.sample(my_popul, k))           # генерация пароля
print (''.join(secret_key))