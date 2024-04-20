import sys
input = sys.stdin.readline
h,w=map(int,input().split())
arr=list(map(int,input().split()))

ans=0
for i in range(1,len(arr)-1):
  left=max(arr[:i])
  right=max(arr[i+1:])
  p=min(left,right)
  if p > arr[i]:
    ans+=p-arr[i]
print(ans)