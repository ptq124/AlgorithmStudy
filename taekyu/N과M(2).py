import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
visited=[0]*n
ans=[]

def dfs(k,lst):
  if len(lst)==m:
    ans.append(lst)
    return
  
  for i in range(k, n):
    if not visited[i]:
      visited[i] = 1
      dfs(i+1, lst+[arr[i]])
      visited[i] = 0

dfs(0,[])

for i in ans:
  print(*i)