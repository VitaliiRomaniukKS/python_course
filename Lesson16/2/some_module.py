import string


def gen_dict(rev=False):
    step = 3
    keys = list(string.ascii_letters + string.digits) 
    if rev:
        values = list(keys[-step:] + keys[:-step])      
    else:    
        values = list(keys[step:] + keys[:step])
    caesar = dict(zip(keys, values))
    caesar[' '] = ' '
    return caesar

def encode(text):
    caesar = gen_dict()
    resalt = [caesar[i] for i in text]
    resalt = ''.join(resalt)
    return resalt

def decode(text):
    caesar = gen_dict(rev=True)
    resalt = [caesar[i] for i in text]
    resalt = ''.join(resalt)
    return resalt


