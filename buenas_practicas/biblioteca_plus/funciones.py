from datetime import date 
personas:dict = {}

def agregar(nombre:str, libro:str) -> str:
    """
        Agrega un usuario a los datos de la biblioteca o un nuevo libro a un usuario existente.

        --params--
        - nombre (string): Nombre de la persona que va a prestar el libro.
        - libro (string): Nombre del libro que va a prestar.

        --return--
        - libro (string): Devuelve el libro si el usuario a sido creado correctamente.
    """
    if (not (str(nombre).lower() in personas.keys())): # Si NO existe:
        if nombre.isspace() == False:
            personas[str(nombre).lower()] = {} 

    if libro.isspace() == False:
        persona = personas[str(nombre).lower()]
        persona[str(libro).lower()] = str(date.today())
        return persona[str(libro).lower()]
    
def eliminarlibro(nombre:str, libro:str) -> str:
    """
        Elimina el libro del usuario.

        --params--
        - nombre (string): Nombre de la persona que tenga el libro.
        - libro (string): Nombre del libro que vas a eliminar.

        --return--
        - nombre (string): Si existe, devuelve el nombre del libro que eliminastes.
    """
    if str(nombre).lower() in personas: # Verifica si usuario existe
        persona = personas[str(nombre).lower()]
        if str(libro).lower() in persona:
            persona.pop(str(libro).lower())
            return nombre

def eliminar(nombre:str) -> str:
    """
        Elimina el usuario de la lista de usuarios.

        --params--
        - nombre (string): Nombre de la persona que vas a eliminar.

        --return--
        - nombre (string): Si la persona existe, devuelve el nombre del usuario que eliminastes.
    """
    if str(nombre).lower() in personas: # Verifica si usuario existe
        personas.pop(str(nombre).lower())
        return nombre

    return None

def buscar(nombre:str) -> str:
    """
        Busca los datos de el usuario existente.

        --params--
        - nombre (string): Nombre de la persona que vas a buscar.

        --return--
        - usuario ()
    """
    if str(nombre).lower() in personas: # Verifica si usuario existe
        persona = personas[str(nombre).lower()]
        return persona

def visualizar() -> dict:
    """
        Visualiza todos los datos de los usuarios.

        --return--
        - usuarios (dict): Diccionario con todos los datos.
    """
    return personas

if __name__ == "__main__":
    pass