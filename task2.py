import numpy as np
import random
import tkinter as tk
from tkinter import messagebox

# Constants
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

# Initialize the board
board = np.array([[EMPTY, EMPTY, EMPTY],
                  [EMPTY, EMPTY, EMPTY],
                  [EMPTY, EMPTY, EMPTY]])

# Function to check if a player has won
def check_winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in board.T:
        if all(cell == player for cell in col):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full (draw)
def is_board_full():
    return all(cell != EMPTY for row in board for cell in row)

# Function for the computer's move (using a simple AI)
def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
    return random.choice(empty_cells)

# Function to update the GUI and handle player's move
def handle_player_move(row, col):
    if board[row][col] == EMPTY:
        board[row][col] = PLAYER_X
        buttons[row][col].configure(text=PLAYER_X)
        if check_winner(PLAYER_X):
            messagebox.showinfo("Winner", "You win!")
            reset_board()
        elif is_board_full():
            messagebox.showinfo("Tie", "It's a draw!")
            reset_board()
        else:
            computer_turn()

# Function to handle computer's move
def computer_turn():
    if not is_board_full():
        row, col = computer_move()
        board[row][col] = PLAYER_O
        buttons[row][col].configure(text=PLAYER_O)
        if check_winner(PLAYER_O):
            messagebox.showinfo("Winner", "Computer wins!")
            reset_board()
        elif is_board_full():
            messagebox.showinfo("Tie", "It's a draw!")
            reset_board()

# Function to reset the game board
def reset_board():
    global board
    board = np.array([[EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY]])
    for row in range(3):
        for col in range(3):
            buttons[row][col].configure(text=EMPTY)

# Create the GUI window
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [[None, None, None], [None, None, None], [None, None, None]]

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=EMPTY, font=("Helvetica", 20),
                                      height=2, width=5, command=lambda r=row, c=col: handle_player_move(r, c))
        buttons[row][col].grid(row=row, column=col)

# Start the game loop
root.mainloop()
