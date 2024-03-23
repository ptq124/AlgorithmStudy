n=int(input())
m=int(input())
arr=list(input().split())

ans = abs(100-n)

for i in range(1000001):
  for j in str(i):
    if j in arr:
      break
  else:
    ans = min(ans, len(str(i)) + abs(i-n))
print(ans)