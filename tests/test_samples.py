from approvaltests.approvals import verify, verify_all

from approvaltests.reporters.python_native_reporter import PythonNativeReporter
from approvaltests import Options, verify_as_json
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from approvaltests import set_default_reporter
from approvaltests.storyboard import Storyboard

class GameOfLife:
    def __init__(self):
        self.alive_cells = set()
    
    def __str__(self) -> str:
        height = self.get_max_y() + 1
        width = self.get_max_x() + 1
        return "\n".join(["".join(["*" if self.is_alive(x, y) else " " for x in range(width)]) for y in range(height)])
    
    def get_max_x(self):
        return max([cell[0] for cell in self.alive_cells], default=0)
    
    def get_max_y(self):
        return max([cell[1] for cell in self.alive_cells], default=0)

    def set_alive(self, x, y):
        self.alive_cells.add((x, y))

    def is_alive(self, x, y):
        return (x, y) in self.alive_cells

    def get_age(self, x, y):
        return 0

    def advance(self):
        new_alive_cells = set()
        neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1),
                            ( 0, -1),          ( 0, 1),
                            ( 1, -1), ( 1, 0), ( 1, 1)]

        potential_cells = {neighbor for cell in self.alive_cells for neighbor in 
                           [(cell[0] + dx, cell[1] + dy) for dx, dy in neighbor_offsets]}

        for cell in potential_cells:
            alive_neighbors = sum((neighbor in self.alive_cells) for neighbor in 
                                  [(cell[0] + dx, cell[1] + dy) for dx, dy in neighbor_offsets])

            if alive_neighbors == 3 or (alive_neighbors == 2 and cell in self.alive_cells):
                new_alive_cells.add(cell)

        self.alive_cells = new_alive_cells


def create_glider_at(game,x,y):
    game.set_alive(x+0,y+1)
    game.set_alive(x+1,y+2)
    game.set_alive(x+2,y+0)
    game.set_alive(x+2,y+1)
    game.set_alive(x+2,y+2)

def verify_story_board(game,steps):
    storyboard = Storyboard()
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
    game.set_alive(0, 0)
    game.set_alive(0, 1)
    game.set_alive(1, 0)
    game.set_alive(1, 1)
    assert game.get_age(3,3) == 0
    assert game.get_age(0,0) == 1
    game.advance()
    assert game.get_age(0,0) == 2