class Alumno():
    minimo = 70
    
    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = nota
        
    def aprobado(self):
        if self.nota >= self.minimo:
            print("Aprovado")
        else:
            print("No aprovado")

a = Alumno("David", 70)
a.aprobado()