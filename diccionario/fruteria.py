frutas = {
    "manzana": 6000,
    "platano": 2000,
    "pera": 5000,
    "piña": 2000
}
while True:
    try:
        for fruta, precio in frutas.items():
            print(fruta, "a", precio, "por kilo")
        fruta = str(input("Que fruta desea comprar? => "))
        precio = frutas[fruta.lower()]
        cantidad = float(input("Cuantos kilos de "+ fruta +" desea comprar? ("+str(precio)+"$ * kilo) => "))
        print(cantidad,"kilos de ", fruta + ", total: ", str(precio * cantidad) + "$")
        break
    except:
        print("Valor no valido, intenta de nuevo.")