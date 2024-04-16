import sys
input=sys.stdin.readline

n,s=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
def dfs(lst,c,k):
  global ans
  if len(lst)==k and sum(lst)==s:
    ans+=1
    return
  
  for i in range(c,n):
    dfs(lst+[arr[i]], i+1, k)

for i in range(1,n+1):
  dfs([],0,i)

print(ans)