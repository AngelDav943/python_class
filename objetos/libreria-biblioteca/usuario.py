class persona():
    def __init__(self, nombre) -> None:
        self.nombre = str(nombre).lower()
        self.libros : dict = {}
        
    def agregar_libro(self, nombre, fecha):
        libro = str(nombre).lower()
        self.libros[libro] = fecha
        
    def eliminar_libro(self, nombre):
        if self.libros in str(nombre).lower():
            self.libros.remove(str(nombre).lower())
            
    def consultar(self):
        return self.libros
            
    def __str__(self) -> str:
        return self.nombre