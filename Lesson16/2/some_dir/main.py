import sys

pth =  __file__
pth = pth.split('/')
pth = pth[:-2]
pth = '/'.join(pth)
sys.path.append(pth)

import some_module 

my_text = 'Hi Ksu'

encoded_text = (some_module.encode(my_text))
print(encoded_text)

decoded_text = (some_module.decode(encoded_text))
print(decoded_text)