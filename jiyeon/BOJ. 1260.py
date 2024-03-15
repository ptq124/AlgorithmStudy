#dfs 와 bfs

from collections import deque

def dfs(graph, v, visited):
    visited[v] =True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] =True
    
    while queue:
        v= queue.popleft()
        print(v,end=' ')
        for i in graph[v]:#현재 정점과 연결된, 아직 방문하지 않은 원소들 큐에 삽입
            if not visited[i] :
                queue.append(i)
                visited[i] = True

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]#노드의 갯수만큼 리스트 생성
#print(graph)

for i in range(m):
    vt1,vt2 = map(int, input().split())
    graph[vt1].append(vt2)
    graph[vt2].append(vt1)

for i in graph:
    i.sort() #방문 가능한 정점이 여러개인 경우에는 정점이 작은 번호부터

#print(graph)
visited = [False] *(n+1)
dfs(graph,v,visited)
print()
visited = [False] *(n+1)
bfs(graph,v,visited)