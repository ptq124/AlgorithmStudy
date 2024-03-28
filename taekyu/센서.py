import sys
input = sys.stdin.readline

n=int(input())
k=int(input())
arr=list(map(int,input().split()))
tmp=[]

if k>=n:
  print(0)
  sys.exit()

arr.sort()

for i in range(0, n-1):
  tmp.append(arr[i+1]-arr[i])

tmp.sort(reverse=True)
for _ in range(k-1):
  tmp.pop(0)

print(sum(tmp))


