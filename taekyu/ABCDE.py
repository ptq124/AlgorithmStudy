n,m = map(int,input().split())

dict = {}

for i in range(n):
  dict[i] = []

arr = [list(map(int,input().split())) for _ in range(m)]

for i in arr:
  q,w = i[0], i[1]
  dict[q].append(w)
  dict[w].append(q)

seen =  set()
stack=[]
check =False

def dfs(k, depth):
  global check

  if depth == 4:
    check=True
    return

  items = dict[k]

  for item in items:
    if item not in seen:
      seen.add(item)
      dfs(item, depth+1)
      seen.remove(item)

for i in range(n):
  seen.add(i)
  dfs(i, 0)
  seen.remove(i)

  if check:
    break

if check:
  print(1)
else:
  print(0)
