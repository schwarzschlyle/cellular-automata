import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Implementation of Wolfram's rule
n = 30
rule = [n // 2**i % 2 for i in range(8)]

width = 80
height = 32

# Creaiting a 2D grid to represent the cellular automaton
grid = np.zeros((height, width), dtype=int)
grid[0, width//2] = 1

# Create a figure and axis for the animation
fig, ax = plt.subplots()

# Create an empty plot with initial values
cells = ax.imshow(grid, cmap='binary')

#remove the axis
ax.axis('off')

# Function to update the plot for each generation
def update_plot(i):
    global grid

    # Update the specific row for the current iteration
    row = i + 1

    for col in range(1, width-1):
        # Apply the rule to the cell at (row, col)
        grid[row, col] = rule[4*grid[row-1, col-1] + 2*grid[row-1, col] + grid[row-1, col+1]]

    # Update the plot with the new generation
    cells.set_array(grid)

    return [cells]

# Animate the cellular automaton
animation = animation.FuncAnimation(fig, update_plot, frames=height-1, blit=True)

# Save the animation as a GIF file
animation.save('cellular_automaton.gif', writer='pillow')

# Show the animation
plt.show()
