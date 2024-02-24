#8 Queens Program
import random
import math
import matplotlib.pyplot as plt
import numpy as np

popSize = 1000
numIterations = 1000
mutationPct = 0.01
boardSize = 8

class board:
    def __init__(self, queens = None):
        self.queens = queens
        if (self.queens == None):
            self.queens = []
            self.queens = list(range(boardSize))
            random.shuffle(self.queens)

        self.fitness = checkFitness(self.queens)

def printBoard(queens):
    for i in range(boardSize):
        for j in range(boardSize):
            if (queens[j] == i):
                print(" Q ", end="")
            else:
                print(" - ", end="")
        print()
    print()

def attacking(c1, r1, c2, r2) -> bool:
    if (r1 == r2):
        return True
    
    if (r1 + c1) == (r2 + c2):
        return True
    
    if ((boardSize - 1 - r1) + c1) == ((boardSize - 1 - r2) + c2):
        return True

    return False

def checkFitness(queens):
    maxAttacks = math.comb(boardSize, 2)
    attackCount = 0
    for i in range(boardSize):
        for j in range(i + 1, boardSize):
            if attacking(i, queens[i], j, queens[j]):
                attackCount += 1
    return maxAttacks - attackCount + 1

def selectParents(pop):
    totalPop = popFit(pop)
    p1Fit = random.randrange(0, totalPop)
    p2Fit = random.randrange(0, totalPop)

    p1 = p2 = pop[0]  

    counter = 0
    for i in range(len(pop)):
        if counter >= p1Fit:
            p1 = pop[i]
            break
        counter += pop[i].fitness

    counter = 0
    for i in range(len(pop)):
        if counter >= p2Fit:
            p2 = pop[i]
            counter += pop[i].fitness
            break
        counter += pop[i].fitness

    return p1, p2

def crossover(p1, p2):   
    c1 = c2 = []
    randLoc = random.randrange(1, boardSize - 1)
    for i in range(0, boardSize):
        for j in range(0, randLoc):
            if p2.queens[i] == p1.queens[j]:
                c1.append(p2.queens[i])
    
    for i in range(randLoc, boardSize):
        c1.append(p1.queens[i])

    for i in range(0, randLoc):
        c2.append(p2.queens[i])
    
    for i in range(0, boardSize):
        for j in range(randLoc, boardSize):
            if p1.queens[i] == p2.queens[j]:
                c2.append(p1.queens[i])

    c1 = mutate(c1)
    c2 = mutate(c2)

    return board(c1), board(c2)
    
def mutate(c):
    
    if random.uniform(0, 1) < mutationPct:
        i = random.sample(range(0, boardSize), 2)
        temp = c[i[0]]
        c[i[0]] = c[i[1]]
        c[i[1]] = temp

    return c

def popFit(pop, average = False):
    totalFit = 0
    for i in pop:
        totalFit += i.fitness
    
    if not average:
        return totalFit
    
    return totalFit / ((math.comb(boardSize, 2) + 1) * popSize)

def maxFit(pop, printed):
    maxFit = 0
    solution = -1
    for i in range(len(pop)):
        if (pop[i].fitness > maxFit):
            maxFit = pop[i].fitness

        if not printed and (pop[i].fitness == math.comb(boardSize, 2) + 1):
            solution = i

    return maxFit, solution

def main():
    printedSolution = False

    children = []
    for i in range(popSize):
        children.append(board())

    initPrint = random.randint(0, popSize - 1)
    print(f"\nPrinting random example of initial population (Idx: {initPrint}, Fitness: {children[initPrint].fitness}): ")
    printBoard(children[initPrint].queens)

    improveCount = 0
    x = np.empty(1)
    y = np.empty(1)
    y2 = np.empty(1)
    
    fitness = popFit(children, True)
    maxFitness, solution = maxFit(children, True)

    print(f"Average Fitness (Gen 0): \t{fitness:.3f}")
    x = np.append(x, 0)
    y = np.append(y, fitness)
    y2 = np.append(y2, maxFitness)

    for i in range(numIterations):
        parents = children
        children = []

        for j in range(int(popSize/2)):
            p1, p2 = selectParents(parents)
            c1, c2 = crossover(p1, p2)

            pFit = checkFitness(p1.queens) + checkFitness(p2.queens)
            cFit = checkFitness(c1.queens) + checkFitness(c2.queens)
            
            # print(f"P: {pFit}, C: {cFit}")

            if cFit > pFit:
                improveCount += 1
            if cFit == pFit and random.randint(0, 1) == 1:
                improveCount += 1

            children.append(c1)
            children.append(c2)
        
        fitness = popFit(children, True)
        maxFitness, solution = maxFit(children, printedSolution)

        if (solution != -1):
            initPrint = random.randint(0, popSize - 1)
            print(f"\nPrinting sample solution (Gen {i + 1}, Idx: {solution}, Fitness: {children[solution].fitness}): ")
            printBoard(children[solution].queens)
            printedSolution = True

        print(f"Average Fitness (Gen {i + 1}): \t{fitness:.3f}")
        x = np.append(x, i + 1)
        y = np.append(y, fitness)
        y2 = np.append(y2, maxFitness)

    finPrint = random.randint(0, popSize - 1)
    print(f"\nPrinting random example of final population (Idx: {finPrint}, Fitness: {children[finPrint].fitness}): ")
    printBoard(children[finPrint].queens)

    print(f"\n{((improveCount / ((popSize/2) * numIterations)) * 100):.3f}% of children improved upon their parents")

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.plot(x, y, color='g')
    ax2.plot(x, y2, color='b')

    ax1.grid()
    ax2.grid()

    ax1.set_xlim([0, numIterations])
    ax1.set_ylim([0.6, 1.0])

    ax2.set_xlim([0, numIterations])
    ax2.set_ylim([24, math.comb(boardSize, 2) + 2])

    ax1.set_title(label='Generations vs. Average Fitness')
    ax1.set_xlabel('Generation Number')
    ax1.set_ylabel('Average Fitness')
    
    ax2.set_title(label='Generations vs. Best Fitness')
    ax2.set_xlabel('Generation Number')
    ax2.set_ylabel('Best Fitness (higher is better)')

    plt.show()
    return


if __name__ == '__main__':
    main()