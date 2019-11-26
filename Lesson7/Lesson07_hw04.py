
def make_dict (my_string):
    name = dict(zip(['first_name', 'last_name'], ['', '']))
    name_str, age, salary_str, profession  = my_string[:-1].split(';') # не придумал как по другому убрать перевод каретки
    name['first_name'], name['last_name'] = name_str.title().split()
    age = int(age)
    amount, currency = salary_str.split()
    amount = float(amount)
    salary = dict(amount=amount, currency=currency)
    my_dict = dict (name=name, age=age, salary=salary, profession=profession)
    return my_dict

persons = {}

with open('persons.txt', 'r') as my_file:
    for person in my_file:
        my_name, *other = person.strip().split()
        persons.update( {my_name: make_dict(person)} )

print(persons)
