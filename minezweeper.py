#MINEZWEEPER: A Python program


#import
import tkinter
import random

#variableSet
gameOver = False
score = 0
squaresToClear = 0


#define=Window
def play_minezweeper(): #Creates 
    create_mine(mine)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()

mine = []

#define=MineCreation
def create_mine(mine):
    global squaresToClear

    for row in range(0,10):
        rowList = []
        for column in range(0,10):
            if random.randint(1,100) <20:
                rowList.append(1)
            else:
                rowList.append(0)
                squaresToClear = squaresToClear + 1
        mine.append(rowList)
        

def printfield(minee):
    for rowList in mine:
        print(rowList)


def layout_window(window):
    for rowNumber, rowList in enumerate(mine):
        for columnNumber, columnEntry in enumerate(rowList):
            if random.randint(1,100) < 25:
                square = tkinter.Label(window, text = "    ", bg= "darkgreen")
            elif random.randint(1,100) > 75:
                square = tkinter.Label(window, text = "    ", bg= "seagreen")
            else:
                square = tkinter.Label(window, text = "    ", bg= "green")
            square.grid(row = rowNumber, column = columnNumber)
            square.bind("<Button-1>", on_click)


def on_click(event):
    global score
    global gameOver
    global squaresToClear
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currentText = square.cget("text")
    if gameOver == False:
        if mine[row][column] ==1:
            gameOver = True
            square.config(bg = "red")
            print("Game Over! You hit a bomb!")
            print("Your score was: ", score)
        elif currentText == "    ":
            square.config(bg = "saddlebrown")
            totalBombs = 0
 
            if row < 9:
                if mine[row+1][column] == 1:
                    totalBombs = totalBombs + 1
            
            if row > 0:
                if mine[row-1][column] ==1:
                    totalBombs = totalBombs + 1
            
            if column > 0:
                if mine[row][column-1] == 1:
                    totalBombs = totalBombs + 1
             
            if column < 9:
                if mine[row][column+1] == 1:
                    totalBombs = totalBombs + 1
             
            if row > 0 and column > 0:
                if mine[row-1][column-1] ==1:
                    totalBombs = totalBombs +1
             
            if row < 9 and column > 0:
                if mine[row+1][column-1] ==1:
                    totalBombs = totalBombs + 1
              
            if row > 0 and column < 9:
                if mine[row-1][column+1] == 1:
                    totalBombs = totalBombs + 1
            
            if row < 9 and column < 9:
                if mine[row+1][column+1] == 1:
                    totalBombs = totalBombs + 1


            square.config(text = " " + str(totalBombs) + " ")
            squaresToClear = squaresToClear -1
            score = score +1
            if squaresToClear ==0:
                gameOver = True
                print("Well done! You found all the safe squares!")
                print("Your score was:", score)


play_minezweeper()