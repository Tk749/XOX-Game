from tkinter import *
from tkinter import messagebox

XOX = [' ']*9
player = 'X'
gameOver = False

def click(r):
    global XOX
    global player

    if XOX[r] == " " and gameOver == False:
        XOX[r] = player
        b[r].configure(text = player)
        if player == 'O':
            player = 'X'
        elif player == 'X':
            player = 'O'


    game_check(XOX)
    if gameOver == True:
        window.destroy()


    gc = False
    for a in range(9):
        if XOX[a] == " ":
            gc = True
            break
    if gc == False and gameOver == False:
        messagebox.showinfo("GAME OVER", "?????")
        window.destroy()

def game_check(XOX):
    global  gameOver
    if (XOX[0] == XOX[1] and XOX[1] == XOX[2] and XOX[0] != " " or
            XOX[3] == XOX[4] and XOX[4] == XOX[5] and XOX[3] != " " or
            XOX[6] == XOX[7] and XOX[7] == XOX[8] and XOX[6] != " " or
            XOX[0] == XOX[3] and XOX[3] == XOX[6] and XOX[0] != " " or
            XOX[1] == XOX[4] and XOX[4] == XOX[7] and XOX[1] != " " or
            XOX[2] == XOX[5] and XOX[5] == XOX[8] and XOX[2] != " " or
            XOX[0] == XOX[4] and XOX[4] == XOX[8] and XOX[0] != " " or
            XOX[2] == XOX[4] and XOX[4] == XOX[6] and XOX[2] != " "):
        gameOver = True
        if player == 'O':
            messagebox.showinfo("GAME OVER","PLAYER1 WON")
        else:
            messagebox.showinfo("GAME OVER","PLAYER2 WON")

window = Tk()
window.title("XOX")
b = [None]*9

for i in range(9):
    b[i] = Button(window, height=8, width=12
                  , text=(" ")
                  , font="Times", fg="#73FF9A", bg="grey"
                  , command=lambda r = i: click(r))
    b[i].grid(row = int(i/3) , column = (i%3))

mainloop()