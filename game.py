import os
import random
import numpy as np
import numba
from numba import jit

#@profile
def PlaceTile(board):
    b = np.argwhere(board==0)
    placey,placex = b[random.randrange(0, b.shape[0])]
    board[placey][placex] = 1 if random.random() < 0.9 else 2

def CreateBoard():
    board = np.zeros((4,4),dtype=np.uint16)
    PlaceTile(board)
    PlaceTile(board)
    return board

def PrintBoard(board):
    text = "-" * 29 + "\n"
    for r in range(4):
        for c in range(4):
            text += "|{0: <6}".format("" if board[r][c] == 0 else 2**board[r][c])
        text += "|\n" + "-" * 29 + "\n"
    os.system("cls")
    print(text)

"""
Move:
0: left
1: up
2: right
3: down
"""
# Can be optimized by removing rotation, will likely have to
@jit(nopython=True, cache=True)
def ShiftBoard(board=np.array([[]]), move=0):
    board = np.rot90(board, move)  # Temporarily rotate board depending on move direction
    newboard = np.zeros((4, 4), dtype=np.uint16)
    for r in range(4): # Loop each row of board
        shiftline = board[r][np.nonzero(board[r])]  # Compress row 
        if shiftline.size == 0: continue
        for i in range(shiftline.size - 1): # Check for combinations
            if shiftline[i] == shiftline[i+1]:
                shiftline[i] += 1
                shiftline[i+1] = 0
        shiftline = shiftline[np.nonzero(shiftline)]  # Re compress row after potential combinations
        newboard[r][:shiftline.size] = shiftline

    newboard = np.rot90(newboard, -move) # Rotate board back
    return newboard
    """
    if np.array_equal(board, newboard):
        return False
    else:
        board = newboard
        return True
    """

#@profile
def MoveBoard(board, move):
    nb = ShiftBoard(board, move)
    if not np.array_equal(nb, board):
        PlaceTile(nb)
        return nb
    else:
        return board

def GameOver(board):
    for i in range(4):
        new_board = ShiftBoard(board, i)  # Calculate move
        if not np.array_equal(new_board, board): # Move is valid
            return False
    return True