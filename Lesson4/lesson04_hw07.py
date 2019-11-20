import string
import random
random_string = list(random.sample(string.ascii_letters, 10))
print(''.join(random_string))