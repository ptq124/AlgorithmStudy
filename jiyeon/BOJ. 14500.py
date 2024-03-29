# 테크로미노
import sys
input =sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int ,input().split())))
#print(graph)

max_sum =0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
visited = [[0]*m for _ in range(n)]

def dfs(x,y,depth ,eachsum):
    global max_sum
    #print("in", eachsum ,x,y,depth)
    
    if depth==3:
        max_sum = max(max_sum,eachsum)
        return
    
    for d in range(4):
        di = x+dx[d]
        dj = y+dy[d]
        #print(di,dj)
        if 0<=di<n and 0<=dj<m and visited[di][dj]==0:
            #print(visited)
            visited[di][dj]=1
            dfs(di,dj,depth+1,eachsum+graph[di][dj])
            visited[di][dj]=0
    
for i in range(n):
    for j in range(m):
        visited[i][j] =1
        dfs(i,j,0,graph[i][j])
        visited[i][j]=0
        #print(max_sum)
        if 1<=i<n-1 and 1<=j<m-1: #ㅗㅜㅏㅓ
            checkOne = sum([graph[i-1][j], graph[i+1][j],graph[i][j-1],graph[i][j+1]]) - min(graph[i-1][j], graph[i+1][j],graph[i][j-1],graph[i][j+1])
            checkOne+= graph[i][j]
            max_sum = max(checkOne,max_sum)
print(max_sum)