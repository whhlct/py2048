import sys
import time
import numpy as np
from pynput import keyboard # couldnt find in conda :(
from game import *
from exmax import *
from numpy import savetxt
from math import log

class Game:
    def __init__(self):
        self.board = CreateBoard()

    def PrintBoard(self):
        PrintBoard(self.board)

    def MoveBoard(self, move):
        self.board = MoveBoard(self.board, move)

def on_press(key):
    if key == keyboard.Key.esc:
        exit()
    
    if key == keyboard.Key.left:
        move = 0
    elif key == keyboard.Key.up:
        move = 1
    elif key == keyboard.Key.right:
        move = 2
    elif key == keyboard.Key.down:
        move = 3
    else:
        return
    game.MoveBoard(move)
    game.PrintBoard()


if __name__ == "__main__":
    game = Game()


    # -p flag runs game in player mode 
    if len(sys.argv) == 2 and sys.argv[1] == "-p":
        game.PrintBoard()
        while not GameOver(game.board):
            with keyboard.Listener(
                    on_press=on_press) as listener:
                listener.join()
    else:
        for i in range(100):
            print("Beginning tree traversal") 
            board = CreateBoard()
            while not GameOver(board):
                tic = time.perf_counter()
                depth = round(log(50000, 4 * (16 - np.count_nonzero(board)) + 4)) # Calculate depth based on number of empty squares
                print(f"Depth: {depth}")
                _, best_move = CalculateMoveScore(board, 0, depth)
                board = MoveBoard(board, best_move)
                PrintBoard(board)
                toc = time.perf_counter()
                print(f"{toc - tic:0.4f} seconds")
            print("Game Over!")
            savetxt(f'games/1_game_{i}.csv', 2**board, fmt="%d", delimiter=',')
