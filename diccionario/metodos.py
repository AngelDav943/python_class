carro = { # Diccionario
    "Marca":"Ford",
    "Modelo": "Mustang",
    "Año": 1964
}
print(carro)
carro.update({"Año":2025, "Color": "Rojo", "Precio":244490000}) # Agregar datos al diccionario
print(carro)
carro.pop("Año") # Eliminar Año del diccionario
print(carro)
del carro["Modelo"] # Eliminar Modelo de carro
print(carro)
carro.clear() # Vaciar diccionario
print(carro)