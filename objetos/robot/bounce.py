from robot import Robot
from displayrobot import display
import time

robo = Robot("alberto")

horizont = 1
vertical = -1

while True:
    robo.horizontal(horizont)
    robo.vertical(vertical)
    
    hit = display(robo, robo.x, robo.y)
    
    if hit["x"] == True:
        horizont = horizont * -1
    if hit["y"] == True:
        vertical = vertical * -1
    print(robo.posicion())
    print(hit)
    print("h:",horizont,"| v:",vertical)
    time.sleep(0.1)