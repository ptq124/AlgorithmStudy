import sys
input = sys.stdin.readline
n= int(input())
house =[]
for i in range(n):
    x= list(map(int,input().split(" ")))
    house.append(x)
#print(house)
dp=[ [0,0,0] for _ in range(n)]
for i in range(3):
    dp[0][i] = house[0][i]

for i in range(1,n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + house[i][0];
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + house[i][1];
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + house[i][2];

print(min(dp[n-1]))