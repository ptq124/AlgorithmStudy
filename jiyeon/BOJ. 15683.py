#삼성 sw 기출문제
#감시

import copy
n, m = map(int, input().split())
cctv = []
graph = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

def fill(board, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7

def dfs(depth, arr):
    global min_value

    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return
    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)


min_value = int(1e9)
dfs(0, graph)
print(min_value)



#------------------------------------------------(1번째 시도)
# import sys
# input = sys.stdin.readline

# # 0은 빈칸 6은 벽, 1-5는 cctv
# n,m = map(int,input().split())
# graph =[]
# cctv = [] #(x,y,numOf cctv) 최대 8개

# for i in range(n):
#     graph.append(list(map(int,input().split())))
#     for j in range(m):
#         if 1<=graph[i][j]<=5:
#             cctv.append((i,j,graph[i][j]))

# def ck_4_direction(x,y):
#     #왼 오 위 아래
#     left , right, up, down = 0,0,0,0
#     for i in range(x-1,-1,-1):
#         if graph[y][i]==0:
#             left+=1
#         elif graph[y][i]==6:
#             break #반복문 종료
        
#     for i in range(x+1,m):
#         if graph[y][i]==0:
#             right+=1
#         elif graph[y][i]==6:
#             break
        
#     for i in range(y-1,-1,-1):
#         if graph[i][x]==0:
#             up +=1
#         elif graph[i][x]==6:
#             break
    
#     for i in range(y+1,n):
#         if graph[i][x]==0:
#             down+=1
#         elif graph[i][x]==6:
#             break
        
#     return (left, right, up, down)
            
            
# cctv = sorted(cctv, key=lambda x : x[2],reverse=True)
# def colorTheGrpah(x,y,coloring):
#     if coloring[0]==1:
#         for i in range(x-1,-1,-1):
#             if graph[y][i]==0:
#                 graph[y][i]='#'
#             elif graph[y][i]==6:
#                 break #반복문 종료
#     if coloring[1]==1:
#         for i in range(x+1,m):
#             if graph[y][i]==0:
#                 graph[y][i]='#'
#             elif graph[y][i]==6:
#                 break
#     if coloring[2]==1:
#         for i in range(y-1,-1,-1):
#             if graph[i][x]==0:
#                 graph[i][x]='#'
#             elif graph[i][x]==6:
#                 break
#     if coloring[3]==1:
#         for i in range(y+1,n):
#             if graph[i][x]==0:
#                 graph[i][x]='#'
#             elif graph[i][x]==6:
#                 break

        
# for x,y,numTV in cctv:
#     coloring =[0,0,0,0] #색칠할 부분을 1로 체크하기(left, right, up, down)
#     # print(x,y,numTV)
#     dir_cnt = ck_4_direction(y,x)
#     if numTV==5:
#         coloring=[1,1,1,1]
        
#     elif numTV ==4:
#         coloring=[1,1,1,1]
#         dir = dir_cnt.index(min(dir_cnt))
#         coloring[dir]=0

#     elif numTV ==3:
#         checkTwo = [dir_cnt[0]+dir_cnt[2],dir_cnt[1]+dir_cnt[2],dir_cnt[0]+dir_cnt[3],dir_cnt[1]+dir_cnt[3]]
#         ck2 = checkTwo.index(max(checkTwo))
#         if ck2==0:
#             coloring=[1,0,1,0]
#         elif ck2==1:
#             coloring=[0,1,1,0]
#         elif ck2==2:
#             coloring = [1,0,0,1]
#         else:
#             coloring=[0,1,0,1]

#     elif numTV==2:
#         if dir_cnt[0]+dir_cnt[1]>dir_cnt[2]+dir_cnt[3]:
#             coloring=[1,1,0,0]
#         else:
#             coloring=[0,0,1,1]
#     elif numTV==1:
#         dir = dir_cnt.index(max(dir_cnt))
#         coloring[dir]=1
#     # print(x,y)
#     # print(coloring)
#     colorTheGrpah(y,x,coloring)
#     for i in range(n):
#         print(*graph[i])
    
# cnt=0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j]==0:
#             cnt+=1
            
# print(cnt)
