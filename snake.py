'''
Author: Abdullah A. Alnajim
Email:  aalnajim1@hotmail.com

..: Snake Game :..
move the snake to eat the food and avoid any collisions
use the arrow keys to control the snake
eating the food will increase the snake's length
collision with the walls or itself will end the game

..: Requirements :..
- Python 3.x
- tkinter library

..: How to Run :..
python3 snake_game.py
'''

import tkinter as tk
from tkinter import messagebox
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.resizable(False, False)
        
        # Game constants
        self.CELL_SIZE = 20
        self.GRID_WIDTH = 30
        self.GRID_HEIGHT = 30
        self.GAME_SPEED = 100
        
        # Initialize game state
        self.snake = [(12, 12), (11, 12), (10, 12)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        
        # Create game canvas
        self.canvas = tk.Canvas(master, 
                               width=self.GRID_WIDTH*self.CELL_SIZE,
                               height=self.GRID_HEIGHT*self.CELL_SIZE)
        self.canvas.pack()
        
        # Score display
        self.score_label = tk.Label(master, text=f"Score: {self.score}", font=('Arial', 14))
        self.score_label.pack()
        
        # Bind arrow keys
        self.master.bind('<Key>', self.change_direction)
        
        # Start game loop
        self.update()

    def create_food(self):
        while True:
            x = random.randint(0, self.GRID_WIDTH-1)
            y = random.randint(0, self.GRID_HEIGHT-1)
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        key = event.keysym
        if (key == "Up" and self.direction != "Down" or
            key == "Down" and self.direction != "Up" or
            key == "Left" and self.direction != "Right" or
            key == "Right" and self.direction != "Left"):
            self.direction = key

    def update(self):
        # Move snake
        head_x, head_y = self.snake[0]
        
        if self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        else:  # Right
            new_head = (head_x + 1, head_y)
        
        # Check collisions
        if (new_head in self.snake or
            new_head[0] < 0 or new_head[0] >= self.GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= self.GRID_HEIGHT):
            self.game_over()
            return
        
        self.snake.insert(0, new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.create_food()
        else:
            self.snake.pop()
        
        # Redraw game
        self.canvas.delete("all")
        
        # Draw snake
        for x, y in self.snake:
            self.canvas.create_rectangle(
                x * self.CELL_SIZE, y * self.CELL_SIZE,
                (x+1) * self.CELL_SIZE, (y+1) * self.CELL_SIZE,
                fill="green", outline="black"
            )
        
        # Draw food
        x, y = self.food
        self.canvas.create_oval(
            x * self.CELL_SIZE, y * self.CELL_SIZE,
            (x+1) * self.CELL_SIZE, (y+1) * self.CELL_SIZE,
            fill="red", outline="black"
        )
        
        self.master.after(self.GAME_SPEED, self.update)

    def game_over(self):
        messagebox.showinfo("Game Over", f"Final Score: {self.score}")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()