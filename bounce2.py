import os
import time

def display(res, pos):
    os.system("cls")
    text = [list(" " * res[0])] * res[1]
    
    if pos[0] < res[0] and pos[1] < res[1]:
        if pos[0] > 0 and pos[1] > 0:
            text[pos[1]][pos[0]] = "O"
    #for dy in range(res[1]):
    #    posx = max(0, min(pos[0], res[0] - 1))
    #    if pos[1] == dy:
    #        text[posx] = "O"
    #    
    for t in text:
        print("".join(text[0]))

res = [50,10]
pos = [5,5]
vel = [1,1]
while True:
    if pos[0] >= res[0]-1 or pos[0] <= 1:
        vel[0] = vel[0] * -1
    if pos[1] >= res[1]-1 or pos[1] <= 1:
        vel[1] = vel[1] * -1
        
    pos[0] = pos[0] + vel[0]
    pos[1] = pos[1] + vel[1]
    display(res, pos)
    print(pos)
    time.sleep(0.1)