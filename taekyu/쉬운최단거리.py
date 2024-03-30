import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
que=deque()
visited=[[False]*m for _ in range(n)]
ans = [[0]*m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if arr[i][j]==2:
      que.append([i,j])
      visited[i][j]=True
      break
  if que:
    break

dx=[1,0,-1,0]
dy=[0,1,0,-1]


while que:
  x,y=que.popleft()

  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y

    if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 1 and not visited[nx][ny]:
      que.append([nx,ny])
      visited[nx][ny] = True
      ans[nx][ny]= ans[x][y] + 1

for i in range(n):
  for j in range(m):
    if arr[i][j]==0:
      visited[i][j] = True

for i in range(n):
  for j in range(m):
    if not visited[i][j]:
      print(-1, end=" ")
    else:
      print(ans[i][j], end=" ")
  print()

