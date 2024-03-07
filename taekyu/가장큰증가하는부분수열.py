import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp =[i for i in arr]

for i in range(1, n):
  for j in range(i):
    if arr[j] < arr[i]:
      dp[i] = max(dp[j]+arr[i], dp[i])
print(max(dp))