from collections import deque

def bfs(x,y):
  que = deque()
  dx=[1,0,-1,0,1,-1,1,-1]
  dy=[0,1,0,-1,1,1,-1,-1]
  que.append([x,y])
  land[x][y]=0

  while que:
    cur_x,cur_y = que.popleft()
    for i in range(8):
      nx = cur_x + dx[i]
      ny = cur_y + dy[i]

      if 0<=nx<h and 0<=ny<w and land[nx][ny]==1:
        que.append([nx,ny])
        land[nx][ny]=0


while True:
  w,h=map(int,input().split())
  if w==0 and h==0:
    break
  land = []
  for _ in range(h):
    land.append(list(map(int,input().split())))    
  cnt=0
  for i in range(h):
    for j in range(w):
      if land[i][j]==1:
        bfs(i,j)
        cnt+=1
  print(cnt)