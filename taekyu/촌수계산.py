import sys

input = sys.stdin.readline

n=int(input())
q,w = map(int, input().split())
m=int(input())

tree={}
for i in range(1,n+1):
  tree[i]=[]

for _ in range(m):
  a,b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

seen = set()
cnt=0
arr=[0]*(n+1)

def dfs(k):
  if k==w:
    return
  
  seen.add(k)
  items = tree[k]

  for item in items:
    if item not in seen:
      arr[item] = arr[k] + 1
      seen.add(item)
      dfs(item)

dfs(q)

if arr[w] > 0:
  print(arr[w])
else:
  print(-1)