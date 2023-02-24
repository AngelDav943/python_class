palabras1 = []
palabras2 = []

def agregar(lista:list, palabra:str) -> list:
    lista.append(nuevapalabra)
    return lista

num_nuevas = int(input("Cuantas palabras desea ingresar? \n=> "))
for i in range(num_nuevas):
    nuevapalabra = input(f"Inserte la palabra numero {str(i+1)}: {str(palabras1)} \n=> ")
    agregar(palabras1, nuevapalabra)
print(palabras1)

num_nuevas = int(input("Cuantas palabras desea ingresar? \n=> "))
for i in range(num_nuevas):
    nuevapalabra = input(f"Inserte la palabra numero {str(i+1)}: {str(palabras2)} \n=> ")
    agregar(palabras2, nuevapalabra)

palabras3 = palabras1 + palabras2

for palabra in (palabras1 + palabras2):
    if (palabra in palabras1) and (palabra in palabras2):
        palabras3.remove(palabra)

print(f"Lista 1: {palabras1}")
print(f"Lista 2: {palabras2}")
print(f"Lista 3: {palabras3}")