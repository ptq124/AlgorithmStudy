import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n=int(input())

def dfs(k, group):
  global check

  visited[k] = group
  items = dict[k]

  for item in items:
    if visited[item]==0:
      dfs(item, -group)
    elif visited[item] == visited[k]:
      check = False

for _ in range(n):

  v,e = map(int,input().split())
  dict = {}
  visited = [0] * (v+1)

  for i in range(1, v+1):
    dict[i] = []

  for _ in range(e):
    a, b = map(int,input().split())
    dict[a].append(b)
    dict[b].append(a)
  
  check = True

  for i in range(1,v+1):
    if visited[i] == 0:
      dfs(i,1)
      if not check:
        break
  
  if check:
    print('YES')
  else:
    print("NO")




