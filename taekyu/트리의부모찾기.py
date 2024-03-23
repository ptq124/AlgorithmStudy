import sys

input = sys.stdin.readline 
sys.setrecursionlimit(1000000)

n=int(input())

dict = {}
for i in range(1,n+1):
  dict[i] = []

seen = set()

for _ in range(n-1):
  a,b = map(int,input().split())
  dict[a].append(b)
  dict[b].append(a)

parents = [0] * (n+1)

def dfs(k):
  items=dict[k]
  seen.add(k)
  for item in items:
    if item not in seen:
      parents[item] = k
      seen.add(item)
      dfs(item)

dfs(1)


for i in range(2,len(parents)):
  print(parents[i])