# 가장 큰 증가하는 부분 수열
import sys
input = sys.stdin.readline

a =int(input())
num = list(map(int,input().split()))

dp = num[:]

#print(dp,dp_list)

for i in range(a):
    for j in range(i):
        if num[i]>num[j]:
            dp[i] = max(dp[i], dp[j]+num[i])
            #print(dp)
print(max(dp))
