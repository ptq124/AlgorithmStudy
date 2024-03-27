import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
que = deque()
cnt = 0
max_width = 0

def bfs(x,y):
  global max_width

  visited[x][y] = 1
  que.append([x,y])
  dx=[1,0,-1,0]
  dy=[0,1,0,-1]
  cur_wdth = 1

  while que:
    curx, cury = que.popleft()
    
    for i in range(4):
      nx = dx[i] + curx
      ny = dy[i] + cury

      if 0<=nx<n and 0<=ny<m and arr[nx][ny] and not visited[nx][ny]:
        visited[nx][ny] = 1
        cur_wdth+=1
        que.append([nx,ny])

  max_width = max(cur_wdth,max_width)

for x in range(n):
  for y in range(m):
    if arr[x][y]==1 and not visited[x][y]:
      cnt+=1
      bfs(x,y)

print(cnt)
print(max_width)