import sys
input=sys.stdin.readline
from collections import deque

m,n=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
que=deque()
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs():
  while que:
    cx,cy=que.popleft()

    for i in range(4):
      nx=dx[i]+cx
      ny=dy[i]+cy
      if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0:
        arr[nx][ny]=arr[cx][cy]+1
        que.append([nx,ny])

for i in range(n):
  for j in range(m):
    if arr[i][j]==1:
      que.append([i,j]) # i: 세로, ㅓ: 가로

bfs()
ans=0

for i in arr:
  if 0 in i:
    ans=-1
    break
  ans=max(max(i),ans)

if ans==1:
  print(0)
elif ans==-1:
  print(-1)
else:
  print(ans-1)