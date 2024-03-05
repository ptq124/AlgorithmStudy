import sys
input = sys.stdin.readline

n = int(input())
dp = []

for i in range(n):
    dp.append(int(input()))

d = [0] * n
d[0] = dp[0]

if n > 1:
    d[1] = dp[0]+dp[1]
if n > 2:
    d[2] = max(dp[2]+dp[1], dp[2]+dp[0], d[1])
for i in range(3, n):
    d[i] = max(d[i-1], d[i-3]+dp[i-1]+dp[i], d[i-2]+dp[i])

print(d[n-1])