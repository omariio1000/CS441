#Robby the Robot Program

import numpy as np
import random
import math
import matplotlib.pyplot as plt

worldSize = 10
canChance = 0.5
episodes = 5000
steps = 200
eta = 0.2
gamma = 0.9
epsilonInit = 0.1
epStep = 0.002
epInt = 50
epTest = 0.1

class RobbyRobot:
    def __init__(self):
        self.world = self.generate()
        self.xPos = random.randint(1, worldSize)
        self.yPos = random.randint(1, worldSize)
        self.score = 0
        self.qMat = np.zeros((3, 3, 3, 3, 3, 5))

    @staticmethod
    def generate():
        world = np.zeros((worldSize + 2, worldSize + 2))

        for i in range(worldSize + 2):
            for j in range(worldSize + 2):
                if i == 0 or i == worldSize + 1 or j == 0 or j == worldSize +1:
                    world[i][j] = 2
                elif random.uniform(0, 1) <= canChance:
                    world[i][j] = 1
                # print(int(world[i][j]), end="")
            # print()
        
        return world
    
    def current(self):
        return int(self.world[self.xPos][self.yPos])
    
    def north(self):
        return int(self.world[self.xPos][self.yPos - 1])

    def south(self):
        return int(self.world[self.xPos][self.yPos + 1])

    def east(self):
        return int(self.world[self.xPos + 1][self.yPos])

    def west(self):
        return int(self.world[self.xPos - 1][self.yPos])
    
    def pickUp(self):
        if self.world[self.xPos][self.yPos] == 1:
            self.world[self.xPos][self.yPos] = 0
            return 10
        else:
            return -1

    def move(self, direction):        
        #NORTH
        if (direction == 1): 
            ret = self.north()
            if ret != 2:
                self.yPos -= 1
            else:
                return -5

        #SOUTH
        elif (direction == 2): #
            ret = self.south()
            if ret != 2:
                self.yPos += 1
            else:
                return -5
        
        #EAST
        elif (direction == 3):
            ret = self.east()
            if ret != 2:
                self.xPos += 1
            else:
                return -5

        #WEST
        else: 
            ret = self.west()
            if ret != 2:
                self.xPos -= 1
            else:
                return -5

        # print(f"({self.xPos}, {self.yPos}) C: {self.current()} n: {self.north()} s: {self.south()} e: {self.east()} w: {self.west()}")
        return 0        
    
    def getState(self):
        return np.array([self.current(), self.north(), self.south(), self.east(), self.west()])

    def episode(self, episodeNum, testing=False):
        self.score = 0
        for i in range(steps):
            self.score += self.step(episodeNum, testing)
        
        self.world = self.generate()
        self.xPos = random.randint(1, worldSize)
        self.yPos = random.randint(1, worldSize)

        return self.score
    
    def step(self, episodeNum, testing=False):
        score = 0
        state = self.getState()
        action = self.getAction(state, episodeNum, testing)

        if action == 0:
            score = self.pickUp()
        else:
            score = self.move(action)

        newState = self.getState()

        if not testing:
            q = self.getQ(state, action)
            maxQ = self.getQ(newState, self.bestAction(newState))
            newQ = q + eta * (score + (gamma * maxQ) - q)
            self.setQ(state, action, newQ)

        return score
    
    def bestAction(self, state):
        actionVals = np.zeros(5)
        for i in range(len(actionVals)):
            actionVals[i] = self.getQ(state, i)

        actions = np.argwhere(actionVals == max(actionVals))
        idx = random.randrange(0, len(actions))
        return actions[idx]
    
    def getAction(self, state, episode, testing):
        if testing:
            epsilon = epTest
        else:
            epsilon = epsilonInit
            epsilon -= int(episode/epInt) * epStep

        if random.uniform(0, 1) < epsilon:
            action = random.randrange(0, 5)
        else:
            action = self.bestAction(state)
        
        return action
    
    def getQ(self, state, action):
        return self.qMat[int(state[0]), int(state[1]), int(state[2]), int(state[3]), int(state[4]), action]
    
    def setQ(self, state, action, value):
        self.qMat[int(state[0]), int(state[1]), int(state[2]), int(state[3]), int(state[4]), action] = value


def main(): 
    rob = RobbyRobot()

    print("Training")
    x = []
    y1 = []

    for i in range(episodes):
        score = rob.episode(i)
        if (i == 0 or i % 100 == 99):
            x.append(i)
            y1.append(score)
        print(f"Epsiode: {i}\t Score: {score}")

    print("\nTesting")
    y2 = []
    for i in range(episodes):
        score = rob.episode(0, True)
        if (i == 0 or i % 100 == 99):
            y2.append(score)
        print(f"Epsiode: {i}\t Score: {score}")

    avg = np.average(y2)
    std = np.std(y2)

    print(f"\nAverage: {avg}")
    print(f"Standard Deviation: {std}")

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(x, y1, color='g')
    ax2.plot(x, y2, color='b')

    ax1.grid()
    ax2.grid()

    ax1.set_xlim([0, episodes])
    ax1.set_ylim([0, math.ceil(np.max(y1)/100) * 100])

    ax2.set_xlim([0, episodes])
    ax1.set_ylim([0, math.ceil(np.max(y2)/100) * 100])

    ax1.set_title(label='Training Data')
    ax1.set_xlabel('Episode')
    ax1.set_ylabel('Score')
    
    ax2.set_title(label='Testing Data')
    ax2.set_xlabel('Episode')
    ax2.set_ylabel('Score')

    plt.show()

    return

if __name__ == '__main__':
    main()