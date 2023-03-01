class ser():
    sentidos = ["Olfato", "Vista", "Tacto", "Gusto", "Oido"]
    
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
    def movimiento(self):
        print(self.nombre, "se esta moviendo")
        
    def sonido(self):
        print(self.nombre, "esta haciendo un sonido")
        
class persona(ser):
    def movimiento(self):
        print(self.nombre,"esta caminando")
    
    def sonido(self):
        print(self.nombre,"esta hablando")

class gato(ser):
    def sonido(self):
        print(self.nombre,"esta maullando")

ser1 = ser("shokertec")
ser1.movimiento()

gat = persona("roky")
gat.movimiento()

david = persona("david")
david.movimiento()