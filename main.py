import os
import time
import random

board = [
    ['-----------------'],
    ['-----------------'],
    ['-----------------'],
    ['-----------------']
]

# posX = 0
# posY = 0

def DrawBoard():
    global board

    for y in board:
        for x in y:
            print(x)
    
    time.sleep(0.33)

def ResetBoard():
    global board

    for row in board:
        row[0] = row[0].replace("#", "-")


def UpdateBoard():
    global board

    posY = random.randint(0, len(board) - 1)
    posX = random.randint(0, len(board[posY][0]) - 1)

    ResetBoard()
    board[posY][0] = replaceString(board[posY][0], posX, "#")

    os.system("cls||clear")

def replaceString(string, pos, char):
    string = list(string)
    string[pos] = char

    return ''.join(string)

while True:
    DrawBoard()
    UpdateBoard()