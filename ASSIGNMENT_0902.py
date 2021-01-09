# Name : Vismay Bhavinkumar Patel 
# Date : 08/15/20
# Honour Statement: “I have not given or received any unauthorized assistance on this assignment.”
# Youtube Link : https://youtu.be/V52ODmbIkuo

# Python programme to ceate game of life.

import numpy as np

# get user input
s = int(input('Enter size of 2D array: '))
p = float(input("Enter the proportion: "))
t = int(input("Enter the time of generation "))

def conway(s, p):

    """
    This function takes the values of 2D array/matrix s and the probility p.
    Then generates the random numbers or size to populate the board.
    """
  
    array2D = np.random.random((s, s))              # Randomly generates the 2 dimensional array with side s.
    board = array2D + p                             # This generates the board which is filled with probability. 
    return board.astype(int)                        # return type of the board with zeros and ones will be int.

b = conway(s, p)                                    # create a board to call the board.      


def rules(cell, live_n):

    """
    This function assigns the rules of game of life. 
    The criteria of whether a cell will remain alive or dead based on the rules.
    """
    
    if cell == 0:                                   # If condition, when the cell is equal to 0.

        if live_n == 3:                             # If condition when there are three cells alive. 
            return 1                                # If three cells are alive then the cell survives/lives.

        else:                                       # If condition if are no live neighburing cells.
            return 0                                # The cell dies, if there are no live neighbouring cells.

    else:                                           # When the value of cell is  1.

        if live_n < 2 or live_n > 3:                # If condition when there are less than 2 live neighbors or more than 3 live neighbors.
            return 0                                # The cell dies due to over population.
        
        else:                                       # else, if there are 2 live neighbors or 3 live neighbors
            return 1                                # The cell survives


def neighbors(b, i, j):

    """
    The function takes three parameters, namely b = board, i = rows and j = columns.
    This function represents the logic for calculation/evaluation of the neighbours.
    And returns the sum of neighbouring values.
    """
 
    s = len(b[0])                                   # length of board initially at 0 index.
    
    left, right = max(0, i-1), min(s+1, i+2)        # left, right side calculations.
    
    up, down = max(0, j-1), min(s+1, j+2)           # top, bottom side calculations.  
    
    num = b[left:right, up:down]                    # here we consider both left, right and top and bottom elements on the board.

    if b[i,j] == 1:                                 # If the cell value on the board is 1.

        return np.sum(num) - 1                      # Then the sum of the number is substracted by one.

    else:

        return np.sum(num)                          # other wise the pattern is returned.


def updated_board():

    """
    This function generates a new board, based on the rules of game of life.
    Here the global variable b(board) is declared that is later set as new board.
    """
    
    global b

    s = len(b[0])                                               # Side of the board.   
    
    new_board = conway(s, 0)                                    # New board parameters.
    
    N = len(b[0])                                               # length of the board.

    for i in range(N):                                          # for row in length of board.

        for j in range(N):                                      # for column in length of board.

            new_board[i,j] = rules(b[i,j], neighbors(b,i,j))    # Displaying the new board based on the rules and neighbours by calling them.
                                                                # in new_board function.

    b = new_board                                               # set board as new board.



def advance(t):

    """
    This function takes t time steps based on the rules advance the board or update the exhisting board.
    Then prints the final result.
    """

    global b

    print('\nGeneration Zero/Original Board:')
    
    for i in b:                                         # loop that prints the current board values.
        print(i)
    
    for i in range(t):                                  # loop that takes time t to perform operation.
        print(updated_board())

    print('\nGeneration One/Updated Board:')
    
    for i in b:                                         # loop that prints the updated board.
        print(i)


advance(t)
