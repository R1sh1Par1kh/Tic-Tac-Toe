# main.py
import random
import time

player = "X"
flip = random.randint(0,1)
if flip == 0:
  player = "O"
  
def printBoard(game):
  for r in range(3):
    for c in range(3):
      if c == 2:
        print(" " + game[r][c], end="")
      else:
        print(" " + game[r][c] + " |", end="")
    if r != 2:
      print("\n---+---+---")
  print("")
      
def win(game, turn):
  if game[0][0] == turn and game[0][1] == turn and game[0][2] == turn:
    return True
  elif game[1][0] == turn and game[1][1] == turn and game[1][2] == turn:
    return True
  elif game[2][0] == turn and game[2][1] == turn and game[2][2] == turn:
    return True
  elif game[0][0] == turn and game[1][0] == turn and game[2][0] == turn:
    return True
  elif game[0][1] == turn and game[1][1] == turn and game[2][1] == turn:
    return True
  elif game[0][2] == turn and game[1][2] == turn and game[2][2] == turn:
    return True
  elif game[0][0] == turn and game[1][1] == turn and game[2][2] == turn:
    return True
  elif game[0][2] == turn and game[1][1] == turn and game[2][0] == turn:
    return True
  else:
    return False

def testWin(game, turn):
  for r in range(3):
    for c in range(3):
      if game[r][c] == " ":
        game[r][c] = turn
        if win(game, turn) == True:
          game[r][c] = " "
          return r, c
        game[r][c] = " "
  return False
      
def testFork(game, turn):
  for r in range(3):
    for c in range(3):
      if game[r][c] == " ":
        game[r][c] = turn
        forkCounter = 0
        coords = 0, 0
        for x in range(3):
          for y in range(3):
            if game[x][y] == " ":
              game[x][y] = turn
              if win(game, turn) == True:
                coords = x, y
                forkCounter += 1
              game[x][y] = " "
        if forkCounter == 2:
          game[r][c] = " "
          if turn == "O":
            return r, c
          else:
            return coords
        game[r][c] = " "
  return False
  
def computer(game):
  # rules:
  #1 - play a winning move if there is one
  #2 - play a move that blocks the winning move from the opponent
  #3 - play center if its open
  #4 - play in the corners
  #5 - play randomly
  
  if testFork(game, "O") != False:
    r, c = testFork(game, "O")
    game[r][c] = "O"
  
  elif testFork(game, "X") != False:
    r, c = testFork(game, "X")
    game[r][c] = "O"
  
  elif testWin(game, "O") != False:
    r, c = testWin(game, "O")
    game[r][c] = "O"
    
  elif testWin(game, "X") != False:
    r, c = testWin(game, "X")
    game[r][c] = "O"
    
  elif game[1][1] == " ":
    game[1][1] = "O"
    
  elif game[0][0] == " ":
    game[0][0] = "O"
    
  elif game[0][2] == " ":
    game[0][2] = "O"
  
  elif game[2][0] == " ":
    game[2][0] = "O"
    
  elif game[2][2] == " ":
    game[2][2] = "O"

  else:
    while True:
      randrow = random.randint(0,2)
      randcol = random.randint(0,2)
      if game[randrow][randcol] == " ":
        game[randrow][randcol] = "O"
        time.sleep(1)
        break
  
grid = []
for i in range(3):
  line = []
  for j in range(3):
    line.append(" ")
  grid.append(line)
turn = player

print("Player " + turn + " won the toss!")

while True:
  printBoard(grid)
  print(" ")
  if turn == "X":
    while True: 
      row = int(input("\nWhat row would you like to choose (rows go by 0-2)?\n"))
      column = int(input("\nWhat column would you like to choose (columns go by 0-2)?\n"))
      if (-1 < row and row < 3) and (-1 < column and column < 3) and grid[row][column] == " ":
        grid[row][column] = "X"
        break
      print("Not a valid move, try again")
  else:
    computer(grid)
  
  if win(grid, turn) == True:
    printBoard(grid)
    print("Player " + turn + " wins!")
    break
  tie = True
  for r in range(3):
    for c in range(3):
      if grid[r][c] == " ":
        tie = False
  if tie == True:
    printBoard(grid)
    print("It is a tie!")
    break
        
  if turn == "X":
    turn = "O"
  else:
    turn = "X"
