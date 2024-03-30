import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

cctv=[]
mode=[
  [],
  [[0],[1],[2],[3]],
  [[0,2],[1,3]],
  [[0,1],[1,2],[2,3],[0,3]],
  [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
  [[0,1,2,3]]
]

for i in range(n):
  for j in range(m):
    if 1<=arr[i][j]<=5:
      cctv.append([arr[i][j],i,j])

def fill(tmp, x, y, mn):
  dx=[1,0,-1,0]
  dy=[0,1,0,-1]

  for i in mn:
    nx=x
    ny=y
    while True:
      nx += dx[i]
      ny += dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        break
      if tmp[nx][ny]==6:
        break
      if tmp[nx][ny]==0:
        tmp[nx][ny]='#'

  return tmp

ans=int(1e9)

def dfs(k, lst):

  if k==len(cctv): # 탈출 조건
    tmp = [row[:] for row in arr]

    for j in range(len(lst)):
      x, y = cctv[j][1] , cctv[j][2]
      tmp = fill(tmp, x, y, lst[j])

    global ans
    cnt=0
    for i in tmp:
      cnt+=i.count(0)
    ans = min(ans,cnt)
    
    return
  
  cctv_num, x, y = cctv[k]

  for i in mode[cctv_num]: # 조합 로직
    dfs(k+1, lst+[i])

dfs(0, [])

print(ans)