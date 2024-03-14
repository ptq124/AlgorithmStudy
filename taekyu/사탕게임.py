import sys
input = sys.stdin.readline

n=int(input())
arr = [list(map(str,input().rstrip('\n'))) for _ in range(n)]

def check(arr):
  max_cnt = 1
  for i in range(n):
    cnt = 1
    for j in range(1,n):
      if arr[i][j] == arr[i][j-1]:
        cnt+=1
      else:
        cnt = 1
      max_cnt = max(cnt,max_cnt)
    cnt=1
    for j in range(1,n):
      if arr[j][i] == arr[j-1][i]:
        cnt+=1
      else:
        cnt=1
      max_cnt = max(cnt,max_cnt)
  return max_cnt

max_cnt = 0

for i in range(n):
  for j in range(1, n):
    arr[i][j-1], arr[i][j] = arr[i][j], arr[i][j-1] 
    max_cnt = max(check(arr), max_cnt)
    arr[i][j-1], arr[i][j] = arr[i][j], arr[i][j-1] 

for i in range(n):
  for j in range(1,n):
    arr[j-1][i], arr[j][i] = arr[j][i], arr[j-1][i] 
    max_cnt = max(check(arr), max_cnt)
    arr[j-1][i], arr[j][i] = arr[j][i], arr[j-1][i] 

print(max_cnt)
