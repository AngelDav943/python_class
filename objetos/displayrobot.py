import os
import robot
import math
lim = 20

def display(x=0, y=0):
    os.system('cls')
    for dy in range(1,lim):
        text = ""
        for dx in range(lim*2):
            if x == int(dx-(lim)) and y == -(dy-(lim/2)):
                text = text + "O"
            elif int(dx-(lim)) == 0:
                text = text + "|"
            elif int(dy-(lim/2)) == 0:
                text = text + "-"
            else:
                text = text + " " 
        print(text)
        
    
robo = robot.Robot("Alberto")
display(robo.x, robo.y)

def mov(opcion):
    match str(opcion).lower():
        case 'w':
            robo.vertical(1)
        case 's':
            robo.vertical(-1)
        case 'a':
            robo.horizontal(-1)
        case 'd':
            robo.horizontal(1)

while True:
    opcion = input("wasd => ")
    for t in opcion:
        mov(t)
    
    if abs(robo.x) >= lim:
        robo.x = (robo.x * -1)
    if abs(robo.y) >= (lim/2):
        robo.y = (robo.y * -1)
        
    robo.x = max(-lim+1, min(robo.x, lim-1))
    robo.y = max(-(lim/2), min(robo.y, (lim/2)-1))
    
    display(robo.x, robo.y)
    print(robo.posicion())