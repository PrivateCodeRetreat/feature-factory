import tkinter as tk


class TkinterGui:

    def __init__(self, game_of_life,width=10,height=10):
        self.width = width
        self.height = height
        self.game = game_of_life
        self.root = tk.Tk()
        self.root.title("Game of Life")
        self.cell_size = 10
        self.frame_duration = 250
        self.cells = {}
        self.create_widgets()

    def show(self, num_of_iterations=-1):
        self.iterations = 0
        self.num_of_iterations = num_of_iterations
        self.root.after(self.frame_duration, self.advance_turn)
        self.root.mainloop()

    def advance_turn(self):
        if self.iterations == self.num_of_iterations:
            self.root.destroy()
            return
        self.iterations += 1
        self.game.advance()
        self.update_cells()
        self.root.after(self.frame_duration, self.advance_turn)

    def create_widgets(self):
        for x in range(self.width):
            for y in range(self.height):
                cell_frame = tk.Frame(self.root, width=self.cell_size, height=self.cell_size,
                                      borderwidth=1, relief='raised')
                cell_frame.grid(row=y, column=x)
                cell = tk.Label(cell_frame, bg='white', width=2, height=1)
                cell.pack(padx=1, pady=1)
                self.cells[(x, y)] = cell
        self.update_cells()

    def update_cells(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.game.is_alive(x, y):
                    self.cells[(x, y)].config(bg='blue')
                    self.cells[(x, y)].config(text=self.game.get_age(x,y))
                else:
                    self.cells[(x, y)].config(bg='grey')
                    self.cells[(x, y)].config(text='')
