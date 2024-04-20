# 배열돌리기1
import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = []
q= deque()

dx=[0,1,0,-1]
dy=[1,0,-1,0] #아래, 오른, 위, 왼

for i in range(n):
    graph.append(list(map(int,input().split())))

loops = min(n,m)//2 # 사각형 내에 돌 수 있는 loop수
for i in range(loops):
    q.clear()
    q.extend(graph[i][i:m-i]) #위 가로
    q.extend([row[m-i-1] for row in graph[i+1:n-i-1]])
    q.extend(graph[n-i-1][i:m-i][::-1])
    q.extend([row[i] for row in graph[i+1:n-i-1][::-1]])
    
    q.rotate(-r)
    # print(list(q))
    
    for j in range(i,m-i):
        graph[i][j] = q.popleft()
    for j in range(i+1, n-i-1):          
        graph[j][m-i-1] = q.popleft()
    for j in range(m-i-1, i-1, -1):           
        graph[n-i-1][j] = q.popleft()  
    for j in range(n-i-2, i, -1):         
        graph[j][i] = q.popleft()    

for i in range(n):
    print(*graph[i], sep= " ")
    
# # 배열돌리기1
# import sys
# input = sys.stdin.readline

# n,m,r = map(int,input().split())
# graph = []

# dx=[0,1,0,-1]
# dy=[1,0,-1,0] #아래, 오른, 위, 왼

# for i in range(n):
#     graph.append(list(map(int,input().split())))

# # print(graph)

# def rotation(x1,y1,x2,y2):
#     temp = graph[x1][y1]
#     x,y = x1,y1
#     for i in range(4):
#         while True:
#             # print(x,y)
#             x,y = x+dx[i], y+dy[i]
#             if x<x1 or x>x2 or y<y1 or y>y2:
#                 x,y = x-dx[i], y-dy[i]
#                 break
#             graph[x-dx[i]][y-dy[i]] = graph[x][y]
        
#     graph[x1+1][y1]= temp
#     # print(*graph,sep="\n")
#     # print()
    
    
# for i in range(r): #회전수
#     x1,y1,x2,y2 = 0,0,n-1,m-1
#     #print(i)
#     while x1<=x2 and y1<=y2:
#         rotation(x1,y1,x2,y2)
#         x1,y1,x2,y2 = x1+1,y1+1,x2-1,y2-1
#         #print(x1,y1,x2,y2)
        
# for i in range(n):
#     print(*graph[i], sep=" ")