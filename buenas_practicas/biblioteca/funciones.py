personas:dict = {}

def agregar(nombre:str, libro:str) -> str:
    """
        Agrega un usuario a los datos de la biblioteca.

        --params--
        - nombre (string): Nombre de la persona que va a prestar el libro.
        - libro (string): Nombre del libro que va a prestar.

        --return--
        - libro (string): Devuelve el libro si el usuario a sido creado correctamente.
    """
    if (not (str(nombre).lower() in personas.keys())):
        if nombre.isspace() == False and libro.isspace() == False:
            personas[str(nombre).lower()] = libro
            return libro

    return None

def actualizar(nombre:str, nuevo_libro:str) -> str:
    """
        Actualiza un usuario ya existente a los datos de la biblioteca.

        --params--
        - nombre (string): Nombre de la persona que vas a actualizar.
        - libro (string): Nombre del nuevo libro.

        --return--
        - libro (string): Devuelve el libro si el usuario existe.
    """
    if str(nombre).lower() in personas: # Verifica si usuario existe
        personas[str(nombre).lower()] = nuevo_libro
        libro:str = nuevo_libro
        return libro

    return None

def eliminar(nombre:str) -> str:
    """
        Elimina el usuario de la lista de usuarios.

        --params--
        - nombre (string): Nombre de la persona que vas a eliminar.

        --return--
        - nombre (string): Si la persona existe, devuelve el nombre del usuario que eliminastes.
    """
    if str(nombre).lower() in personas: # Verifica si usuario existe
        personas.pop(nombre)
        return nombre

    return None

def buscar(nombre:str) -> str:
    """
        Busca los datos de el usuario existente.

        --params--
        - nombre (string): Nombre de la persona que vas a buscar.

        --return--
        - libro (string): El libro que a prestado el usuario.
    """
    if str(nombre).lower() in personas: # Verifica si usuario existe
        libro:str = personas[str(nombre).lower()]
        return libro

    return None

def visualizar() -> dict:
    """
        Visualiza todos los datos de los usuarios.

        --return--
        - usuarios (dict): Diccionario con todos los datos.
    """
    return personas

if __name__ == "__main__":
    pass