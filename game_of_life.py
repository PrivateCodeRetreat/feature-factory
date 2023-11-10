class GameOfLife:
    def __init__(self):
        self.alive_cells = set()
        self.cell_ages = {}

    def __str__(self) -> str:
        height = self.get_max_y() + 1
        width = self.get_max_x() + 1
        return "\n".join(["".join([f"{self.get_age(x,y)}" if self.is_alive(x, y) else " " for x in range(width)]) for y in range(height)])
    
    def get_max_x(self):
        return max([cell[0] for cell in self.alive_cells], default=0)
    
    def get_max_y(self):
        return max([cell[1] for cell in self.alive_cells], default=0)

    def set_alive(self, x, y):
        self.alive_cells.add((x, y))
        self.cell_ages[(x, y)] = 1

    def is_alive(self, x, y):
        return (x, y) in self.alive_cells

    def get_age(self, x, y):
        return self.cell_ages.get((x, y), 0)

    def advance(self):
        new_alive_cells = set()
        new_cell_ages = {}
        neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1),
                            ( 0, -1),          ( 0, 1),
                            ( 1, -1), ( 1, 0), ( 1, 1)]

        potential_cells = {neighbor for cell in self.alive_cells for neighbor in 
                           [(cell[0] + dx, cell[1] + dy) for dx, dy in neighbor_offsets]}

        for cell in potential_cells:
            alive_neighbors = sum((neighbor in self.alive_cells) for neighbor in 
                                  [(cell[0] + dx, cell[1] + dy) for dx, dy in neighbor_offsets])
            current_age = self.cell_ages.get(cell, 0)

            if alive_neighbors == 3 or (alive_neighbors == 2 and cell in self.alive_cells):
                new_alive_cells.add(cell)
                new_cell_ages[cell] = current_age + 1

        self.alive_cells = new_alive_cells
        self.cell_ages = new_cell_ages