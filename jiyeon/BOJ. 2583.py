import sys
input =sys.stdin.readline
sys.setrecursionlimit(100000)
dx=[1,0,-1,0]
dy = [0,1,0,-1]
m,n,k = map(int,input().split())
graph = [[0 for _ in range(n)]for _ in range(m)]

for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            graph[y][x] =1 #갈수 없는 곳 표시


def dfs(y,x):
    graph[y][x] =1
    global area
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<m and 0<=nx<n and graph[ny][nx]==0:
            dfs(ny,nx)
            area+=1
cnt=0
#print(graph)
areas=[]
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            area = 1
            dfs(i,j)
            cnt+=1 #총갯수수
            areas.append(area)

print(cnt)
print(*sorted(areas),sep=" ")