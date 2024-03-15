#덩치
# 브루트포스

import sys
input = sys.stdin.readline

n= int(input())
people = []
rank ={}

for i in range(n):
    people.append(list(map(int,input().split())))
    #print(people)
    rank[i] = 1

for i in range(n):
    for j in range(n):
        if i!=j and people[i][0]<people[j][0] and people[i][1]<people[j][1] :
            rank[i] +=1
            #print(rank)
print(*list(rank.values()))