import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[x for x in range(1,n+1)]
ans=[]
def dfs(k,lst):
  if len(lst) == m:
    ans.append(lst)
    return
  
  for i in range(n):
    dfs(i,lst+[arr[i]])


dfs(0,[])
for i in ans:
  print(*i)