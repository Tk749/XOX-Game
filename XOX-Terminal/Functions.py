import random

# Function to reset the game board by filling it with empty spaces
def reKey(XOX):
    for x in range(9):
        XOX[x] = " "

# Function for the player's move
def playerMove(XOX, playerKey):
    print("Player turn")
    while True:
        try:
            val = int(input("Please enter an integer from 1 to 9: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            if 0 > val or val > 9:
                continue
            elif XOX[val - 1] == " ":
                XOX[val - 1] = playerKey
                break
            print("This location is occupied.")
            continue

# Function for the computer's move
def computerMove(XOX, playerKey):
    print("Computer turn")
    while True:
        value = random.randint(1, 9) - 1
        if XOX[value] == " ":
            if playerKey == "X" or playerKey == "x":
                XOX[value] = "O"
            else:
                XOX[value] = "X"
            break

# Function to allow the player to choose their side (X or Y)
def side():
    while True:
        tempKey = input('Please select X or Y  ')
        if tempKey == "X" or tempKey == "Y" or tempKey == "x" or tempKey == "y":
            if tempKey == "x":
                tempKey = "X"
            elif tempKey == "y":
                tempKey = "Y"
            return tempKey

# Function to manage each player's move
def moveMaker(move, XOX, playerKey):
    if move == True:
        print("")
        playerMove(XOX, playerKey)
    else:
        computerMove(XOX, playerKey)

    return (not move)

# Function to check if the game has finished (win, lose, or draw)
def gameFinishControl(XOX):
    if (XOX[0] == XOX[1] and XOX[1] == XOX[2] and XOX[0] != " " or
        XOX[3] == XOX[4] and XOX[4] == XOX[5] and XOX[3] != " " or
        XOX[6] == XOX[7] and XOX[7] == XOX[8] and XOX[6] != " " or
        XOX[0] == XOX[3] and XOX[3] == XOX[6] and XOX[0] != " " or
        XOX[1] == XOX[4] and XOX[4] == XOX[7] and XOX[1] != " " or
        XOX[2] == XOX[5] and XOX[5] == XOX[8] and XOX[2] != " " or
        XOX[0] == XOX[4] and XOX[4] == XOX[8] and XOX[0] != " " or
        XOX[2] == XOX[4] and XOX[4] == XOX[6] and XOX[2] != " "):
        return False
    else:
        return  True
