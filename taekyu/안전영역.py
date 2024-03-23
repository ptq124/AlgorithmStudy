import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

arr = []
h = 0 

for i in range(n):
  arr.append(list(map(int,input().split())))
  h = max(arr[i])

def dfs(x,y):
  dx = [1,0,-1,0]
  dy = [0,1,0,-1]

  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
      visited[nx][ny] = 1
      dfs(nx, ny)


def check(h):
  for i in range(n):
    for j in range(n):
      if arr[i][j] <= h:
        visited[i][j] = 1
a = []
cnt = 0

for i in range(min(map(min, arr))-1, max(map(max, arr))+1):
  visited = [[0]*n for _ in range(n)]
  check(i)
  for x in range(n):
    for y in range(n):
      if visited[x][y] == 0:
        visited[x][y]=1
        dfs(x,y)
        cnt+=1
  a.append(cnt)
  cnt = 0

print(max(a))