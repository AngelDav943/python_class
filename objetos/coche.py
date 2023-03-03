class Coche():
    def __init__(self, matricula, marca, km, gasolina) -> None:
        self.matricula = matricula
        self.marca = marca
        self.kilometros = km
        self.gasolina = gasolina
        
    def avanzar(self, km) -> bool:
        print(self.gasolina - km)
        if self.gasolina - km >= 0:
            self.gasolina = self.gasolina - km
            self.kilometros = self.kilometros + km
            return True
        
        print("No hay suficiente gasolina.")
        return False
        
        
carro = Coche("QHY451", "Chevrolet", 45, 20)
print(carro.avanzar(20))