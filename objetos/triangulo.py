class Triangulo():
    def __init__(self, a, b, c) -> None:
        self.lados = [a, b, c]
        
    def ladoMayor(self) -> float:
        mayor = max(self.lados)
        return mayor
    
    def tipo(self):
        conjunto = set(self.lados)
        if len(conjunto) == 3:
            return "escaleno"
        elif len(conjunto) == 2:
            return "isoseles"
        else:
            return "equilatero"

lad = []
for i in range(3):
    lad.append( int(input("Ingresa el lado " + str(i+1) + " => " )) )
trian = Triangulo(lad[0],lad[1],lad[2])

print("El triangulo es ", trian.tipo())