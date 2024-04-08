# 다음 순열
# 더 큰 값이 있는지 확인하여 변경

import sys
input = sys.stdin.readline

n= int(input())

x =list(map(int,input().split()))
lst =[]
flag=0

if x == [i for i in range(n,0,-1)]: #제일 큰 값이면 돌지 않기
    print("-1")
else:
    for i in range(n-1,0,-1):
        if x[i-1]<x[i]:
            for j in range(n-1,0,-1):
            #print(i,j)
                if x[i-1]<x[j]:
                    x[j],x[i-1] = x[i-1],x[j]
                    x= x[:i]+sorted(x[i:])
                    print(*x, sep =" ")
                    flag=1
                    break
        if flag==1:
            break
                