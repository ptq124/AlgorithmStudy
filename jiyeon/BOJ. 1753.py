# 최단경로

import sys
from heapq import *

INF = sys.maxsize

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
min_table = [INF for _ in range(v + 1)]


for _ in range(e):
    st, ed, w = map(int, input().split())
    graph[st].append((ed, w))  # 방향그래프임을 주의 하나만 추가하기

# print(graph)


def dikstra(st):
    q = []
    heappush(q, (0, st))
    min_table[st] = 0
    while q:
        we, now = heappop(q)
        if min_table[now] < we:  # 현재테이블보다 가중치가 크면 무시
            continue
        # print(q)
        for x, w in graph[now]:
            next_w = we + w

            if next_w < min_table[x]:  # 값이 더 적을경우에만 큐도 탐색 추가
                min_table[x] = next_w
                heappush(q, (next_w, x))
            # print(q, min_table)
    # print(min_table)


dikstra(start)
for i in range(1, len(min_table)):
    if min_table[i] >= 30 * 10**5:
        print("INF")
    else:
        print(min_table[i])
