import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

grid = np.zeros((100, 100))

xPos = 50
yPos = 50

grid[xPos, yPos] = 1

fig, ax = plt.subplots()
image = ax.imshow(grid, cmap='gray', vmin=0, vmax=1)

def MoveParticle(direction):
    global xPos
    global yPos

    if direction == 1:
        grid[xPos + 1, yPos + 0] = 1
        #grid[xPos, yPos] = 0
        xPos += 1
    if direction == 2:
        grid[xPos + 0, yPos - 1] = 1
        #grid[xPos, yPos] = 0
        yPos -= 1
    if direction == 3:
        grid[xPos - 1, yPos + 0] = 1
        #grid[xPos, yPos] = 0
        xPos -= 1
    if direction == 4:
        grid[xPos + 0, yPos + 1] = 1
        #grid[xPos, yPos] = 0
        yPos += 1

def update(frame):
    global xPos
    global yPos

    MoveParticle(np.random.randint(1, 5))

    image.set_array(grid)

    return [image]

animation = FuncAnimation(fig, update, interval=0)
plt.show()