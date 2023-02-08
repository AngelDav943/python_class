carrito = {}
while True:
    print("\nArticulos:",len(carrito), "(Presiona X para salir)")
    articulo = input("¿Que articulo desea comprar? => ")
    if articulo.lower() == "x":
        break

    precio = input("¿Cual es el precio de " + articulo + "? => ")
    if precio.lower() == "x":
        break

    if precio.isnumeric():
        carrito.update({articulo: int(precio)})
    else:
        print("Precio tiene que ser un numero, Intenta de nuevo.")

total = 0
print("\nCarrito de compras: (", len(carrito), "articulos)")
for articulo, precio in carrito.items():
    total = total + precio
    print("\t",articulo, "a", precio)
print("\tTOTAL:", total)