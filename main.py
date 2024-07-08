import os
import time
import random

# Game variables
points = 0
board = [
    ['-----------------'],
    ['-----------------'],
    ['-----------------'],
    ['-----------------']   
]
# --- Player --- #
player = "X"
# --- Player positions --- #
playerX = 0
playerY = 0
prevPlayerX = 0
prevPlayerY = 0
# --- Fruit --- #
fruit = "O"
# --- Fruit positions --- #
fruitX = 0
fruitY = 0
prevFruitX = 0
prevFruitY = 0
# --- Obstacles --- #
obstacle = "#"
obstacleX = 0
obstacleY = 0
obstacles = [] # An iterable of obstacles position

# --- GAME FUNCTIONS ---#

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
    UpdatePlayer()


# Update a single object on the game board.
def updateObjects(y, x, obj):
    y = list(y)
    y[x] = obj
    return ''.join(y)

# --- PLAYER FUNCTIONS --- #
# Update the player position on the game board.
def UpdatePlayer():
    global board, player, playerX, playerY, prevPlayerX, prevPlayerY
    # Resets the previous player position
    board[prevPlayerY][0] = updateObjects(board[prevPlayerY][0], prevPlayerX, "-")
    prevPlayerX = playerX
    prevPlayerY = playerY

    # Updates the current player position
    board[playerY][0] = updateObjects(board[playerY][0], playerX, player)
    CheckFruitColision()
    CheckObstacleColision()
    os.system("cls||clear")


# --- FRUITS FUNCTIONS --- #
# Update the fruit position by random X & Y positions
def UpdateFruit():
    global board, fruit, fruitX, fruitY
    # board[prevFruitY][0] = updateObjects(board[prevPlayerY][0], prevPlayerX, "-")
    fruitY = random.randint(0, len(board) - 1)
    fruitX = random.randint(0, len(board[fruitY][0]) - 1)

    board[fruitY][0] = updateObjects(board[fruitY][0], fruitX, fruit)
    os.system("cls||clear")

def CheckFruitColision():
    global playerX, playerY, fruitX, fruitY, points
    if playerX == fruitX and playerY == fruitY:
        points += 1 
        UpdateObstacle() 
        UpdateFruit()  # Updates fruit's position after colision

# --- OBSTACLE FUNCTIONS --- #
# Update the obstacle position by random X & Y positions
def UpdateObstacle():
    global board, obstacle, obstacleX, obstacleY

    obstacleY = random.randint(0, len(board) - 1)
    obstacleX = random.randint(0, len(board[obstacleY][0]) - 1)
    obstacles.append((obstacleX, obstacleY))  
    board[obstacleY][0] = updateObjects(board[obstacleY][0], obstacleX, obstacle)
    os.system("cls||clear")

# Check if the player has collided with an obstacle
def CheckObstacleColision():
    global playerX, playerY, obstacleX, obstacleY
    for obstacleX, obstacleY in obstacles:
        if playerX == obstacleX and playerY == obstacleY:
            print("Game Over!")
            exit()

# --- USER FUNCTIONS --- #
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

# GAME RUNNER
UpdateObstacle() # Initialize obstacle's position
UpdateFruit() # Initialize fruit's position
while True:
    UpdateGame()
    DrawBoard()
    if points < 10:   
        playerInput()
    else:
        print("You won!")
        break