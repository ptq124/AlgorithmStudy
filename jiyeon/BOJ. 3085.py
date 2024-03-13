#사탕게임(브루트 포스)

import sys
input = sys.stdin.readline

n = int(input())
board =[]
max_Result =0

def checking (row,column,color):
    row_cnt =0
    col_cnt=0
    max_cnt =0
    for i in range(n):
        if board[row][i]==color:
            row_cnt+=1
        else:
            #max_cnt = max(max_cnt, row_cnt)
            row_cnt=0
        if board[i][column]==color:
            col_cnt+=1
        else:
            #max_cnt = max(max_cnt, col_cnt)
            col_cnt = 0
        max_cnt = max(max_cnt,col_cnt,row_cnt)
        #print(max_cnt,color,row_cnt,col_cnt,"in def")
    return max_cnt

for i in range(n):
    board.append(list(input().rstrip()))

for i in range(n-1):
    for j in range(n):
        #print(i,j)
        if j!=n-1:
            board[i][j],board[i][j+1] = board[i][j+1],board[i][j]
            check1 = checking(i,j,board[i][j])
            check3 = checking(i,j+1,board[i][j+1])
            max_Result = max(check1,check3,max_Result)
            #print(board, check1,check3)
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        check2 = checking(i, j, board[i][j])
        check4 = checking(i+1, j, board[i+1][j])
        #print(board, check2,check4)
        max_Result = max(check2,check4 ,max_Result)
        board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]


print(max_Result)