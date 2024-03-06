import sys
input = sys.stdin.readline

n=int(input())
dp = [list(map(int,input().split())) for _ in range(n)]

if n>1:
  dp[1][0]+=dp[0][0]
  dp[1][1]+=dp[0][0]

for i in range(2, n):
  for j in range(i+1):
    if j==0:
      dp[i][j]+=dp[i-1][0]
    elif j==i:
      dp[i][j]+=dp[i-1][j-1]
    else:
      dp[i][j] = max(dp[i][j]+dp[i-1][j-1], dp[i][j]+dp[i-1][j])

print(max(dp[n-1]))

