import sys
input=sys.stdin.readline

from collections import deque

f,s,g,u,d = map(int,input().split())

que = deque()
visited = [0] * (f+1)
visited[s] = 1
que.append(s)

while que:
  cur = que.popleft()

  if cur == g:
    print(visited[cur]-1)
    break

  for i in (cur+u, cur-d):
    if 0<i<=f and visited[i] == 0:
      visited[i] = visited[cur] + 1
      que.append(i)

if visited[g] == 0:
  print("use the stairs")