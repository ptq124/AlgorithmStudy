#N과 M(2)

n,m= map(int,input().split())
s=[]

def dfs(x):
    if len(s)==m:
        print(*s, sep=" ")
        return
    for i in range(x,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)