# 1. Написать скрипт, осуществляющий шифрование фразы, введенной пользователем, 
# по методу из ДЗ-3, задание 5 (после каждой буквы исходной фразы, добавлять определенное 
# число случайных символов, букв латинского алфавита. Чтобы скрыть первую букву, добавили и 
# перед ней такое же количество случайных символов. Ваши специалисты узнали, что это число - 10).
# Проверять, что шифрование отрабатывает верно (как делали в ДЗ3-5).

import random
import string

def generate_str(count):
    my_popul = list(string.ascii_letters + string.digits)   
    secret_key = list(random.sample(my_popul, count))           
    return(''.join(secret_key))

add_str = generate_str(5)
print(add_str)
step = 10

sours_str = input('ВВедите строку: ')
new_str = [i+generate_str(step) for i in sours_str]
new_str = list(generate_str(step)) + new_str
print(f"Зашифрованная строка {''.join(new_str)}")

# Старая ДР для проверки 

secret = ''.join(new_str)
# secret = str ('VZoFPzGvXwtbR+guMLszPhfvZotHwDm-emryhEXAaBW+-AbMdmEK+ztGDWyIzSFvjaFrHLzhoRqgsQraUdnSBGykFWNLOxTVKM+ynHqsVrQGEiqdKULoDVZcsZ-BpTWkDVR+jSgrfQZhUAdWCxtwOmTBQo+qWOlYyvGxnNpZFlTSrmaesQOotBLnVw!gOUrhz+F-DctdKWvTGhMUopoSPyFAXdJnY+DGFZQbOVgzaqsGvWjtBrJjBWhAFgryaTtwginpEsWtAuOxbgI-ZVunVAIuklBqTlSGUnevwEMqayHKF+sebTCtWcnhzUelA+iM+ivKleqrjoLsmrtHZOGfnHOWXYJpDwU!')
message = secret[10::11]
print('Текст шифровки:',message)