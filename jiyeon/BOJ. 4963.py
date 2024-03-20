# 섬의 개수 
# 그래프

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

w, h = map(int, input().split())


def dfs(y, x):
    graph[y][x] = 0  # 방문표시
    dx = [1, -1, 0, 0,1,-1,1,-1]
    dy = [0, 0, -1, 1,1,-1,-1,1]
    for d in range(8):

        xx = dx[d] + x
        yy = dy[d] + y

        if xx >= 0 and xx < w and yy >= 0 and yy < h and graph[yy][xx] == 1:
            #print(graph, xx, yy)
            dfs(yy, xx)


while w != 0 and h != 0:
    graph = []
    count = 0
    for i in range(h):
        graph.append(list(map(int, input().split())))
    #print(graph)
    for i in range(h):  # 높이
        for j in range(w):  # 가로
            if graph[i][j] == 1:  # land 일 경우
                dfs(i,j)
                count += 1
                #print(graph)
    print(count)
    w, h = map(int, input().split())