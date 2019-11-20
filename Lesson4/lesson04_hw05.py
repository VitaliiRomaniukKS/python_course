import random
my_list = [random.randint(100,999), random.randint(100,999), random.randint(100,999),]
print('Полученный список', my_list)
my_list.sort()
print('Отсортированный в прямом порядке', my_list)
my_list.sort(reverse=True)
print('Отсортированный в  обратном порядке', my_list)