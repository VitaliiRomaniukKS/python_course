import random
rand_num = random.randint(1,100)
my_list = [rand_num]*30
print(my_list)
my_list[2::3]= [1000] * 10
print(my_list)