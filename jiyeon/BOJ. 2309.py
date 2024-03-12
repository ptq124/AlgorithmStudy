#일곱 난쟁이 (브루트포스)

import itertools
import sys
input = sys.stdin.readline

heights = []
for i in range(9):
    heights.append(int(input()))

a= list(itertools.combinations(heights, 7))

for i in a:
    if sum(i)==100:
        answer = i
        break

answer = sorted(list(answer))
print(*answer, sep='\n')