from math import ceil

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
gridSize = 120
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
        grid[newX, newY] = 0
        newX += 1
    if direction == 2:
        grid[newX, newY] = 0
        newY -= 1
    if direction == 3:
        grid[newX, newY] = 0
        newX -= 1
    if direction == 4:
        grid[newX, newY] = 0
        newY += 1

    if not CheckCollisions(newX, newY):
        grid[xPos, yPos] = 1
        xPos = ceil(gridSize / 2)
        yPos = ceil(gridSize / 2)

    if CheckCollisions(newX, newY):
        grid[newX, newY] = 1
        xPos = newX
        yPos = newY

def CheckCollisions(newX, newY):

    if not (1 <= newX < gridSize - 1 and 1 <= newY < gridSize - 1):
        return False

    isNotColliding = (
        grid[newX + 1, newY] == 0 and
        grid[newX - 1, newY] == 0 and
        grid[newX, newY + 1] == 0 and
        grid[newX, newY - 1] == 0
    )

    return isNotColliding

def update(frame):
    for i in range(10000):
        MoveParticle(np.random.randint(1, 5))

    image.set_array(grid)

    return [image]

animation = FuncAnimation(fig, update, interval=0)
plt.show()