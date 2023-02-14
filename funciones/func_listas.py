estudiantes = ["david", "omar", "isaac"]
profesores = ["felipe"]

def agregar(lista:list) -> list:
    persona = str(input("Ingrese un nombre \n=> "))
    lista.append(persona.lower())
    return lista

def eliminar(lista:list) -> list:
    persona = str(input("Ingrese la persona a eliminar \n=> "))
    if persona in lista:
        lista.remove(persona.lower())
    return lista

def visualizar(lista:list) -> None:
    for item in lista:
        print(item, end=", ")
    print("\n")

print("\t--Estudiantes.")
visualizar(estudiantes)
agregar(estudiantes)
visualizar(estudiantes)
eliminar(estudiantes)
visualizar(estudiantes)

print("\n\t--Profesores.")
visualizar(profesores)
agregar(profesores)
visualizar(profesores)
eliminar(profesores)
visualizar(profesores)

def combinar2(list1:list, list2:list, extra = "juan") -> list:
    nuevalista = list1 + list2
    nuevalista.append(extra)
    return nuevalista

print("\n\t--Total")
print(combinar2(estudiantes,profesores))