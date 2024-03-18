#연결 요소의 갯수
#dfs

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) ### 이 부분이 재귀함수에서 깊이 제한을 넣어줌

n,m= map(int,input().split())
visit =[0 for _ in range(n+1)]
node = [[] for _ in range(n+1)]

def dfs(node,visit,s):
    visit[s] =1

    for i in node[s]:
        if visit[i]==0:#not visit
            dfs(node,visit,i)

for i in range(m):
    x,y = map(int,input().split())
    node[x].append(y)
    node[y].append(x)

count =0
for i in range(1,n+1):
    if visit[i]==0:
        dfs(node,visit,i)
        print(visit)
        count+=1 #dfs 한번 끝날 때마다 count+1

print(count)
