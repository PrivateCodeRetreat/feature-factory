import os

from approvaltests.approvals import verify

from approvaltests.storyboard import Storyboard

from project.game_of_life import GameOfLife

# If this fails, run:
# brew install python-tk

def is_running_on_github_actions():
    return os.getenv('CI') == 'true'
def test_tkinter_gui():
    if is_running_on_github_actions():
        return
    from project.TkinterGui import TkinterGui
    game = GameOfLife()
    create_square_at(game, 8, 8)
    create_glider_at(game, 0, 0)
    gui = TkinterGui(game)
    gui.show(22)

def create_blinker_at(game,x,y):
    game.set_alive(x+0,y+1)
    game.set_alive(x+1,y+1)
    game.set_alive(x+2,y+1)

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

def create_applesauce_at(game,x,y):
    create_square_at(game,x,y)
    create_square_at(game,x+3,y)
    create_square_at(game,x,y+3)
    create_square_at(game,x+3,y+3)

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
    verify_story_board(game,5)

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