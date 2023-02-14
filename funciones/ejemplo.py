import math

def suma_dos(a, b):
    suma = a + b
    return suma

def dist(x1, y1, x2, y2):
    x = math.pow(x2 - x1, 2)
    y = math.pow(y2 - y1, 2)
    dist = math.sqrt( x + y )
    return dist

print(suma_dos(2, 3))
print(dist(0,0, 4,0))

def suma(*nums):
    total = 0
    for num in nums:
        total = total + num
    print(total)
    return total

suma(1,2,2,4,5)

def suma_listas(*listas):
    res:list = []
    for lista in listas:
        res = res + lista
    print(res)
    return res


suma_listas(["a","b"], [2,3], [False,True])
