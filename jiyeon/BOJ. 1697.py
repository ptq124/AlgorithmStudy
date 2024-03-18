#숨바꼭질
# 
from collections import deque
import sys

input = sys.stdin.readline


def bfs(v):
    q = deque([v])

    while q:
        #print(q)
        v = q.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < 100001 and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)


n, k = map(int, input().split())
array = [0] * 100001
print(bfs(n))