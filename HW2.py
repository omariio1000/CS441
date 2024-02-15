#homework 2 problem 13

import numpy as np
import random

def function(x, y):
    return (5*(x**2)) + (40 * x) + (y**2) - (12*y) + 127

def gradient(x, y):
    return (((10 * x) + 40, (y - 12)))

etas = np.array([.1, .01, .001])
steps = 500

results = np.zeros((3, 3, 10))

for i in range(np.size(etas)):
    print(f"Step size: {etas[i]}")
    for k in range(10):
        x = np.zeros(2)
        x[0] = random.uniform(-10.0, 10.0)
        x[0] = round(x[0], i + 1)
        x[1] = random.uniform(-10.0, 10.0)
        x[1] = round(x[1], i + 1)
        
        # print(f"({x[0]}, {x[1]})")

        min = []
        min.append(np.zeros(3))
        min[0][0] = function(x[0], x[1])
        min[0][1] = x[0]
        min[0][2] = x[1]   
        
        for j in range(steps):
            min.append(np.zeros(3))
            ret = gradient(min[j][1], min[j][2])
            min[j + 1][1] = min[j][1] - (etas[i] * ret[0])
            min[j + 1][2] = min[j][2] - (etas[i] * ret[1])
            min[j + 1][0] = function(min[j+1][1], min[j+1][2])

            if (min[j + 1][0] > min[j][0]):
                break
        
        results[i, 0, k] = min[-2][0]
        results[i, 1, k] = min[-2][1]
        results[i, 2, k] = min[-2][2]
        # print(f"({min[-2][1]}, {min[-2][2]})")
    
    print(f"Average value: ({round(np.average(results[i][1]), i + 1)}, {round(np.average(results[i][2]), i + 1)})")
    
    bestIdx = np.argmin(results[i][0])
    print(f"Best value: ({round(results[i][1][bestIdx], i + 1)}, {round(results[i][2][bestIdx], i + 1)})\n")

# print(results)