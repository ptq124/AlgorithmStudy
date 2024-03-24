import sys
input = sys.stdin.readline

n=int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [0] * n
cnt = sys.maxsize

def back_track(idx, depth):
  global cnt
  if depth==n//2:
    a,b=0,0
    for i in range(n):
      for j in range(n):
        if visited[i] == 1 and visited[j]==1:
          a+=arr[i][j]
        elif visited[i] == 0 and visited[j]==0:
          b+=arr[i][j]
    cnt = min(cnt, abs(a-b))
    return
  
  for i in range(idx, n):
    if visited[i] == 0:
      visited[i] = 1
      back_track(i+1, depth+1)
      visited[i] = 0

back_track(0,0)

print(cnt)