import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split()) # 세로, 가로
arr=[list(input().strip()) for _ in range(r)]

que=deque()
que2=deque()

visited=[[0] * c for _ in range(r)]
visited2=[[0] * c for _ in range(r)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs():
  while que:
    cx,cy=que.popleft()

    for i in range(4):
      nx=dx[i]+cx
      ny=dy[i]+cy
      if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and arr[nx][ny]!="#":
        visited[nx][ny] = visited[cx][cy] + 1
        que.append([nx,ny])

  while que2:
    cx,cy=que2.popleft()
    for i in range(4):
      nx=dx[i]+cx
      ny=dy[i]+cy
      if 0<=nx<r and 0<=ny<c:
        if not visited2[nx][ny] and arr[nx][ny]!="#":
          if not visited[nx][ny] or visited[nx][ny] > visited2[cx][cy] + 1:
            visited2[nx][ny] = visited2[cx][cy] + 1
            que2.append([nx,ny])     
      else:
        return visited2[cx][cy]
  return "IMPOSSIBLE"

for i in range(r):
  for j in range(c):
    if arr[i][j] =='F':
      que.append([i,j])
      visited[i][j] = 1
    if arr[i][j] == 'J':
      que2.append([i,j])
      visited2[i][j] = 1

print(bfs())