import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
  arr.append(int(input()))

arr.sort(reverse=True)
tmp=0
for i in range(n):
  tmp = max(tmp , arr[i] * (i+1))
print(tmp)