from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI(
    title="Biblioteca",
    description="hola",
    version="v0.0.1"
)
personas = []

def persona_existe(id): # Verifica si usuario existe
    return id > 0 and id <= len(personas)

@app.get("/")
def root():
    return {
        "titulo":app.title,
        "version":app.version
    }

@app.get("/personas", tags=["Personas"])
def personas_all():
    """Devuelve una lista de todas las personas en la biblioteca.

    Returns:

    - List: Lista de personas en biblioteca.
    """
    return personas

@app.get("/personas/{id}", tags=["Personas"])
def personas_buscar(id: int):
    """Devuelve el usuario pedido.

    Args:

    - id (int): ID del usuario

    Returns:

    - dict: usuario.
    """
    if persona_existe(id):
        return personas[id - 1]

@app.post("/personas", tags=["Personas"])
def personas_add(nombre: str):
    """Agrega un usuario a los datos de la biblioteca.

    Returns:

    - dict: Devuelve el usuario.
    """
    usuario = {
        "nombre": str(nombre).lower(),
        "libros": []
    }
    personas.append(usuario)
    return usuario

@app.put("/personas", tags=["Personas"])
def personas_modify(id: int, nuevo_nombre:str):
    """Modifica datos de un usuario existente.

    Args:
    - id (int): _description_
    - nuevo_nombre (str): El nuevo nombre que le va a poner al usuario.

    Returns:

    - bool: Retorna True si el usuario existe.
    """
    if persona_existe(id): # Verifica si usuario existe
        personas[id - 1]["nombre"] = str(nuevo_nombre).lower()
        return True

@app.delete("/personas", tags=["Personas"])
def personas_delete(id: int):
    """Elimina un usuario a los datos de la biblioteca.

    Args:

    - id (int): Id del usuario.

    Returns:

    - bool: Devuelve True si el usuario existe.
    """
    if persona_existe(id): # Verifica si usuario existe
        personas.pop(id - 1)
        return True

@app.post("/libro", tags=["Libros"])
def libro_add(id: int, libro:str):
    """Agrega un libro a un usuario.

    Args:

    - id (int): Id de la persona que va a prestar el libro.
    - libro (str): Nombre del libro a prestar.

    Returns:

    - bool: Devuelve True si puede agregar el libro al usuario.
    """
    if persona_existe(id):
        personas[id - 1]["libros"].append({
            "nombre": libro,
            "fecha": str(date.today()),
            "estado": "prestado"
        })
        return True

@app.delete("/libro", tags=["Libros"])
def libro_remove(persona_id: int, libro_id:int):
    """Elimina un libro de un usuario.

    Args:

    - persona_id (int): ID de la persona que va a eliminar el libro.
    - libro_id (int): ID del libro a eliminar.

    Returns:

    - bool: Devuelve True si puede eliminar el libro del usuario.
    """
    if persona_existe(persona_id):
        libros = personas[persona_id - 1]["libros"]
        if libro_id > 0 and libro_id <= len(libros):
            libros.pop(libro_id - 1)
        return True
