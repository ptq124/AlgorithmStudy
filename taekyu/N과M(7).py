import sys
input=sys.stdin.readline

n,m = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

def dfs(k, lst):
  if len(lst)==m:
    print(*lst)
    return
  
  for i in range(n):
    dfs(k+1, lst+[arr[i]])


dfs(0,[])