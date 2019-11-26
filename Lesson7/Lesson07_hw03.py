person1 = 'harry potter; 30; 127.45 galeon; auror'
person2 = 'ross geller; 34; 6500.45 usd; paleontologist'
with open('persons.txt', 'w') as my_file:
    my_file.writelines(person1 + '\n' + person2 + '\n')



