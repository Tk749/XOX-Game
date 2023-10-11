# Importing necessary packages from tkinter
from tkinter import *
from tkinter import messagebox

# Initializing player 1 as 'X' and a flag to stop the game
Player1 = 'X'
stop_game = False

# Function to handle button click events with row and column arguments
def clicked(r, c):
    global Player1
    # Check if it's player 1's turn and the cell is empty
    if Player1 == "X" and states[r][c] == 0 and not stop_game:
        # Set the button text to 'X' and update the state
        b[r][c].configure(text="X")
        states[r][c] = 'X'
        # Switch to player 2's turn
        Player1 = 'O'
    # Check if it's player 2's turn and the cell is empty
    elif Player1 == 'O' and states[r][c] == 0 and not stop_game:
        # Set the button text to 'O' and update the state
        b[r][c].configure(text='O')
        states[r][c] = "O"
        # Switch to player 1's turn
        Player1 = "X"
    # Check if there's a winner after each move
    check_if_win()

# Function to check if there's a winner
def check_if_win():
    global stop_game

    # Check for horizontal wins
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            stop_game = True
            # Show a message box indicating the winner
            winner = messagebox.showinfo("Winner", states[i][0] + " Won!")
            break

    # Check for vertical wins
    for i in range(3):
        if states[0][i] == states[1][i] == states[2][i] != 0:
            stop_game = True
            winner = messagebox.showinfo("Winner", states[0][i] + " Won!")
            break

    # Check for diagonal wins
    if states[0][0] == states[1][1] == states[2][2] != 0:
        stop_game = True
        winner = messagebox.showinfo("Winner", states[0][0] + " Won!")

    if states[0][2] == states[1][1] == states[2][0] != 0:
        stop_game = True
        winner = messagebox.showinfo("Winner", states[0][2] + " Won!")

    # Check for a tie (if all cells are filled)
    if all(states[i][j] != 0 for i in range(3) for j in range(3)) and not stop_game:
        stop_game = True
        tie = messagebox.showinfo("Tie", "It's a Tie!")

# Design the window
root = Tk()
root.title("Tic Tac Toe")
root.resizable(0, 0)

# Create buttons and states for the game board
b = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

states = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

# Create and configure buttons for the game board
for i in range(3):
    for j in range(3):
        b[i][j] = Button(
            height=4, width=8,
            font=("Helvetica", "20"),
            command=lambda r=i, c=j: clicked(r, c))
        b[i][j].grid(row=i, column=j)

# Start the main loop
mainloop()
