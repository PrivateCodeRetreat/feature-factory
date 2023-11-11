import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

# Create canvas
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

# Initial snake and food parameters
snake = [(20, 20), (20, 30), (20, 40)]
snake_speed = 10
snake_direction = "right"
food = (50, 50)

# Function to draw snake and food
def draw_elements():
    canvas.delete("all")
    for segment in snake:
        canvas.create_rectangle(segment[0], segment[1], segment[0]+10, segment[1]+10, fill="green")
    canvas.create_rectangle(food[0], food[1], food[0]+10, food[1]+10, fill="red")

# Function to move the snake
def move_snake():
    global snake, food
    x, y = snake[0]
    if snake_direction == "up":
        y -= 10
    elif snake_direction == "down":
        y += 10
    elif snake_direction == "left":
        x -= 10
    elif snake_direction == "right":
        x += 10
    new_head = (x, y)

    # Collision with food
    if new_head == food:
        snake = [new_head] + snake
        food = generate_food()
    else:
        snake = [new_head] + snake[:-1]

    # Collision with walls or itself
    if x < 0 or x >= 400 or y < 0 or y >= 400 or new_head in snake[1:]:
        game_over()
        return

    draw_elements()
    root.after(100, move_snake)

# Change snake direction
def change_direction(new_direction):
    global snake_direction
    if new_direction in ["left", "right"] and not snake_direction in ["left", "right"]:
        snake_direction = new_direction
    elif new_direction in ["up", "down"] and not snake_direction in ["up", "down"]:
        snake_direction = new_direction

# Generate new food
def generate_food():
    while True:
        new_food = (random.randint(0, 39) * 10, random.randint(0, 39) * 10)
        if new_food not in snake:
            return new_food

# Game over
def game_over():
    canvas.create_text(200, 200, text="Game Over", fill="white", font=("Arial", 24))

# Key bindings
root.bind("<Left>", lambda event: change_direction("left"))
root.bind("<Right>", lambda event: change_direction("right"))
root.bind("<Up>", lambda event: change_direction("up"))
root.bind("<Down>", lambda event: change_direction("down"))

# Start game
food = generate_food()
draw_elements()
move_snake()

root.mainloop()
