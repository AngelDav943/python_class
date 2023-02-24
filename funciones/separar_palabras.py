frase = input("ESCRIBE UNA FRASE, porfa! \n=> ")
frase_lista = {}
frase_lista[frase] = []

def nueva_palabra(palabra:str):
    frase_lista[frase].append(
        {
            "palabra": palabra,
            "longitud": len(palabra)
        }
    )

for palabra in frase.split(" "):
    nueva_palabra(palabra)

print(frase_lista)