persona = {}
while True:
    try:
        persona.update({
            "nombre": str(input("Cual es tu nombre? => ")),
            "apellido": str(input("Cual es tu apellido? => ")),
            "edad":   int(input("Cuantos años tienes? => "))
        })
        break
    except:
        print("Valor no valido, intenta de nuevo")

for key, value in persona.items():
    print("Tu",key,"es",value)