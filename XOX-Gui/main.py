from tkinter import *
from tkinter import messagebox

# Create a list to represent the game board.
XOX = [' '] * 9
# Variable to keep track of whose turn it is.
player = 'X'
# Flag to determine if the game is over.
gameOver = False

# Function to handle the click event on a cell of the game board.
def click(r):
    global XOX
    global player

    # If the clicked cell is empty and the game is not over, proceed.
    if XOX[r] == " " and not gameOver:
        # Place the player's symbol in the selected cell.
        XOX[r] = player
        b[r].configure(text=player)
        # Switch the turn to the other player.
        if player == 'O':
            player = 'X'
        else:
            player = 'O'

        # Check if the game is over.
        game_check(XOX)
        if gameOver:
            window.destroy()

        # Check if the board is full and it's not a tie.
        gc = False
        for a in range(9):
            if XOX[a] == " ":
                gc = True
                break
        if not gc and not gameOver:
            messagebox.showinfo("Game Over", "It's a Draw!")
            window.destroy()

# Function to check for a winner in the game.
def game_check(XOX):
    global gameOver
    if (XOX[0] == XOX[1] and XOX[1] == XOX[2] and XOX[0] != " " or
            XOX[3] == XOX[4] and XOX[4] == XOX[5] and XOX[3] != " " or
            XOX[6] == XOX[7] and XOX[7] == XOX[8] and XOX[6] != " " or
            XOX[0] == XOX[3] and XOX[3] == XOX[6] and XOX[0] != " " or
            XOX[1] == XOX[4] and XOX[4] == XOX[7] and XOX[1] != " " or
            XOX[2] == XOX[5] and XOX[5] == XOX[8] and XOX[2] != " " or
            XOX[0] == XOX[4] and XOX[4] == XOX[8] and XOX[0] != " " or
            XOX[2] == XOX[4] and XOX[4] == XOX[6] and XOX[2] != " "):
        gameOver = True
        # Display a message indicating the winner and that the game is over.
        if player == 'O':
            messagebox.showinfo("Game Over", "Player 1 Wins!")
        else:
            messagebox.showinfo("Game Over", "Player 2 Wins!")

# Create a Tkinter window.
window = Tk()
window.title("Tic Tac Toe")
b = [None] * 9

# Create and layout buttons for the game board.
for i in range(9):
    b[i] = Button(window, height=8, width=12, text=" ", font="Times", fg="#73FF9A", bg="grey", command=lambda r=i: click(r))
    b[i].grid(row=int(i/3), column=(i%3))

# Start the main loop.
mainloop()
