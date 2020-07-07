# Name = Monish Manjunath
# Date = 03/08/2020
# Honor statement = I have not given or received any unauthorized assistance on this assignment.
# Video link Url = "https://youtu.be/AdcfdKe4cKw "


import numpy as np
import random

def conway(size,prob):
    """ Creating a conway board for the size and probabilty value given by the user """
    initialarray = np.zeros((size,size))                        # Creatinng a two dimensional array of inputted size
    for i in range(size):
        for j in range(size):
            if random.random() < prob:                          # Randomly entering values depedning on the probability 
                initialarray[i,j] = 1
    return initialarray


def advance(board, t):
    """ This function checks the rules of conway rules of life and prints the board """
    for i in range(t):
        arr = np.zeros(board.shape)                             # Creating new board for every iteration
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                alive = numOfAlive(board, i, j)                 # Calling a function and checking if the neighboring cells are alive or dead
                if returnExactPosition(board, i, j) == 1:       # Checks if the cell is marked as 1 or alive
                    if alive < 2:                               # Live cell with less than 2 live neighbors
                        arr[i,j] = 0
                    elif alive == 2 or alive == 3:              # Live cell with two or 3 live neighbors
                        arr[i,j] = 1
                    elif alive >=3:                             # Live cell with more than 3 live neighbors
                        arr[i,j]=0
                else:
                    if alive == 3:                              # Checks if the dead cell has more than 3 live neighbors 
                        arr[i,j]= 1
                    else:
                        arr[i,j]=0
        board = arr
    return board


def numOfAlive(board, a, b):
    """  This function checks if the neigboring cells are alive or dead """
    alive = 0
    for i in range(-1, 2):                                      # Checking left of cells
        for j in range(-1,2):                                   # Checking right of the cells
            alive += returnExactPosition(board, a + i, b + j)   # Incrementing the count based on the live cells
    alive -= returnExactPosition(board, a, b)
    return alive    


def returnExactPosition(board, x, y):
    """ This function unpacks the accurate location of the cells in the n dimensional array   """
    highX, highY = board.shape
    x = x % highX
    y = y % highY
    return board[x,y]








def main():
    """ Main function of the program accepts users values and makes appropriate function calls """

    sizeofboard = int(input("Enter the size of the board: "))
    probability = float(input("Enter a value for probability between 0.0 to 0.1: "))
    board = conway(sizeofboard, probability)                                # Calling the conway function
                   

    numOfIterations = int(input("Enter the number of iterations to run: "))
    numOfSteps = int(input("Enter the number of steps per iteration: "))
    for i in range(numOfIterations):
        board = advance(board, numOfSteps)                                  # Calling the advance function 
        print(board)
        

main()