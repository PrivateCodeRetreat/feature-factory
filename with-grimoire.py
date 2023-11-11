# this code was generated from the grimoire
# link to chat: https://chat.openai.com/share/4ceab0af-225f-4bd8-8415-7b3f31172515

import tkinter as tk
import copy
import time

# Constants for the grid size and cell size
GRID_SIZE = 10
CELL_SIZE = 20

# Initialize the grid
def init_grid():
    return [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Place the glider and square on the grid
def setup_initial_state(grid):
    # Glider pattern
    grid[1][2] = grid[2][3] = grid[3][1] = grid[3][2] = grid[3][3] = 1   
    # Square pattern
    grid[8][8] = grid[8][9] = grid[9][8] = grid[9][9] = 1

# Count the alive neighbors of a cell
def count_neighbors(grid, x, y):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x+i < GRID_SIZE and 0 <= y+j < GRID_SIZE:
                neighbors += grid[x+i][y+j]
    return neighbors

# Update the grid based on the Game of Life rules
def update_grid(grid):
    new_grid = copy.deepcopy(grid)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i][j] = 0
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
    return new_grid

# Draw the grid using Tkinter
def draw_grid(canvas, grid):
    canvas.delete("all")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = "black" if grid[i][j] == 1 else "white"
            canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill=color, outline="gray")

def main():
    root = tk.Tk()
    root.title("Game of Life")
    canvas = tk.Canvas(root, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE)
    canvas.pack()

    grid = init_grid()
    setup_initial_state(grid)

    def update():
        nonlocal grid
        grid = update_grid(grid)
        draw_grid(canvas, grid)
        root.after(500, update)

    update()
    root.mainloop()

if __name__ == "__main__":
    main()
