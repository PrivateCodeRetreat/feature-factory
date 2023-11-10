from approvaltests.approvals import verify, verify_all

from approvaltests.reporters.python_native_reporter import PythonNativeReporter
from approvaltests import Options, verify_as_json
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from approvaltests import set_default_reporter
from approvaltests.storyboard import Storyboard

from game_of_life import GameOfLife

import tkinter as tk

class TkinterGui:

    def __init__(self, game_of_life,width=10,height=10):
        self.width = width
        self.height = height
        self.game = game_of_life
        self.root = tk.Tk()
        self.root.title("Game of Life")
        self.cell_size = 10
        self.frame_duration = 400
        self.cells = {}
        self.create_widgets()
    
    def show(self):
        self.root.after(self.frame_duration, self.advance_turn)
        self.root.mainloop()
    
    def advance_turn(self):
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

def test_tkinter_gui():
    game = GameOfLife()
    create_glider_at(game, 0, 0)
    gui = TkinterGui(game)
    gui.show()

def create_square_at(game,x,y):
    game.set_alive(x+0,y+0)
    game.set_alive(x+0,y+1)
    game.set_alive(x+1,y+0)
    game.set_alive(x+1,y+1)

def create_glider_at(game,x,y):
    game.set_alive(x+0,y+1)
    game.set_alive(x+1,y+2)
    game.set_alive(x+2,y+0)
    game.set_alive(x+2,y+1)
    game.set_alive(x+2,y+2)

def verify_story_board(game,steps):
    storyboard = Storyboard()
    storyboard.add_frame(game)
    for i in range(steps):
        game.advance()
        storyboard.add_frame(game)
    verify(storyboard)

def test_game_of_life():
    game = GameOfLife()
    create_glider_at(game, 0, 0)
    verify_story_board(game,4)

def test_game_of_life_with_blinker():
    game = GameOfLife()
    game.set_alive(1, 1)
    game.set_alive(1, 2)
    game.set_alive(1, 3)
    game.advance()
    assert game.is_alive(0, 2)
    assert game.is_alive(1, 2)
    assert game.is_alive(2, 2)

def test_square_age():
    game = GameOfLife()
    create_square_at(game,0,0)
    assert game.get_age(3,3) == 0
    assert game.get_age(0,0) == 1
    game.advance()
    assert game.get_age(0,0) == 2