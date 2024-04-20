import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
idx=-1
for i in range(n-1,-1,-1):
  if arr[i-1] < arr[i]:
    idx = i-1
    break

if idx==-1:
  print(-1)
else:
  for i in range(n-1,-1,-1):
    if arr[i] > arr[idx]:
      idx1 = i
      break

  arr[idx], arr[idx1] = arr[idx1], arr[idx]

  arr=arr[:idx+1] + sorted(arr[idx+1:])

  print(*arr)