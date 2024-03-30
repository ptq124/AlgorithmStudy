import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
ans=0

# 벽 조합 계싼, 백트래킹
def dfs(k, x, y):
  if k==3:
    bfs()
    return
  
  for i in range(x, n):
    start_y = y if i == x else 0
    for j in range(start_y, m):
      if maps[i][j] == 0:
        maps[i][j]=1
        dfs(k+1,i ,j+1)
        maps[i][j]=0 

# 바이러스 퍼지게 
def bfs():
  tmp_map = [row[:] for row in maps] 
  que=deque()
  dx=[1,0,-1,0]
  dy=[0,1,0,-1]

  for i in range(n):
    for j in range(m):
      if tmp_map[i][j]==2:
        que.append([i,j])

  while que:
    cx, cy=que.popleft() 

    for i in range(4):
      nx=dx[i]+cx
      ny=dy[i]+cy

      if 0<=nx<n and 0<=ny<m and tmp_map[nx][ny]==0:
        tmp_map[nx][ny]=2
        que.append([nx,ny])
  
  global ans
  cnt=0
  for i in range(n):
    cnt += tmp_map[i].count(0)
  ans=max(ans,cnt)

dfs(0, 0, 0)
print(ans)