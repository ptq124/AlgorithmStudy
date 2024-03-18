from collections import deque

n,k = map(int,input().split())

que = deque()
que.append(n)
seen = set()
visited = [0] * 100001

while que:
  num = que.popleft()

  if num==k:
    print(visited[k])
    break


  for i in [num-1,num+1,num*2]:
    if i not in seen and 0<=i<=100000:
      que.append(i)
      seen.add(i)
      visited[i] = visited[num] + 1

