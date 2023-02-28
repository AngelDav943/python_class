class persona:
    sentidos = ["Tacto", "Vista", "Olfato"]
    
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.libros = {}
        
    def __str__(self) -> str:
        return self.nombre
        
    def hola(self) -> str:
        print("Hola soy", self.nombre)
    
    def agregar_libro(self, nombre, fecha):
        self.libros[nombre] = fecha

juan = persona("juan", 20)
gabriel = persona("gabriel", 15)
juan.agregar_libro("libro1","24-02-2023")
juan.agregar_libro("libroB","20-06-2021")

print(gabriel.libros)
print(juan.libros)
print(type(gabriel))
