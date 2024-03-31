import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
visited=[0]*n

arr.sort()

def dfs(k,s,lst):
  if len(lst)==m:
    print(*lst)
    return
  
  for i in range(s, n):
    if not visited[i]:
      visited[i]=1
      dfs(k+1,i+1,lst+[arr[i]])
      visited[i]=0

dfs(0,0,[])