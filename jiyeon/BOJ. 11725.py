#트리의 부모 찾기

import sys
input =sys.stdin.readline

n= int(input())
graph = {}
check_parent ={}

visited = []

for i in range(n-1):
    x, y = map(int, input().split())

    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []

    graph[x].append(y)
    graph[y].append(x)
    #print(graph)

def dfs(root):
    visited.append(root)
    for node in graph[root]:
        if node not in visited: #방문하지 않았을 경우
            check_parent[node]= root
            #print(check_parent)
            dfs(node)

dfs(1)
for i in range(n-2):
    print(sorted(check_parent.items())[i][1])