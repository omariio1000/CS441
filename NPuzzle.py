#N-Puzzle Program
import random
import math
import numpy as np
import copy
import heapq as hq
from treelib import Tree, exceptions as x

goalArray = [1, 2, 3, 4, 5, 6, 7, 8, 0]

bestFirst = 0
aStar = 1

h1 = 0
h2 = 1
h3 = 2

class grid:
    def __init__(self, size, arr):
        self.size = size + 1
        self.width = int(math.sqrt(self.size))
        self.array = np.array(arr)
        self.goal = np.array(goalArray)
    
    @staticmethod
    def find(array, num):
        return np.where(array == num)[0]

    def getBlank(self):
        return self.find(self.array, 0)
    
    def swap(self, a, b):
        if a < 0 or a > self.size - 1 or b < 0 or b > self.size - 1:
            return False
        
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp
        return True

    def up(self):
        e = self.getBlank()
        if e < self.width:
            return False
        self.swap(e, e - self.width)
        return True
    
    def down(self):
        e = self.getBlank()
        if e > self.size - 1 - self.width:
            return False
        self.swap(e, e + self.width)
        return True
    
    def left(self):
        e = self.getBlank()
        if e % self.width == 0:
            return False
        self.swap(e, e - 1)
        return True
    
    def right(self):
        e = self.empty()
        if (e + 1) % self.width == 0:
            return False
        self.swap(e, e + 1)
        return True
    
    def diff(self, num, col):
        a = self.find(self.array, num)
        b = self.find(goalArray, num)
        
        diff = 0
        if (col):
            diff = abs((a % self.width) - (b % self.width))
        else:
            diff = abs((a // self.width) - (b // self.width))
        
        return diff
    

    def heuristic1(self):
        cost = 0
        for i in range(1, self.size):
            if self.diff(i, False) or self.diff(i, True):
                cost += 1
        
        return cost
    
    def heuristic2(self):
        cost = 0
        for i in range(1, self.size):
            cost += math.sqrt(pow(self.diff(i, False), 2) + pow(self.diff(i, True), 2))
        
        return cost
        
    def heuristic3(self):
        cost = 0
        for i in range(1, self.size):
            cost += self.diff(i, False) + self.diff(i, True)
        
        return cost
    
    def getString(self):
        returnStr = ""
        for i in self.array:
            returnStr = str(i).zfill(2)
        return returnStr()
    
    def solvable(self):
        if len(self.array) == 0:
            return False
        
        total = 0
        for  i in range(0, self.size - 1):
            for j in range(i + 1, self.size):
                if self.array[i] != 0 and self.array[j] != 0 and self.array[i] > self.array[j]:
                    total += 1

        return total % 2 == 0
    
    def solved(self):
        if np.array_equal(self.array, self.goalArray):
            return True
        
        return False

class node:
    def __init__(self, cost, id):
        self.cost = cost
        self.id = id
    
    def __lt__ (self, comp):
        return self.cost < comp.cost
    
class Run:
    def __init__(self, type, arr):
        self.tree = Tree()
        self.queue = []
        self.found = None
        self.type = type

        root = grid(8, arr)
        self.tree.create_node(root.getString(), root.getString(), data=root)
        hq.heappush(self.queue, node(0, root.getString()))

    def expand(self, inNode):
        for i in range(4):
            c = copy.deepcopy(inNode)
            c.parent = inNode

            if i == 0:
                c.left()
            elif i == 1:
                c.right()
            elif i == 2:
                c.up()
            elif i == 3:
                c.down()

            if c.getString() == inNode.getString():
                continue

            fail = False
            try:
                self.tree.create_node(c.getString(), c.getString(), parent=node.getString(), data=c)
            except x.DuplicatedNodeIdError:
                fail = True

            if not fail:
                cost = 0

                if self.heuristic == h1:
                    cost = c.heuristic1()
                elif self.heuritic == h2:
                    cost = c.heuristic2()
                elif self.heuristic == h3:
                    cost = c.h3()

                if self.type == aStar:
                    n = self.tree.get_node(c.getString())
                    d = self.tree.depth(n)
                    cost += d
                
                hq.heappush(self.queue, self.node(cost, c.getString()))

    def expandCheapest(self):
        cheapest = hq.heappop(self.queue)
        node = self.tree.get_node(cheapest.getString()).data

        if node.goal():
            self.found = node
        else:
            self.expand(node)

    def showPath(self, node, result):
        result.insert(0, node.arr)

    def run(self, limit=100000):
        for i in range(limit):
            self.expandCheapest()
        
        if self.found:
            print("Nodes expanded: ", i)
            path = []
            path = self.


def main():
    arrs = []
    for i in range(5):
        arrs.append(goalArray.copy())
        random.shuffle(arrs[i])

    # print(arrs)

    for i in range(2):
        for j in range(3):
            for k in range(5):
                search = "Best-First" if i == bestFirst else "A*"
                print(f"\nSearch method: {search}\tHeuristic: {j + 1}\tArray ({k + 1}): {arrs[k]}")

    return

if __name__ == '__main__':
    main()