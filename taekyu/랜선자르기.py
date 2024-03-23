k, n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
#[802,743,457,539]
start = 1
end = max(arr)

while start <= end:
  mid = (start+end)//2
  a=0

  for i in arr:
    a = a + (i // mid)
  
  if n <= a:
    start = mid+1
  else:
    end = mid-1
  

print(end)
