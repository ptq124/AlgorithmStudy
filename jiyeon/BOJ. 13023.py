#ABCDE dfs 그래프 문제

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
relations =[[] for _ in range(n)]
visited = [False]*2001
result =0

for i in range(m):#관계 추가
    a,b= map(int,input().split())
    relations[a].append(b)
    relations[b].append(a)
#print(relations)

def dfs(idx, depth):
    global result
    visited[start] = True  # 첫 방문 방문처리

    if depth ==4:
        result =1
        return
    for i in relations[idx]:
        if visited[i] == False: #방문하지 않았으면
            visited[i] = True
            dfs(i,depth+1)
            visited[i] = False


for start in range(n):#사람 수 대로 계산
    if result ==1:
        break

    dfs(start,0) #깊이는 0 으로 시작
    visited[start] = False
print(result)
