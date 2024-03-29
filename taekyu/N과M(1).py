import sys
input = sys.stdin.readline

# n,m=map(int,input().split())

# arr = [x for x in range(1,n+1)]

# a =[]
# def back_track(k,m):

#   if m==len(a):
#     print(' '.join(str(x) for x in a))
#     return

#   for i in range(0,len(arr)):
#     if arr[i] not in a:
#       a.append(arr[i])
#       back_track(k+1,m)
#       a.pop()

# back_track(0,m)

n,m=map(int,input().split())
arr = [x for x in range(1,n+1)]
visited=[0]*n

def dfs(k, lst):
  if k==m:
    ans.append(lst)

  for i in range(n):
    if not visited[i]:
      visited[i] = 1
      dfs(k+1, lst+[arr[i]])
      visited[i] = 0
ans=[]
dfs(0, [])

for i in ans:
  print(*i)