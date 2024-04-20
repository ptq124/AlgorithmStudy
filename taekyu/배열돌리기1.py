import sys
input=sys.stdin.readline
from collections import deque

n,m,r=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
new_arr=[[0]*m for _ in range(n)]

a=deque()

loops = min(n,m)//2

for i in range(0,loops):
  a.clear()
  for j in range(i, n-i):
    a.append(arr[j][i])
  for j in range(i+1, m-i):
    a.append(arr[n-i-1][j])
  for j in range(n-i-2, i-1,-1):
    a.append(arr[j][m-i-1])
  for j in range(m-i-2, i, -1):
    a.append(arr[i][j])

  a.rotate(r)

  for j in range(i, n-i):
    new_arr[j][i]=a.popleft()
  for j in range(i+1, m-i):
    new_arr[n-i-1][j]=a.popleft()
  for j in range(n-i-2, i-1,-1):
    new_arr[j][m-i-1] = a.popleft()
  for j in range(m-i-2, i, -1):
    new_arr[i][j]=a.popleft()

for i in new_arr:
  print(*i)