import sys
input=sys.stdin.readline

n,m=map(int, input().split())
arr=list(map(int, input().split()))
visited=[0]*n
arr.sort()

def dfs(lst):
  prev=0
  if len(lst)==m:
    print(*lst)
    return
  
  for i in range(n):
    if not visited[i] and arr[i]!=prev:
      visited[i] = 1
      prev=arr[i]
      dfs(lst+[arr[i]])
      visited[i] = 0

dfs([])
