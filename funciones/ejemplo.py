import math

def suma_numeros(a, b):
    suma = a + b
    return suma

def dist(x1, y1, x2, y2):
    x = math.pow(x2 - x1, 2)
    y = math.pow(y2 - y1, 2)
    dist = math.sqrt( x + y )
    return dist

print(suma_numeros(2, 3))
print(dist(0,0, 4,0))