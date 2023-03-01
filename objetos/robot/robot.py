class Robot():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.x = 0
        self.y = 0
        pass
    
    def vertical(self, n):
        self.y = self.y + n
    
    def horizontal(self, n):
        self.x = self.x + n
    
    def posicion(self):
        return {"x": self.x, "y": self.y}

if __name__ == "__main__":
    robo = Robot("Alberto")
    print(robo.nombre, "ubicado en", robo.posicion())

    while True:
        opcion = input("wasd => ")
        match str(opcion).lower():
            case 'w':
                robo.vertical(1)
            case 's':
                robo.vertical(-1)
            case 'a':
                robo.horizontal(-1)
            case 'd':
                robo.horizontal(1)
            
        print(robo.nombre, "ubicado en", robo.posicion())