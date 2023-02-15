palabras = []

def agregar(palabra:str) -> bool:
    if not nuevapalabra.isspace() and nuevapalabra != "":
        palabras.append(nuevapalabra)
        return True
    return False

def eliminar(palabra:str) -> bool:
    if palabra in palabras:
        palabras.remove(palabra)
        return True
    return False

num_nuevas = 0
# Pregunta cuantas palabras desea ingresar y queda en loop hasta que ingrese un numero valido
while True: 
    num_nuevas = input("Cuantas palabras desea ingresar? \n=> ")
    if num_nuevas.isnumeric():
        num_nuevas = int(num_nuevas)
        break

for i in range(num_nuevas):
    while True:
        nuevapalabra = input("Inserte la palabra numero " + str(i+1) + ": " + str(palabras) + "\n=> ")
        if agregar(nuevapalabra) == True:
            break

num_eliminar = 0
# Pregunta cuantas palabras desea eliminar y queda en loop hasta que ingrese un numero valido
while True: 
    num_eliminar = input("Cuantas palabras desea eliminar? "+ str(palabras) +"\n=> ")
    if num_eliminar.isnumeric():
        num_eliminar = int(num_eliminar)
        break
    
for i in range(num_eliminar):
    while True:
        palabra = input(str(i+1)+".Inserte la palabra a eliminar:" + str(palabras) + "\n=> ")
        if eliminar(palabra) == True:
            break
        
print(palabras)