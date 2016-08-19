#Reinforcement 1.1
def is_multiple(n, m):
    '''Returns True if n is a multiple of m'''
    return True if n%m==0 else False

#Reinforcement 1.2
def is_even(k):
    '''Takes an integer value and Returns True if k is even'''
    while True:
        if k<=2:
            break
        k = k - 2
    return True if k == 2 else False 

#Reinforcement 1.3
def minmax(data):
    try:
        min, max = 0, 0
        for value in iter(data):
            max = value if max<value and max!=0 else max
            min = value if min>value and min!=0 else min
        return min, max
    except TypeError:
        print "Input data is not iterable!"
