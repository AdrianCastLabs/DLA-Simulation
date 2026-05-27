from math import ceil

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

gridSize = 120
grid = np.zeros((gridSize, gridSize))

grid[gridSize // 2, gridSize // 2] = 1

def SpawnParticle():
    side = np.random.randint(0, 4)

    if side == 0:  # top
        return np.random.randint(0, gridSize), 0

    if side == 1:  # bottom
        return np.random.randint(0, gridSize), gridSize - 1

    if side == 2:  # left
        return 0, np.random.randint(0, gridSize)

    if side == 3:  # right
        return gridSize - 1, np.random.randint(0, gridSize)


xPos, yPos = SpawnParticle()

fig, ax = plt.subplots()
image = ax.imshow(grid, cmap='gray', vmin=0, vmax=1)

def TouchingCluster(x, y):
    return(
        grid[x + 1, y] == 1 or
        grid[x - 1, y] == 1 or
        grid[x, y + 1] == 1 or
        grid[x, y - 1] == 1
    )

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

    if not (1 <= newX < gridSize - 1 and 1 <= newY < gridSize - 1):
        xPos, yPos = SpawnParticle()
        return

    if TouchingCluster(newX, newY):
        grid[newX, newY] = 1
        xPos, yPos = SpawnParticle()
        return

    xPos = newX
    yPos = newY



def update(frame):

    for i in range(10000):
        MoveParticle(np.random.randint(1, 5))

    image.set_array(grid)

    return [image]


animation = FuncAnimation(fig, update, interval=0)

plt.show()