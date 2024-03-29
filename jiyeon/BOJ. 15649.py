#N과 M(1)

from itertools import *
import sys
input= sys.stdin.readline

n,m = map(int,input().split())

per = permutations([i for i in range(1,n+1)],m)

for i in per:
    print(*i, sep=" ")