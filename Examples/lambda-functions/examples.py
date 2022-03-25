'''
def two():
    return 2
'''
two = lambda: 2  

'''
def sqr(x):
    return x * x
'''
sqr = lambda x: x * x

'''
def pwr(x,y):
    return x**y
'''
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

