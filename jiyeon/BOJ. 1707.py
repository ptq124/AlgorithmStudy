#이분 그래프
#BFS 사용해서 풀기

import sys
from collections import deque

input = sys.stdin.readline

def BFS(start):
    q= deque()
    visit[start] = 1# 1로 시작 -> 다음 단계는 2로 채우기
    q.append(start)
    flag = 1#yes
    color =1
    while q:
        now = q.popleft()
        color = visit[now]
        if color==1: color =2 
        else: color =1
        #print("q:",q,"color: ",color ,"visit",visit)
        
        for i in graph[now]:
            if visit[i]==0: #방문하지 않았다면
                visit[i] = color
                q.append(i)
            elif visit[i]!=color: #방문했는데 color가 같다면?
                flag = 0 #no
                break
    return flag

tc = int(input())

#초기 input
for i in range(tc):
    v,e = map(int,input().split()) #정점 & 간선 받기
    graph =[[] for _ in range(v+1)] #정점 갯수에 맞춰 graph 생성
    visit = [0]*(v+1)
    
    for j in range(e):
        v1, v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    flag=1
    for x in range(v+1):
        if visit[x]==0:
            if BFS(x)==0:
                flag =0
    if flag==0:
        print("NO")
    else:
        print("YES")

    

            
        
    