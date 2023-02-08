monedas = {
    "euro": "€",
    "dolar": "$",
    "yen": "¥"
}
for val in monedas.items():
    for item in val:
        print(item)

while True:
    try:
        valor = input("Inserte el nombre de una moneda (euro, dolar o yen) =>")
        print(str(valor).upper() + ":", monedas[str(valor).lower()])
        break
    except:
        print("Nombre de moneda no valida, intenta de nuevo..")