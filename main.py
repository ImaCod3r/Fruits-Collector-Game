import os
import time
import random

board = [
    ['-----------------'],
    ['-----------------'],
    ['-----------------'],
    ['-----------------']
]

# Game variables
player = "O"
points = 0
prevPlayerX = 0
prevPlayerY = 0

# Player positions
playerX = 0
playerY = 0


# Draw the current state of the game board.
# Prints the board with the current player position and points.
def DrawBoard():
    global board, points, playerX, playerY

    print(f"Points:{points}")

    for y in board:
        for x in y:
            print(x)
    
    time.sleep(0.33)

# Clear the console screen.
def UpdateGame():
    os.system("cls||clear")

# Update the player position on the game board.
def UpdatePlayer():
    global board, player, playerX, playerY, prevPlayerX, prevPlayerY
    resetPreviousPosition()
    prevPlayerX = playerX
    prevPlayerY = playerY
    # Updates the player
    board[playerY][0] = updateObjects(board[playerY][0], playerX, player)
    UpdateGame()


# Update a single object on the game board.
def updateObjects(y, x, obj):
    y = list(y)
    y[x] = obj

    return ''.join(y)

# Waits for the user input to update de player position according to PlayerY & PlayerX
def playerInput():
    global board, playerX, playerY

    key = input("Enter:")

    if key.upper() == "W" and playerY > 0:
        playerY -= 1
        print("UP")

    elif key.upper() == "D" and playerX < len(board[playerY][0]) - 1:
        playerX += 1
        print("RIGHT")

    elif key.upper() == "A" and playerX > 0:
        playerX -= 1
        print("LEFT")

    elif key.upper() == "S" and playerY < len(board) - 1:
        playerY += 1
        print("DOWN")
    else:
        pass

# Resets the previous player position
def resetPreviousPosition():
    global board, prevPlayerX, prevPlayerY
    board[prevPlayerY][0] = updateObjects(board[prevPlayerY][0], prevPlayerX, "-")

while True:
    UpdatePlayer()
    DrawBoard()
    playerInput()