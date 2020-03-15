# Создать модуль catalogs, в котором определить две константы - 
# словарь валют {980: "UAH", 643: "RUB", 840: "USD", 943: "EUR"} и 
# словарь стран {"ua": ("Ukraine", 980), "ru": ("Russia", 643), "us": ("USA", 840), 
# "uk": ("United Kindom", 943), "pl": ("Poland", 943), "es": ("Spain", 943)}. 
# Создать модуль main, в котором импортировать модуль catalogs. 
# Вывести на печать названия всех стран с буквенными алиасами валют, упорядочить по имени страны. 
# То есть на выходе будет:
# Country: Poland, currency: EUR
# Country: Russia, currency: RUB
# Country: Spain, currency: EUR
# Country: USA, currency: USD
# Country: Ukraine, currency: UAH
# Country: United Kindom, currency: EUR

from catalogs import curr 
from catalogs import country 


country_lst = []
_ = [country_lst.append(list(i)) for i in country.values()]
country_lst = sorted(country_lst, key=lambda x: x[0])
for k, v in country_lst:
    print(f'Country: {k}, currency: {curr[v]}')