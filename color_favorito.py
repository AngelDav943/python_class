import difflib

def talk(text):
    return input(str(text) + "\n")

colores = ["amarillo", "verde", "naranja", "negro", "azul", "rosado", "rojo", "blanco", "marron", "gris", "morado"]
print("hola!")
nombre = talk("Cual es tu nombre?")
color = talk(nombre + ", cual es tu color favorito?")
print(difflib.get_close_matches(color.lower(), colores))