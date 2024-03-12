#가장 긴 감소하는 부분수열

import sys
input = sys.stdin.readline

a =int(input())
num = list(map(int,input().split()))
num = num[::-1]
dp=[1]*a

for i in range(a):
    for j in range(i):
        if num[i]>num[j] and dp[i]<dp[j]+1:
            dp[i]= dp[j]+1
            #print(dp)
print(max(dp))