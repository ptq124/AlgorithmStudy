import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m,n,k = map(int,input().split())

pos = [list(map(int,input().split())) for _ in range(k)]

visited = [[0]*n for _ in range(m)]

for p in pos:
  x1 , y1 , x2, y2 = p[0], p[1], p[2], p[3]

  for y in range(y1, y2):
    for x in range(x1, x2):
      visited[m-y-1][x] = 1


def dfs(x,y):
  global cnt
  dx = [1,0,-1,0]
  dy = [0,1,0,-1]

  for i in range(4):
    nx=dx[i]+x
    ny=dy[i]+y

    if 0<=nx<m and 0<=ny<n and visited[nx][ny]==0:
      visited[nx][ny] = 1
      cnt+=1
      dfs(nx, ny)

a=[]
for x in range(m):
  for y in range(n):
    cnt = 1
    if visited[x][y] == 0:
      visited[x][y] = 1
      dfs(x,y)
      a.append(cnt)

a.sort()
print(len(a))
for i in a:
  print(i,end=' ')
