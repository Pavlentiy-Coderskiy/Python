import random
board = [['1-1','1-2','1-3'],['2-1','2-2','2-3'],['3-1','3-2','3-3']]
symbol = 'X'
print("===========================================================================================")
print("=============================Добро пожаловать в Крестики-нолики============================")
print("===========================================================================================")
  

  board[x][y] = "",symbol,""
print("/n=============")
for i in range(3):
	print("|",end="")
	for i in range(3):
		print(board[0+i][j]+"|",end="")
	print("/n=============")
    
while True:
   pa = input("Куда поставить "+ symbol+"?")
    if pa in [["1-1","1-2","1-3"],["2-1","2-2","2-3"],["3-1","3-2","3-3"]]
		x = int(pa[0])-1
		y = int[pa[2]]-1
    	if board[x][y] not in ["X","O"]
      		break
		else: 
	  		print("Клетка занята")
	else:
		print("Попробуйте ещё раз")
      if (board[0][0] == board[0][1] == board[0][2] or
            board[1][0] == board[1][1] == board[1][2] or
            board[2][0] == board[2][1] == board[2][2] or

            board[0][0] == board[1][0] == board[2][0] or
            board[0][1] == board[1][1] == board[2][1] or
            board[0][2] == board[1][2] == board[2][2] or

            board[0][0] == board[1][1] == board[2][2] or
            board[0][2] == board[1][1] == board[2][0]):
      	print("Победил", symbol)
        break
if symbol =="X"
   symbol ="O"
else:





