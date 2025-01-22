def print_board(board):
  for list in board:
    for item in list:
      print(item,end=" ")
    print()



def wincheck(board):
  for i in range(3):
    if board[i][0]==board[i][1]==board[i][2]!="⬜":
      return board[i][0]
    if board[0][i]==board[1][i]==board[2][i]!="⬜":
      return board[0][i]
  if board[0][0]==board[1][1]==board[2][2]!="⬜":
    return board[1][1]
  if board[0][2]==board[1][1]==board[2][0]!="⬜":
    return board[1][1]
  return "⬜"
def winner1():
  print("🟦 has won")
def winner2():
  print("🟥 has won")
def wheretogo(board,player):
  place = input("Which spot would you like to go to. Type the row value followed by the column value: ")
  row = int(place[0])
  column = int(place[-1])
  if board[row][column] != "⬜":
    print("Spot is taken")
  else:
    board[row][column] = player
  return board



#### program
board = [["⬜","⬜","⬜"],["⬜","⬜","⬜"],["⬜","⬜","⬜"]]  
count = 0
while count <9 and wincheck(board)=="⬜":
  print_board(board)
  if count%2==0:
    board=wheretogo(board,"🟦")
  else:
    board=wheretogo(board,"🟥")
  count +=1
  print(wincheck(board))







