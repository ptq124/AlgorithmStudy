#N과 M(5)

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst = sorted(lst)
s=[]

def dfs():
    if len(s)==m:
        print(*s, sep=" ")
        return
    for i in lst:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()