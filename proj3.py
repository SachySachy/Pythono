# File:        proj3.py
# Author:      Sachin Saigal
# Date:        12/4/17
# Section:     20
# E-mail:      saigal1@umbc.edu
# Description: this program was created to solve mazes

TOP = 3
LEFT = 2
BOTTOM = 1
RIGHT = 0

# this function reads and finds the end of the maze the finish line
def findEnd(mazeRead):
    endRead = mazeRead[1].strip()
    end = endRead.split(" ")
    return end
# this function reads how big the board will be
def findSize(mazeRead):
    sizeRead = mazeRead[0].strip()
    size = sizeRead.split(" ")
    return size

# this function creates the board and takes in mazeRead a varible with the read txt file 
# it also takes in lower and upper for columns
def createboard(mazeRead,lower,upper):
    # maze1 is the 3d List
    maze1 = []
    rowIndex = 0
    # sizeRead read out the size of the board
    sizeRead = mazeRead[0].strip()
    size = sizeRead.split(" ")
    print(size)
    #then it prints the board
    maxWidth1 = size[1]
    maxHeight = size[0]
    
    upper = upper + int(maxWidth1)
    # this while loops creates the iterates through the file down the size of the columns and then lower and upper is increased my columns so it can propertly go down the list
    while(rowIndex < int(maxHeight)):
        row = []
        while(lower < upper):
            line = mazeRead[lower].strip()
            square = line.split(" ")
            lower= lower+1
            row.append(square)
        upper = upper + int(maxWidth1)
        maze1.append(row)
        rowIndex = rowIndex + 1
    return maze1
    #Read the file for maze and then returns mazeRead
def readFile(choiceMaze):
    maze = open(choiceMaze)
    mazeRead = maze.readlines()
    maze.close()
    return mazeRead
                           # this function first has takes in the maze, pastLoactions and current row and square(column), and what the final destination is
def searchMaze(mazeBoard , pastLocations, row , square, rowFinal , columnFinal):
    #Base case
    if(row == rowFinal and square == columnFinal):
        return 1
    if(int(mazeBoard[row][square][TOP]) == 1 and int(mazeBoard[row][square][BOTTOM]) == 1 and int(mazeBoard[row][square][RIGHT]) == 1 and int(mazeBoard[row][square][LEFT] == 1)):
        return 0

                           #print current location
   # print(mazeBoard[row][square][RIGHT],mazeBoard[row][square][BOTTOM],mazeBoard[row][square][LEFT],mazeBoard[row][square][TOP])
    

# Arguments

    #If the the right side of the circle is open then it will check if it has been there and if it has it skips the whole argument and check the next postion
    if(int(mazeBoard[row][square][RIGHT]) == 0):
        x= 0
        dog = False
        print("Right")
        #this checks the past locations ( dog is the name of the varible that hold the true and false logic statement if dog = = true then the we where at that we cam from that location
        x = len(pastLocations)-1
        if(pastLocations[x] == [row , square] ):
            dog = True
            
        if(dog == False):
            pastLocations.append([row ,square])
            print("[",row ,  square,"]")
            searchMaze(mazeBoard , pastLocations, row , square +1, rowFinal, columnFinal)
    
    if(int(mazeBoard[row][square][LEFT]) == 0):
        x = 0
        dog = False
        print("Left")
        x = len(pastLocations)-1
        if(pastLocations[x] == [row, square]):
            dog = True
        
        if(dog == False):
            pastLocations.append([row ,square])
            print("[",row , square,"]")
            #searchMaze(mazeBoard ,pastLocations, row, square -1, rowFinal, columnFinal)
    
    if(int(mazeBoard[row][square][TOP]) == 0):
        x = 0
        dog = False
        print("Top")
        x= len(pastLocations)
        if(pastLocations[x] == [row , square]):
            dog = True
            
        if(dog == False):
            pastLocations.append([row][square])
            print("[",row ,  square,"]")
            #searchMaze(mazeBoard ,pastLocations, row -1 , square)
    if(int(mazeBoard[row][square][BOTTOM]) == 0):
        x =0
        dog = False
        print("Bottom")
        x = len(pastLocations)-1
        if(pastLocations[x] == [row, square]):
            dog = True
            
        if(dog == False):
            pastLocations.append([row , square])
            print("[",row ,  square,"]")
            #searchMaze(mazeBoard ,pastLocations, row +1, square, rowFinal, columnFinal) 
    

# function main
def main():
    # user input on which maze
    choiceMaze = input("Please enter the name of the maze you would like to use: ")
    mazeRead = readFile(choiceMaze)
    #creates the board
    mazeBoard = createboard(mazeRead,2,2)
    print(mazeBoard)
    pastLocations = [-3,-3]
    # calls findSize
    size = findSize(mazeRead)
    length = size[1]
    width = size[0]

    row = int(input("Please enter the row "))
    column = int(input("Please enter the column "))
    #findEnd
    print(mazeBoard[row][column][TOP])
    end = findEnd(mazeRead) 
    rowFinal = end[0]
    columnFinal = end[1]
    # calls searchMaze
    solution = searchMaze(mazeBoard , pastLocations, row, column , int(rowFinal), int(columnFinal))
    if (solution == 0):
        print("No solution found!")
    if (solution == 1):
        print("solved")



main()
