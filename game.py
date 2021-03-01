import random
import numpy as np


class Game():
    def __init__(self):
        self.startGame()

    def startGame(self):
        self.board = np.zeros((4,4),dtype=np.uint16,order='C')
        self.placeTile()
        self.placeTile()

    def placeTile(self):
        placey,placex = random.choice(np.argwhere(self.board==0))
        self.board[placex][placey] = 2 if random.random() < 0.9 else 4

    def printBoard(self):
        text = ""
        for r in range(4):
            for c in range(4):
                text += "░░░" if self.board[r][c] == 0 else "█{}█".format(self.board[r][c])
            text += "\n"
        return text

    def moveBoard(self):
        #testing with left
        for r in range(4):
            self.board[r] = self.shiftLine(self.board[r])

    def shiftLine(self,line):
        newList = [x for x in line if x!=0]
        if newList == []:
            return [0,0,0,0]
        nl = []
        for i in range(len(newList)-1):
            if newList[i]==newList[i+1]:
                nl += [newList[i]*2]
                newList[i] = 0
                newList[i+1] = 0
            else: nl += [newList[i]]
        nl+=[newList[-1]]
        nl = [x for x in nl if x!=0]
        return nl + [0]*(4-len(nl))