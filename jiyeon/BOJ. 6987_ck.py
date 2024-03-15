#월드컵
#아직 해결안됨!!!

from itertools import *
import sys
input = sys.stdin.readline

vs = list(combinations([0,1,2,3,4,5],2))
result =[]

for i in range(4):
    x= list(map(int,input().split()))
    win = x[::3]
    tie = x[1::3]
    lose =x[2::3]
    flag=1
    #print(win, tie, lose)

    for j in vs:
        if win[j[0]]>0 and lose[j[1]]>0: #승 패
            win[j[0]]-=1
            lose[j[1]]-=1
        elif tie[j[0]]>0 and tie[j[1]]>0: #무 무
            tie[j[1]]-=1
            tie[j[0]]-=1
        elif lose[j[0]]>0 and win[j[1]]>0: #lose[[j[0]]>0 패 승
            lose[j[0]]-=1
            win[j[1]]-=1
        else:
            flag =0

        #print(j, win,tie,lose)

    result.append(flag)

print(*result)