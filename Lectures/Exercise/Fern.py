import random
import matplotlib.pyplot as plt
import numpy as np

# Size of plot
size = (300, 300)

# Start with random coordinates
x, y = random.random(), random.random()

# Start with no points
points = []

# Repeat many times
for i in range(500000):
    # Random number decides action to take
    rand = random.random()

    # This recursion is described in detail
    if rand < 0.01:
        x, y = 0.0, 0.16 * y
    elif rand < 0.86:
        newx = (0.85 * x) + (0.04 * y)
        newy = (-0.04 * x) + (0.85 * y) + 1.6
        x, y = newx, newy
    elif rand < 0.92:
        newx = (0.02 * x) - (0.26 * y)
        newy = (0.23 * x) + (0.22 * y) + 1.6
        x, y = newx, newy
    else:
        newx = (-0.15 * x) + (0.28 * y)
        newy = (0.26 * x) + (0.24 * y) + 0.44
        x, y = newx, newy


plt.scatter(points[:,0],points[:,1],edgecolor='none', s=0.5, color='green') # set opacity
# Remove the axes
plt.axis('off')
plt.show()