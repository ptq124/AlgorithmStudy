import sys

n = int(sys.stdin.readline())
dp = []
for _ in range(n):
  dp.append(list(map(int,sys.stdin.readline().strip().split())))

for i in range(1,n):
  dp[i][0] = min(dp[i-1][1],dp[i-1][2])+dp[i][0]
  dp[i][1] = min(dp[i-1][0],dp[i-1][2])+dp[i][1]
  dp[i][2] = min(dp[i-1][0],dp[i-1][1])+dp[i][2]

print(min(dp[n-1]))