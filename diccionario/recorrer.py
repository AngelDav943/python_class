carro = { # Diccionario
    "Marca":"Ford",
    "Modelo": "Mustang",
    "Año": 1964
}

for key in carro:
    print(key) # Imprime las llaves como "Marca", "Modelo" y "Año"

for key, value in carro.items():
    print(key, "=>", value) # key es la clave y value el valor de la clave