# 이모티콘

import sys
from collections import deque
input = sys.stdin.readline

s = int(input())

q=deque()
q.append((1,0))#화면, 클립보드

dist = [[-1]* 1001 for _ in range(1001)] #dp를 추가할 곳
dist[1][0] =0 

while q:
    screen, clip = q.popleft()
    
    if screen ==s:
        print(dist[screen][clip])
        break
    
    if screen<1001 and dist[screen][screen]==-1 : #클립복사
        dist[screen][screen] = dist[screen][clip]+1
        q.append((screen,screen))
    if screen+clip<1001 and dist[screen+clip][clip] == -1 : # 붙여넣기
        dist[screen+clip][clip] = dist[screen][clip]+1
        q.append((screen+clip,clip))
    if  screen-1>1 and dist[screen-1][clip] ==-1 :
        dist[screen-1][clip] = dist[screen][clip]+1
        q.append((screen-1,clip))
    #print(q)
    
        

    