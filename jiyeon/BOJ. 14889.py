#스타트와 링크
#DFS(BACK TRACKING) + 브루트 포스


#DFS(BACK TRACKING) + 브루트 포스
import sys
from itertools import *

input = sys.stdin.readline

n = int(input())
visit = [0 for _ in range(n)] # visit체크
S=[]
visited = [False for _ in range(n)]

for i in range(n):
    S.append(list(map(int,input().split())))

min_value = 100000
def backtracking(depth, idx):
    global min_value
    if depth== n/2:
        a,b =0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a+= S[i][j]
                elif not visited[i] and not visited[j]:
                    b+= S[i][j]
        min_value = min(min_value, abs(a-b))
        return
    
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            backtracking(depth+1, i+1)
            visited[i] = False

backtracking(0,0)
print(min_value)
