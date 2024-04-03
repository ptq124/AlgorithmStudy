#카잉 달력

# if x<M : x' =x+1
# if y<N : y' = y+1 else y'=1

import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    m,n,x,y =map(int,input().split())
    K = x

    while K <= m * n:
        if (K - x) % m == 0 and (K - y) % n == 0:
            print(K)
            break
        K += m
    else:
        print("-1")