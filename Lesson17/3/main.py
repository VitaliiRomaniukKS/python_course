# Использовать модуль catalogs из п.3. Создать модуль main, в нем импортировать catalogs.
# Просить пользователя ввести код страны (например, us) и выводить информацию об имени страны, 
# код валюты и алиас валюты. Если введено некорректное значение кода, которого нет в словаре, кидать исключение. 

from catalogs import curr 
from catalogs import country 

def country_inform(code):
    try:
        if code not in country:
            raise ValueError()       
        print(f'Country code:{code}')
        print(f'Country name: {country[code][0]}')
        print(f'Currency code: {country[code][1]}')
        print(f'Currency alias: {curr[country[code][1]]}')
    except ValueError:
        print('Country not found')

code = input('Enter country code: ')
country_inform(code)