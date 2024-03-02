#Robby the Robot Program

import numpy as np
import random
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
        self.xPos = random.randint(0, worldSize - 1)
        self.yPos = random.randint(0, worldSize - 1)
        self.score = 0
        self.qMat = np.zeros((3, 3, 3, 3, 3, 5))

    @staticmethod
    def generate():
        world = np.zeros((worldSize, worldSize))

        for i in range(worldSize):
            for j in range(worldSize):
                if random.uniform(0, 1) <= canChance:
                    world[i][j] = 1
        
        return world
    
    def current(self):
        return self.world[self.xPos][self.yPos]
    
    def north(self):
        return self.world[self.col][self.row - 1]

    def south(self):
        return self.world[self.col][self.row + 1]

    def east(self):
        return self.world[self.col + 1][self.row]

    def west(self):
        return self.world[self.col - 1][self.row]
    
    def pickUp(self):
        if self.world[self.xPos][self.yPos] == 1:
            self.world[self.xPos][self.yPos] = 0
            self.score += 10
        else:
            self.score -= 1
        return

    def move(self, direction):        
        #NORTH
        if (direction == 1): 
            try:
                self.north()
                self.yPos -= 1
            except:
                self.score -= 5

        #SOUTH
        elif (direction == 2): #
            try:
                self.south()
                self.yPos += 1
            except:
                self.score -= 5
        
        #EAST
        elif (direction == 3):
            try:
                self.east()
                self.xPos += 1
            except:
                self.score -= 5

        #WEST
        else: 
            try:
                self.west()
                self.xPos -= 1
            except:
                self.score -= 5

        return
    
    def getState(self):
        try:
            current = current()
        except:
            current = 2

        try:
            north = north()
        except:
            north = 2

        try:
            south = south()
        except:
            south = 2

        try:
            east = east()
        except:
            east = 2

        try:
            west = west()
        except:
            west = 2

        return np.array([current, north, south, east, west])

    def episode(self, episodeNum, testing=False):
        self.step(episodeNum, testing)
        
        self.world = self.generate()
        self.xPos = random.randint(0, worldSize - 1)
        self.yPos = random.randint(0, worldSize - 1)

        return self.score
    
    def step(self, episodeNum, testing=False):
        initScore = self.score
        state = self.getState()
        action = self.getAction(state, episodeNum, testing)

        if action == 0:
            self.pickUp()
        else:
            self.move(action)

        newScore = self.score
        newState = self.getState()

        if not testing:
            q = self.getQ(state, action)
            maxQ = self.getQ(newState, self.bestAction(newState))
            newQ = q + eta * ((newScore - initScore) + (gamma * maxQ) - q)
            self.setQ(state, action, newQ)

        return
    
    def bestAction(self, state):
        actionVals = np.zeros(len(state))
        for i in range(len(actionVals)):
            actionVals[i] = self.getQ(state, i)

        actions = np.argwhere(actionVals == max(actionVals))
        idx = random.randint(0, len(actions) - 1)
        return actions[idx]
    
    def getAction(self, state, episode, testing):
        if testing:
            epsilon = epTest
        else:
            epsilon = epsilonInit
            epsilon -= int(episode/epInt) * epStep

        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, len(state) - 1)
        else:
            action = self.bestAction(state)
        
        return action
    
    def getQ(self, state, action):
        return self.q[state[0], state[1], state[2], state[3], state[4], action]
    
    def setQ(self, state, action, value):
        self.q[state[0], state[1], state[2], state[3], state[4], action] = value


def main(): 
    return

if __name__ == '__main__':
    main()