# Import the necessary modules
import table  # Module for displaying the tic-tac-toe board
import Functions  # Module for game functions
import random  # Module for generating random moves

# Create an empty list to represent the tic-tac-toe board
XOX = [None] * 9

# Main game loop
while True:
    playerKey = " "

    # Reset the game board
    Functions.reKey(XOX)

    # Display the empty tic-tac-toe board
    table.printTable(XOX)

    # Allow the player to choose their side (X or O)
    playerKey = Functions.side()

    # Randomly decide who makes the first move
    move = random.choice([True, False])

    # Game loop to continue until the game finishes
    while Functions.gameFinishControl(XOX):
        move = Functions.moveMaker(move, XOX, playerKey)  # Player and computer make moves
        table.printTable(XOX)  # Display the updated board
        Functions.gameFinishControl(XOX)

    # Determine the game result and print a message
    if move == True:
        print("Computer WİN.")
    else:
        print("CONGRATULATİONS, you win.")

    # Ask the player if they want to continue playing or quit
    ch = input("QUİT(Q) Continue(C)")
    if ch == "Q" or ch == "q":
        break  # Exit the game loop if the player chooses to quit
