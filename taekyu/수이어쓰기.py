from collections import deque

n=input()
arr = deque([c for c in n])
check = False

for i in range(1, 30000):
  i = str(i)

  for j in [c for c in i]:
    if arr[0] == j:
      arr.popleft()
    if len(arr) == 0:
      break

  if len(arr) == 0:
    print(i)
    break