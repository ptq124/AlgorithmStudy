import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
que=deque()

dir = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]

for _ in range(n):
  que.clear()
  I = int(input())
  x,y=map(int, input().split())
  ax,ay=map(int, input().split())
  chess=[[0]*I for _ in range(I)]
  visited=[[0]*I for _ in range(I)]
  que.append([x,y])
  chess[x][y] = 1
  visited[x][y] = 1

  while que:
    cx,cy=que.popleft()

    if cx == ax and cy == ay:
      print(chess[ax][ay]-1)
      break

    for dx,dy in dir:
      nx=dx+cx
      ny=dy+cy

      if 0<=nx<I and 0<=ny<I and not visited[nx][ny]:
        chess[nx][ny] = chess[cx][cy] + 1
        visited[nx][ny] = 1
        que.append([nx,ny])  