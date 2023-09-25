def add_digits(number):
    mod = 0
    while number != 0:
        mod = mod + number % 10
        number = number // 10
    return mod

def most(a,b):
    if(a>b):
        return a
    else:
        return b  

def least(a,b):
    if(a<b):
        return a
    else:
        return b