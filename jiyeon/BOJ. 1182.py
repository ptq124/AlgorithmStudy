# 부분수열의 합

n,s = map(int,input().split())
lst = list(map(int,input().split()))
flag=0

def backtracking(sum_lst,c):
    global flag
    #print(sum_lst,flag)
    if sum(sum_lst)==s and sum_lst:
        #print(sum_lst)
        flag+=1
    for i in range(c,n):
        backtracking(sum_lst+[lst[i]],i+1)

backtracking([],0)
print(flag)