import sys
input=sys.stdin.readline
from collections import deque

n,m,k=map(int,input().split())
pos=[list(map(int,input().split())) for _ in range(k)]

arr=[[0]*m for _ in range(n)]
visited=[[False]*m for _ in range(n)]

for i,j in pos:
  arr[i-1][j-1]=1

ans=0

def bfs(x,y):
  que = deque()
  que.append([x,y])
  visited[x][y]=True
  dx=[1,0,-1,0]
  dy=[0,1,0,-1]
  cnt=1
  while que:
    cx,cy = que.popleft()

    for i in range(4):
      nx=dx[i]+cx
      ny=dy[i]+cy
      if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1 and not visited[nx][ny]:
        que.append((nx,ny))
        visited[nx][ny]=True
        cnt+=1

  global ans
  ans = max(ans,cnt)

for i in range(n):
  for j in range(m):
    if arr[i][j]==1:
      bfs(i,j)

print(ans)
