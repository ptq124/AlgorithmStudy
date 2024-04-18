import sys
input=sys.stdin.readline
from  collections import deque

n=int(input())
arr=[list(input().strip()) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
que=deque()
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(x,y,color):
  que.append([x,y])

  while que:
    cx,cy=que.popleft()
    for i in range(4):
      nx=dx[i]+cx
      ny=dy[i]+cy
      if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arr[nx][ny]==color:
        visited[nx][ny]=1
        que.append([nx,ny])

ans=0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      if arr[i][j]=='R':
        visited[i][j]=1
        bfs(i,j,'R') 
        ans+=1
      if arr[i][j]=='G':
        visited[i][j]=1
        bfs(i,j,'G') 
        ans+=1
      if arr[i][j]=='B':
        visited[i][j]=1
        bfs(i,j,'B') 
        ans+=1
print(ans, end=' ')

visited1=[[0]*n for _ in range(n)]
que1=deque()

def bfs1(x,y,color):
  que1.append([x,y])

  while que1:
    cx,cy=que1.popleft()
    for i in range(4):
      nx=dx[i]+cx
      ny=dy[i]+cy
      if 0<=nx<n and 0<=ny<n and not visited1[nx][ny] and arr[nx][ny] in color:
        visited1[nx][ny]=1
        que1.append([nx,ny])

ans=0
for i in range(n):
  for j in range(n):
    if not visited1[i][j]:
      if arr[i][j]=='R' or arr[i][j]=='G':
        visited1[i][j]=1
        bfs1(i,j,['R','G']) 
        ans+=1
      if arr[i][j]=='B':
        visited1[i][j]=1
        bfs1(i,j,['B']) 
        ans+=1
print(ans)