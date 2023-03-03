from usuario import persona
from datetime import date 
personas = {}

def agregar(nombre:str, libro:str) -> str:
    nombre = str(nombre).lower()
    if (not (nombre in personas.keys())): # Si NO existe:
        if nombre.isspace() == False:
            personas[nombre] = persona(nombre)

    if libro.isspace() == False:
        personas[nombre].agregar_libro(
            str(libro).lower(), # nombre del libro
            str(date.today()) # fecha
        )
        return str(date.today())
    
def eliminarlibro(nombre:str, libro:str) -> str:
    if str(nombre).lower() in personas: # Verifica si usuario existe
        personas[str(nombre).lower()].eliminar_libro(str(libro).lower())

def eliminar(nombre:str) -> str:
    if str(nombre).lower() in personas: # Verifica si usuario existe
        personas.pop(str(nombre).lower())
        return nombre

    return None

def buscar(nombre:str) -> persona:
    if str(nombre).lower() in personas: # Verifica si usuario existe
        return personas[str(nombre).lower()]

def visualizar() -> dict:
    return personas
