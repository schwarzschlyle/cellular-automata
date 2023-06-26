import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image


def game_of_life(size=100, steps=100):
    
    # we can start with an initial state
    grid = np.random.choice([0, 1], size=(size, size), p=[0.7, 0.3])
    
    def next_generation(old_grid):
        new_grid = np.zeros_like(old_grid)
        # this is an implementation of the game of life algorithm 
        # shown on the slides
        for i in range(1, size - 1):
            for j in range(1, size - 1):
                neighbors = old_grid[i-1:i+2, j-1:j+2]
                count = np.sum(neighbors) - old_grid[i, j]
                if old_grid[i, j] == 1:
                    if count in [2, 3]:
                        new_grid[i, j] = 1
                else:
                    if count == 3:
                        new_grid[i, j] = 1
        return new_grid

    grid_history = [grid.copy()]
    
    for _ in range(steps):
        grid = next_generation(grid)
        grid_history.append(grid.copy())
    
    return grid_history

def animate_game_of_life(grid_history):
    fig, ax = plt.subplots()
    ax.axis('off')

    img = ax.imshow(grid_history[0], cmap='binary', interpolation='nearest')

    def animate(i):
        img.set_array(grid_history[i])
        return img,

    anim = animation.FuncAnimation(fig, animate, frames=len(grid_history), interval=100, blit=True)

    # save animation as GIF
    anim.save('game_of_life_animation.gif', writer='pillow')

# Exxample usage
grid_history = game_of_life(size=100, steps=100)
animate_game_of_life(grid_history)
