n=int(input("Enter the number of queens :"))

def solveNQ():
    board=[[0]*n for i in range(n)]
    
    if solveNQUtil(board,0)==False:
        print("Solution does not exist")
        return False
    else:
        printSolution(board)
        return True

def solveNQUtil(board, row):
    if(row>=n):
        return True
    for j in range(n):
        if isSafe(board,row,j):
            board[row][j]=1
            if(solveNQUtil(board,row+1)):
                return True
            board[row][j]=0
    return False

def isSafe(board,row,col):
    for a in range(n):              #for row
        if(board[row][a]==1):
            return False
    for a in range(n):              #for column
        if(board[a][col]==1):
            return False
    for a,b in zip(range(row,-1,-1),range(col,-1,-1)):   #for left diagonal
        if(board[a][b]==1):
            return False
    for a,b in zip(range(row,-1,-1),range(col,n,1)):    #for right diagonal
        if(board[a][b]==1):
            return False
    return True
    
def printSolution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print()

solveNQ()
