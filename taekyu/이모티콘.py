import sys
from collections import deque

input = sys.stdin.readline

s=int(input())
visited = [[False] * (s + 1) for _ in range(s + 1)]
que = deque()
que.append([1,0,0]) # screen, clip, count
visited[1][0] = True

while que:
  screen, clip, count = que.popleft()

  if screen == s:
    print(count)
    break
  
  if not visited[screen][screen]:
    visited[screen][screen] = True
    que.append([screen,screen,count+1])
  if screen + clip <= s and not visited[screen+clip][clip]:
    visited[screen+clip][clip] = True
    que.append([screen+clip,clip,count+1])
  if screen - 1 >= 0 and not visited[screen-1][clip]:  
    visited[screen-1][clip] = True
    que.append([screen-1,clip,count+1])


