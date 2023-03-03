import os
import math
import random
import time

class objeto():
    def __init__(self, txt, x, y) -> None:
        self.txt = txt
        self.x = x
        self.y = y
        self.hit = {"x":False, "y":False}
        self.vel = {"x":random.randrange(-1,1), "y":random.randrange(-1,1)}
    
    def vertical(self, n):
        self.y = self.y + n
    
    def horizontal(self, n):
        self.x = self.x + n

lim = 20
def display(objs : list):
    os.system('cls')
    for dy in range(1,lim):
        text = list(" " * (lim*2))
        for dx in range(lim*2):
            for obj in objs:
                if obj.x == int(dx-(lim)) and obj.y == -(dy-(lim/2)):
                    text[dx] = obj.txt
                elif int(dx-(lim)) == 0:
                    text[dx] = "|"
                elif int(dy-(lim/2)) == 0:
                    text[dx] = "-"
        print("".join(text))
        
def hitdet(objs):
    for obj in objs:
        if abs(obj.x) >= lim-1:
            obj.hit["x"] = True
        if abs(obj.y) >= (lim/2)-1:
            obj.hit["y"] = True
        
objetos = [
    objeto("O", 0, 0),
    objeto("X", 5, 2),
    objeto("P", 1, -5),
    objeto("R", 2, -3)
]

while True:
    for obj in objetos:
        obj.horizontal(obj.vel["x"])
        obj.vertical(obj.vel["y"])
        
        hitdet(objetos)
        
        if obj.hit["x"] == True:
            obj.vel["x"] = obj.vel["x"] * -1
        if obj.hit["y"] == True:
            obj.vel["y"] = obj.vel["y"] * -1
    display(objetos)
    time.sleep(0.1)