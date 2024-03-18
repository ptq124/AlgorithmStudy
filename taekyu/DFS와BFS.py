n,m,v=map(int,input().split())
dict={}

for i in range(n):
  dict[i+1] = []

for _ in range(m):
  a,b = map(int,input().split())

  dict[a].append(b)
  dict[b].append(a)

for i in range(n):
  dict[i+1].sort()

seen=set()

def dfs(k, depth):
  print(k,end=' ')
  seen.add(k)
  items=dict[k]

  for item in items:
    if item not in seen:
      dfs(item, depth+1)

dfs(v, 0)

print()

from collections import deque

seen=set()

def bfs(k):
  que = deque()
  que.append(k)
  seen.add(k)  
  print(k, end=' ')

  while que:
    idx = que.popleft()
    items=dict[idx]
    
    for item in items:
      if item not in seen:
        que.append(item)
        seen.add(item)
        print(item ,end=' ')
bfs(v)

