from game import *

count = 0
# Implementation of ExpectiMax algorithm

class Node:
     
    def __init__(self, value):
         
        self.value = value
        self.children = []


# Calculate score of leaf position
# Score algorithm is currently the sum of 3^n for each element n
@jit(nopython=True, cache=True)
def CalculateLeafScore(board):
    return np.sum(3 ** board)    

#@profile
# Evaluate score from a position where it is the computer's turn
#@jit(parallel=True)
def CalculateScore(board, depth, max_depth):
    if (depth >= max_depth):
        return CalculateLeafScore(board)
    
    total_score = 0
    b = np.argwhere(board==0) # Get locations of all empty squares
    
    for x, y in b:  # Loop through empty squares
        new_board2 = board
        new_board2[x][y] = 1
        score2, _ = CalculateMoveScore(new_board2, depth, max_depth)
        total_score += 0.9 * score2

        new_board4 = board
        new_board4[x][y] = 1
        score4, _ = CalculateMoveScore(new_board4, depth, max_depth)
        total_score += 0.1 * score4

    return total_score

#@profile
# Evaluate value of each possible move
#@jit(parallel=True)
def CalculateMoveScore(board, depth, max_depth):

    max_score = 0
    best_move = -1

    # Loop through all the possible moves
    for i in range(4):
        new_board = ShiftBoard(board, i)  # Calculate move
        if not np.array_equal(new_board, board): # Move is valid
            score = CalculateScore(new_board, depth + 1, max_depth)
            if (score > max_score):
                max_score = score
                best_move = i

    return max_score, best_move
