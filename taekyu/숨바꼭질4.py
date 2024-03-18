from collections import deque

n, k = map(int,input().split())
seen=set()
que=deque()
visited = [0] * 100001
path = [0] * 100001

def bfs(v):
  que.append(v)
  seen.add(v)
  while que:
    cur=que.popleft()

    if cur == k:
      a=[]
      print(visited[cur])
      while cur != n:
        a.append(cur)
        cur=path[cur]
      a.append(n)
      print(' '.join(map(str, a[::-1])))
      break
  
    for i in [cur+1,cur-1,cur*2]:
      if i not in seen and 0<=i<=100000:
        que.append(i)
        seen.add(i)
        path[i] = cur
        visited[i] = visited[cur] + 1

bfs(n)