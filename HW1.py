#homework 1 problem 10

import numpy as np
import random

grid = np.zeros((3, 3))
randx = []
randy = []

def reflex(murphy):
    position = [0, 0]
    reverse = False
    actions = 0

    while np.any(grid == 1):
        moving = True
        # x = input()
        # print(f"Position: ({position[0]}, {position[1]})")
        # print(f"Action counter: {actions}\n")
        if grid[position[0]][position[1]] == 1:
            if (murphy):
                temp = round(random.uniform(1, 10.0))
                if (temp != 10):
                    moving = False
                    temp = round(random.uniform(1, 4.0))
                    if (temp != 4):
                        grid[position[0]][position[1]] = 0 #suck
                #     else:
                #         print("SUCK FAILED")
                # else:
                #     print("SENSOR FAILED")
            else:
                grid[position[0]][position[1]] = 0 #suck
                moving = False
        
        if moving:
            if position == [0, 0]:
                reverse = False
                position = [0, 1]

            elif position == [0, 1]:
                if reverse: position = [0, 0]
                else: position = [0, 2]

            elif position == [0, 2]:
                if reverse: position = [0, 1]
                else: position = [1, 2]

            elif position == [1, 2]:
                if reverse: position = [0, 2]
                else: position = [1, 1]

            elif position == [1, 1]:
                if reverse: position = [1, 2]
                else: position = [1, 0]

            elif position == [1, 0]:
                if reverse: position = [1, 1]
                else: position = [2, 0]

            elif position == [2, 0]:
                if reverse: position = [1, 0]
                else: position = [2, 1]

            elif position == [2, 1]:
                if reverse: position = [2, 0]
                else: position = [2, 2]

            elif position == [2, 2]:
                reverse = True
                position = [2, 1]
            
        actions += 1

    return actions

def rand(murphy):
    position = [0, 0]
    actions = 0

    while np.any(grid == 1):
        suck = round(random.uniform(0, 1.0))
        if (suck == 1):
            if (murphy):
                temp = round(random.uniform(1, 4.0))
                if (temp != 4):
                    grid[position[0]][position[1]] = 0
            else:
                grid[position[0]][position[1]] = 0
        else:
            moved = False
            while not moved:
                move = round(random.uniform(1, 4.0))
                if (move == 1): #up
                    temp = position[0] - 1
                    if temp >= 0:
                        position[0] = temp
                        moved = True
                
                elif (move == 2): #down
                    temp = position[0] + 1
                    if temp <= 2:
                        position[0] = temp
                        moved = True

                elif (move == 3): #left
                    temp = position[1] - 1
                    if temp >= 0:
                        position[1] = temp
                        moved = True

                elif (move == 4): #right
                    temp = position[1] + 1
                    if temp <= 2:
                        position[1] = temp
                        moved = True
        actions += 1

    return actions

def randGen():
    randx.clear()
    randy.clear()
    for i in range(5):
        temp1 = round(random.uniform(0, 2.0))
        temp2 = round(random.uniform(0, 2.0))

        for j in range(i):
            while (randx[j] == temp1) and (randy[j] == temp2):
                temp1 = round(random.uniform(0, 2.0))
                temp2 = round(random.uniform(0, 2.0))

        randx.append(temp1)
        randy.append(temp2)
        # print(f"({randx[i]}, {randy[i]})")


            
#1 pile
reflex_1pile_list = []
random_1pile_list = []
reflex_murphy_1pile_list = []
random_murphy_1pile_list = []
for i in range(100):
    grid = np.zeros((3, 3))
    randGen()
    grid[randx[0]][randy[0]] = 1
    reflex_1pile_list.append(reflex(False))
    grid[randx[0]][randy[0]] = 1
    random_1pile_list.append(rand(False))
    grid[randx[0]][randy[0]] = 1
    reflex_murphy_1pile_list.append(reflex(True))
    grid[randx[0]][randy[0]] = 1
    random_murphy_1pile_list.append(rand(True))

reflex_1pile = sum(reflex_1pile_list) / 100.0
random_1pile = sum(random_1pile_list) / 100.0
reflex_murphy_1pile = sum(reflex_murphy_1pile_list) / 100.0
random_murphy_1pile = sum(random_murphy_1pile_list) / 100.0
print(f"Reflex Agent 1 Pile: {reflex_1pile}")
print(f"Random Agent 1 Pile: {random_1pile}")
print(f"Reflex (murphys) Agent 1 Pile: {reflex_murphy_1pile}")
print(f"Random (murphys) Agent 1 Pile: {random_murphy_1pile}\n")


#3 piles
reflex_3pile_list = []
random_3pile_list = []
reflex_murphy_3pile_list = []
random_murphy_3pile_list = []
for i in range(100):
    grid = np.zeros((3, 3))
    randGen()
    grid[randx[0]][randy[0]] = 1
    grid[randx[1]][randy[1]] = 1
    grid[randx[2]][randy[2]] = 1
    reflex_3pile_list.append(reflex(False))
    grid[randx[0]][randy[0]] = 1
    grid[randx[1]][randy[1]] = 1
    grid[randx[2]][randy[2]] = 1
    random_3pile_list.append(rand(False))
    grid[randx[0]][randy[0]] = 1
    grid[randx[1]][randy[1]] = 1
    grid[randx[2]][randy[2]] = 1
    reflex_murphy_3pile_list.append(reflex(True))
    grid[randx[0]][randy[0]] = 1
    grid[randx[1]][randy[1]] = 1
    grid[randx[2]][randy[2]] = 1
    random_murphy_3pile_list.append(rand(True))

reflex_3pile = sum(reflex_3pile_list) / 100.0
random_3pile = sum(random_3pile_list) / 100.0
reflex_murphy_3pile = sum(reflex_murphy_3pile_list) / 100.0
random_murphy_3pile = sum(random_murphy_3pile_list) / 100.0
print(f"Reflex Agent 3 Piles: {reflex_3pile}")
print(f"Random Agent 3 Piles: {random_3pile}")
print(f"Reflex (murphys) Agent 3 Piles: {reflex_murphy_3pile}")
print(f"Random (murphys) Agent 3 Piles: {random_murphy_3pile}\n")

#5 piles
reflex_5pile_list = []
random_5pile_list = []
reflex_murphy_5pile_list = []
random_murphy_5pile_list = []
for i in range(100):
    grid = np.zeros((3, 3))
    randGen()
    grid[randx[0]][randy[0]] = 1
    grid[randx[1]][randy[1]] = 1
    grid[randx[2]][randy[2]] = 1
    grid[randx[3]][randy[3]] = 1
    grid[randx[4]][randy[4]] = 1
    reflex_5pile_list.append(reflex(False))
    grid[randx[0]][randy[0]] = 1
    grid[randx[1]][randy[1]] = 1
    grid[randx[2]][randy[2]] = 1
    grid[randx[3]][randy[3]] = 1
    grid[randx[4]][randy[4]] = 1
    random_5pile_list.append(rand(False))
    grid[randx[0]][randy[0]] = 1
    grid[randx[1]][randy[1]] = 1
    grid[randx[2]][randy[2]] = 1
    grid[randx[3]][randy[3]] = 1
    grid[randx[4]][randy[4]] = 1
    reflex_murphy_5pile_list.append(reflex(True))
    grid[randx[0]][randy[0]] = 1
    grid[randx[1]][randy[1]] = 1
    grid[randx[2]][randy[2]] = 1
    grid[randx[3]][randy[3]] = 1
    grid[randx[4]][randy[4]] = 1
    random_murphy_5pile_list.append(rand(True))

reflex_5pile = sum(reflex_5pile_list) / 100.0
random_5pile = sum(random_5pile_list) / 100.0
reflex_murphy_5pile = sum(reflex_murphy_5pile_list) / 100.0
random_murphy_5pile = sum(random_murphy_5pile_list) / 100.0
print(f"Reflex Agent 5 Piles: {reflex_5pile}")
print(f"Random Agent 5 Piles: {random_5pile}")
print(f"Reflex (murphys) Agent 5 Piles: {reflex_murphy_5pile}")
print(f"Random (murphys) Agent 5 Piles: {random_murphy_5pile}")