name=input ('Как тебя зовут?:')
print('Привет, ' + name)
age=input ('Сколько тебе лет?:')
sex=input ('Какой твой пол (M/W)?:')
weight=input ('Какой у тебя вес(кг))?:')
height=input ('Какой у тебя рост(см))?:')
weight = int(weight)
height = int(height)
height = height / 100
imt = weight / (height*height)
print('Тебя зовут, ' + name + ', тебе ' + age + ' лет')
if sex==('M'):
    if imt<24:
        print (name, 'ну ты и дрыщ')
    else:   
        if imt < 30 :
             print (name, 'ты красава')
        else:
             print (name, 'хватит ЖРАТЬ!!!')

else:
    if imt<20:
        print (name, ', готовиш себя в модели?')
    else:
        if imt < 25 :
            print (name, 'ТЫ БАГИНЯ')
        else:
             print (name, ', попробуй бегать по утрам')

print(' You are lucky Guy!')
