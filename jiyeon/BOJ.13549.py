# 숨바꼭질3
# dfs
import sys
from collections import deque

input= sys.stdin.readline
n,m = map(int,input().split())
time = [100001] * 100001

q= deque()
q.append(n)
time[n] =0

while q:
    subin = q.popleft()
    
    if subin == m:
        print(time[subin])
        break
    
    if subin-1 >=0 and time[subin-1]>time[subin]+1: #not visit
        time[subin-1] = time[subin]+1
        q.append(subin-1)
    if subin*2 <=100000 and time[subin*2]>time[subin]:
        time[subin*2] = time[subin]
        q.append(subin*2)
    if subin+1 <=100000 and time[subin+1]>time[subin]+1: #not visit
        time[subin+1] = time[subin]+1
        q.append(subin+1)
    #print(q,time)