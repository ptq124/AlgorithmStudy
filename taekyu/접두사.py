n=int(input())
arr=[input() for _ in range(n)]

# 방법 1

arr.sort(key=lambda x:(x, len(x)))
ans=[]
while True:
  if not arr:
    break
  s=arr.pop(0)
  for i in arr:
    if s in i[:len(s)]:
      break
  else:
    ans.append(s)

print(len(ans))

# 방법 2

# arr.sort(key=len)
# ans=[]
# for i in range(n):
#   x=arr[i]
#   flag=True
#   for j in arr[i+1:]:
#     if x in j[:len(x)]:
#       flag=False
#       break
#   if flag:
#     ans.append(x)
# print(ans)