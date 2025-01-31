def print_board(n, board):
  # premake +---+ style boundary using string mutiplication and concatination
  boundary_line = ("+---" * n) + "+"
  # range over every row in board (an n by n board)
  for i in range(n):
    # print a leading boundary line
    print(boundary_line)
    # start string for row i with leading bar
    row_i = "|"
    # range over every column in board (an n by n board)
    for j in range(n):
      # update row_i string with space, characher from board, space, and trailing bar
      # this completes "cell j" for row i
      row_i += " " + board[i][j] + " " + "|"
    # print the completed row i
    print(row_i)
  # print final boundary line
  print(boundary_line)

def make_empty_board(side):
  board = [[" " for _ in range(side)]for _ in range(side)]
  return board

def get_location(n, board):
  while True:
    userinputrow = input("Please enter a row index between 0 and " + str(n-1) + ":")
    userinputcol = input("Please enter a column index between 0 and " + str(n-1) + ":")
    if(not userinputrow.isdigit() or not userinputcol.isdigit()):
      print("(" + userinputrow + ", " + userinputcol + ")" + " is not a legal input!")
      continue
    row, col = int(userinputrow), int(userinputcol)
    if(row not in range(n) or col not in range(n)):
      print("(" + userinputrow + ", " + userinputcol + ")" + " is not a legal space!")
      continue
    if(board[row][col] != " "):
      print("(" + userinputrow + ", " + userinputcol + ")" + " is not an available space!")
      continue
    else:
      return row , col

def row_win(n,board,player):
  for row in board:
    if all(spaces == player for spaces in row):
      return True
  return False
def col_win(n,board,player):
  for col in range(n):
    if all(board[row][col] == player for row in range(n)):
      return True
  return False
def diag_win(n, board, player):
    if all(board[i][i] == player for i in range(n)):
        return True
    return False

def anti_diag_win(n, board, player):
    if all(board[i][n-1-i] == player for i in range(n)):
        return True
    return False

def has_won(n,board,player):
  if(row_win(n,board,player) == True or col_win(n,board,player) == True or diag_win(n,board,player) == True or anti_diag_win(n,board,player) == True):
    return True
  else:
    return False
  
def play_game(n):
  print("*** Welcome to "+ str(n) +" by " + str(n) + " Tic-Tac-Toe ***")
  board = make_empty_board(n)
  print_board(n,board)
  players = ["X","O"]
  turn_counter = 0
  max_turn = n*n
  

  while True:
    active_player = players[turn_counter%2]
    print("* " + active_player + "'s turn *")
    row,col = get_location(n,board)
    board[row][col] = active_player
    print_board(n,board)
    turn_counter += 1
    if(has_won(n,board,active_player)):
      print(active_player + " wins!")
      break
    if(turn_counter == max_turn):
      print("Tie!")
      break
