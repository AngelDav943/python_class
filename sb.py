
class Animal():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def movimiento(self):
        print(self.nombre, "se esta moviendo.")

class Perro(Animal):
    pass

perro = Perro("roky")
perro.movimiento()