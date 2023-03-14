import os
import time

def display(res, pos):
    os.system("cls")
    output = []
    for ry in range(res[1]):
        output.append(list(" " * res[0]))
    
    if pos[0] < res[0] and pos[1] < res[1]:
        if pos[0] > 0 and pos[1] > 0:
            output[pos[1]][pos[0]] = "O"
            
    for txt in output:
        print("".join(txt))

res = [50,10]   # x , y
pos = [5,5]     # x , y
vel = [1,1]     # x , y
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