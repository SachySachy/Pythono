# File:      proj2.py
# Author:    Sachin Saigal
# Date:      11/6/17
# Section:   20
# Email:     saigal1@umbc.edu
# Description: Create the game of life






#CreatesBoard using already given height and width    
def createBoard(height, width):
    gameBoard = []
    while len(gameBoard) < height:
        boardRow = []
        while len(boardRow) < width:
            boardRow.append(".")
        gameBoard.append(boardRow)
    return gameBoard


#Gets valid Input
def getValidInput(prompt, minimum):
    print(prompt)
    number = int(input())
    while ( number < minimum ):
        number = int(input("Invalid input"))
        print(prompt)
    return number

#Takes in gameBoard Row and Cols to create a print form gameboard and rows and columns
def printBoard(gameBoard, Rows, Cols):
    rowCount = 0
    while rowCount < Rows:
        colCount = 0
        while colCount < Cols:
            print(gameBoard[rowCount][colCount], end=" ")
            colCount +=1
        print()
        rowCount+=1
#changes gameboard in by adding Alive 
def createAlive(gameBoard, Rows, Cols):
    rowAlive = input("Please enter the row of a cell to turn on ( or q to exit): ")
    while( rowAlive != 'q' ):
        rowAlive = int(rowAlive)
        while ( rowAlive < 0 or rowAlive > Rows-1 ):
            print("That is not a Valid value, please enter a number between, 0 and ", Rows-1)
            rowAlive = int(input("Please enter the row of a cell to turn on: "))
        colAlive = int(input("Please enter the col of a cell to turn on: "))
        
        while ( rowAlive < 0 or colAlive > Cols-1 ):
            print("That is not a Valid value, please enter a number between, 0 and ", Cols-1)
            colAlive = int(input("Please enter the col of a cell to turn on: "))
        gameBoard[rowAlive][colAlive] = "A"

        rowAlive = input("Please enter the row of a cell to turn on ( or q to exit): ")










def checkNeib(gameBoard, Rows, Cols):
    # in this really long function, is where all the action happens in this code
    # this function create New alive cells and also neighborhood, i was having trouble with deep copies of the
    #gameboard and later check would green light previous changes to new list as the orginial list, to get around
    # this i made all new changes alives to N and i changed them back before return, 
    # 1 its easier to see and 2 it was an easy work around, PS sorry for the long code, Comments continue for the
    # rest of the function

    newGameBoard = []
    index = 0
    while(index < len(gameBoard)):    
        newGameBoard.append(gameBoard[index])
        index+=1


    

    newGameBoard = list(gameBoard)
    rowCount = 1
    aliveCount = 0
    #this part of the function check the inside of the gameboard for neighbors and creates new alive
    while rowCount < Rows-1:
        colCount = 1
        while colCount < Cols-1:
            aliveCount = 0
            if(gameBoard[rowCount][colCount] == '.'):
                if(gameBoard[rowCount-1][colCount-1] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount-1][colCount] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount-1][colCount+1] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount][colCount-1] == 'A'):    
                    aliveCount+=1
                if(gameBoard[rowCount][colCount+1] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount+1][colCount-1] == 'A'):  
                    aliveCount+=1
                if(gameBoard[rowCount+1][colCount] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount+1][colCount+1] == 'A'):    
                    aliveCount+=1
                if(aliveCount == 3):
                    newGameBoard[rowCount][colCount] = 'A'
            colCount+=1
        rowCount+=1
    
    




#Check and creates new alive for sides of gameboard nut not the edges and also uses N for new alive
    #top edge
    aliveCount = 0
    colCount = 1
    while (colCount < Cols-1):
        aliveCount = 0
        if(gameBoard[0][colCount] == '.'):
            if(gameBoard[0][colCount-1] == 'A'):
                aliveCount+=1
            if(gameBoard[0][colCount+1] == 'A'):
                aliveCount+=1
            if(gameBoard[1][colCount-1] == 'A'):
                aliveCount+=1
            if(gameBoard[1][colCount] == 'A'):
                aliveCount+=1
            if(gameBoard[1][colCount+1] == 'A'):
                aliveCount+=1
            if(aliveCount == 3):
                newGameBoard[0][colCount] = 'A'
        colCount+=1
    
    #left edge
    aliveCount = 0
    rowCount = 1
    while (rowCount < Rows-1):
        aliveCount = 0
        if(gameBoard[rowCount][0] == '.'):
            if(gameBoard[rowCount-1][0] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount+1][0] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount-1][1] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount][1] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount+1][1] == 'A'):
                aliveCount +=1
            if(aliveCount ==3):
                newGameBoard[rowCount][0] = 'A'
        rowCount+=1
    
    #right Edge
    aliveCount = 0
    rowCount = 1
    while(rowCount < Rows-1):
        aliveCount = 0
        if(gameBoard[rowCount][Rows-1] == '.'):
            if(gameBoard[rowCount-1][Cols-1] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount+1][Cols-1] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount-1][Cols-2] == 'A'):
                aliveCount+=1
            if(gameBoard[rowCount][Cols-2] == 'A'):
                aliveCount+=1
            if(gameBoard[rowCount+1][Cols-2] == 'A'):
                aliveCount+=1
            if(aliveCount == 3):
                newGameBoard[rowCount][Cols-1] = 'A'
        rowCount+=1
    
    #bottom edge
    aliveCount = 0
    colCount = 1
    while (colCount < Cols-1):
        aliveCount = 0
        if(gameBoard[0][colCount] == '.'):
            if(gameBoard[Rows-1][colCount-1] == 'A'):
                aliveCount+=1
            if(gameBoard[Rows-1][colCount+1] == 'A'):
                aliveCount+=1
            if(gameBoard[Rows-2][colCount-1] == 'A'):
                aliveCount+=1
            if(gameBoard[Rows-2][colCount] == 'A'):
                aliveCount+=1
            if(gameBoard[Rows-2][colCount+1] == 'A'):
                aliveCount+=1
            if(aliveCount == 3):
                newGameBoard[Rows-1][colCount] = 'A'
        colCount+=1


    #check edges, corner piece 
    if(gameBoard[0][0] == '.'):
        aliveCount = 0
        
        if(gameBoard[0][1] == 'A'):
            aliveCount +=1
        if(gameBoard[1][0] == 'A'):
            aliveCount +=1
        if(gameBoard[1][1] == 'A'):
            aliveCount +=1
        if(aliveCount ==3):
            newGameBoard[0][0] = 'A'
    
    if(gameBoard[0][Cols-1] == '.'):
        aliveCount = 0
    
        if(gameBoard[0][Cols-2] == 'A'):
            aliveCount +=1
        if(gameBoard[1][Cols-1] == 'A'):
            aliveCount +=1
        if(gameBoard[1][Cols-2] == 'A'):
            aliveCount +=1
        if(aliveCount == 3):
            newGameBoard[0][Cols-1] = 'A'

    if(gameBoard[Rows-1][Cols-1] == '.'):
        aliveCount = 0

        if(gameBoard[Rows-1][Cols-2] == 'A'):
            aliveCount +=1
        if(gameBoard[Rows-2][Cols-1] == 'A'):
            aliveCount +=1
        if(gameBoard[Rows-2][Cols-2] == 'A'):
            aliveCount +=1
        if(aliveCount == 3):
            newGameBoard[Rows-1][Cols-1] = 'A'
                
    if(gameBoard[Rows-1][0] == '.'):
        aliveCount = 0

        if(gameBoard[Rows-1][1] == 'A'):
            aliveCount +=1
        if(gameBoard[Rows-2][0] == 'A'):
            aliveCount +=1
        if(gameBoard[Rows-2][1] == 'A'):
            aliveCount +=1
        if(aliveCount == 3):
            newGameBoard[Rows-1][0] = 'A'


# Now that all the cases are done its time to check the orginial gameboard and for the NewAlive
    aliveCount = 0
    #this part of the function check the inside of the gameboard for neighbors and creates new alive
    rowCount = 1
    while rowCount < Rows-1:
        colCount = 1
        while colCount < Cols-1:
            aliveCount = 0
            if(gameBoard[rowCount][colCount] == 'A'):
                if(gameBoard[rowCount-1][colCount-1] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount-1][colCount] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount-1][colCount+1] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount][colCount-1] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount][colCount+1] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount+1][colCount-1] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount+1][colCount] == 'A'):
                    aliveCount+=1
                if(gameBoard[rowCount+1][colCount+1] == 'A'):
                     aliveCount+1

                if(aliveCount < 2):
                    newGameBoard[rowCount][colCount] = '.'
                if(aliveCount > 3):
                    newGameBoard[rowCount][colCount] = '.'
            colCount+=1
        rowCount+=1
    #to create dead cells top edge     
    
    aliveCount = 0
    colCount = 1
    while (colCount < Cols-1):
        aliveCount = 0
        if(gameBoard[0][colCount] == 'A'):
            if(gameBoard[0][colCount-1] == 'A'):
                aliveCount+=1
            if(gameBoard[0][colCount+1] == 'A'):
                aliveCount+=1
            if(gameBoard[1][colCount-1] == 'A'):
                aliveCount+=1
            if(gameBoard[1][colCount] == 'A'):
                aliveCount+=1
            if(gameBoard[1][colCount+1] == 'A'):
                aliveCount+=1
            if(aliveCount < 2):
                    newGameBoard[0][colCount] = '.'
            if(aliveCount > 3):
                    newGameBoard[0][colCount] = '.'
        colCount+=1
  



  #to create dead cell left edge
    aliveCount = 0
    rowCount = 1
    while (rowCount < Rows-1):
        aliveCount = 0
        if(gameBoard[rowCount][0] == 'A'):
            if(gameBoard[rowCount-1][0] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount+1][0] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount-1][1] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount][1] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount+1][1] == 'A'):
                aliveCount +=1
            if(aliveCount < 2):
                    newGameBoard[rowCount][0] = '.'
            if(aliveCount > 3):
                    newGameBoard[rowCount][0] = '.'
        rowCount+=1

    #to create dead cell right Edge
    aliveCount = 0
    rowCount = 1
    while(rowCount < Rows-1):
        aliveCount = 0
        if(gameBoard[rowCount][Rows-1] == 'A'):
            if(gameBoard[rowCount-1][Cols-1] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount+1][Cols-1] == 'A'):
                aliveCount +=1
            if(gameBoard[rowCount-1][Cols-2] == 'A'):
                aliveCount+=1
            if(gameBoard[rowCount][Cols-2] == 'A'):
                aliveCount+=1
            if(gameBoard[rowCount+1][Cols-2] == 'A'):
                aliveCount+=1
            if(aliveCount < 2):
                    newGameBoard[rowCount][Cols-1] = '.'
            if(aliveCount > 3):
                    newGameBoard[rowCount][Cols-1] = '.'
        rowCount+=1
    print()
    #to create dead cells bottom edge
    aliveCount = 0
    colCount = 1
    while (colCount < Cols-1):
        aliveCount = 0
        if(gameBoard[Rows-1][colCount] == 'A'):
            if(gameBoard[Rows-1][colCount-1] == 'A'):
                aliveCount+=1
            if(gameBoard[Rows-1][colCount+1] == 'A'):
                aliveCount+=1
            if(gameBoard[Rows-2][colCount-1] == 'A'):
                aliveCount+=1
            if(gameBoard[Rows-2][colCount] == 'A'):
                aliveCount+=1
            if(gameBoard[Rows-2][colCount+1] == 'A'):
                aliveCount+=1
            if(aliveCount < 2):
                    newGameBoard[Rows-1][colCount] = '.'
            if(aliveCount > 3):
                    newGameBoard[Rows-1][colCount] = '.'
        colCount+=1
    return newGameBoard

#re call checkNeib as many times the user wants
def nextIteration(gameboard, Rows, Cols):
    num = getValidInput("How many times do you want to Iterate gameboard?: ", 0)
    numIndex = 0
    while(numIndex < num):
        print()
        print("Iteration number ", numIndex+1)
        gameBoard2= checkNeib(gameboard,Rows ,Cols)
        printBoard(gameBoard2, Rows, Cols)
        numIndex+=1

def main():
    Rows = getValidInput("Please enter how many Rows you would like for the board: ", 0 )
    Cols = getValidInput("Please enter how many Columns you would like for the board: ", 0 )
    gameBoard = createBoard(Rows , Cols)
    printBoard(gameBoard, Rows , Cols)   
    createAlive(gameBoard, Rows, Cols)
    printBoard(gameBoard, Rows , Cols)   
    
    nextIteration(gameBoard, Rows, Cols)
    
    
       
main()

