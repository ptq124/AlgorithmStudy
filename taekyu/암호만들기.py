L,C = map(int,input().split())
arr = list(map(str,input().split()))
code = []
arr.sort()

a = []
s='aeiou'

def dfs(strat,depth):
  if depth == L:
    v_count, c_count = 0, 0
    for c in code[:]:
      if c in s:
        v_count+=1
      else:
        c_count+=1
    if v_count >= 1 and c_count >= 2:
      a.append(code[:])
    return

  for i in range(strat, C):
    code.append(arr[i])
    dfs(i+1, depth+1)
    code.pop()

dfs(0, 0)
for i in range(len(a)):
  print(''.join(a[i]))