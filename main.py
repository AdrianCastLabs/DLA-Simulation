from math import ceil

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
gridSize = 25
grid = np.zeros((gridSize, gridSize))

xPos = ceil(gridSize / 2)
yPos = ceil(gridSize / 2)

grid[xPos, yPos] = 1

fig, ax = plt.subplots()
image = ax.imshow(grid, cmap='gray', vmin=0, vmax=1)

def MoveParticle(direction):
    global xPos
    global yPos

    newX = xPos
    newY = yPos

    if direction == 1:
        newX += 1
    if direction == 2:
        newY -= 1
    if direction == 3:
        newX -= 1
    if direction == 4:
        newY += 1

    # Check bounds
    if 0 <= newX < gridSize and 0 <= newY < gridSize:
        grid[newX, newY] = 1
        xPos = newX
        yPos = newY

def update(frame):


    MoveParticle(np.random.randint(1, 5))

    image.set_array(grid)

    return [image]

animation = FuncAnimation(fig, update, interval=0)
plt.show()