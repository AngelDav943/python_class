import random
from robot.robot import Robot

class Robot1(Robot):
    def vertical(self, n):
        self.y = self.y + (n*2)
    
    def horizontal(self, n):
        self.x = self.x + (n*2)
        

class Robot2(Robot):
    def saltar(self):
        self.x = self.x + random.randrange(-3,3)
        self.y = self.y + random.randrange(-3,3)
        
ne = Robot2("ang")
print(ne.posicion())
ne.saltar()
print(ne.posicion())