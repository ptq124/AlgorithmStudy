import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
m=int(input())

tree={}
for i in range(1,n+1):
  tree[i] = []

for _ in range(m):
  a,b=map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)

visited=[0]*(n+1)
def bfs(k):
  que=deque()
  que.append(k)
  visited[k] = 1

  while que:
    cur=que.popleft()
    items=tree[cur]
    for item in items:
      if not visited[item]:
        que.append(item)
        visited[item] = visited[cur]+1

bfs(1)
ans=0
for i in visited[2:]:
  if 0<i<=3:
    ans+=1
print(ans)