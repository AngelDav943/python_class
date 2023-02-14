edades_a = [2,6,4,8,3,10,12,16,20,12]
edades_b = [2,7,20,12,19,14,15,13,10]

def cuantos_mayor_edad(lista1:list, lista2:list) -> int:
    edades:list = lista1 + lista2
    mayores:list = []
    for edad in edades:
        if edad >= 18:
            mayores.append(edad)
    
    cantidad:int = len(mayores)
    print("Hay", cantidad, "mayores de edad:", str(mayores)+", total:", len(edades))
    return cantidad
    
cuantos_mayor_edad(edades_a, edades_b)