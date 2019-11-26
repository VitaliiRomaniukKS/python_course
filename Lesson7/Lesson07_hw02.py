import string
sourse_population = list(string.ascii_letters)
code_caesar = {}
step = 5
for i in sourse_population:
    code_caesar[i] = sourse_population[sourse_population.index(i) + step - len(sourse_population)]
print(code_caesar)