
k,n= map(int,input().split())
arr=[]
for i in range(k):
    arr.append(int(input()))
    
start =1
end = max(arr)

while start <=end:
    mid = (start+end)//2
    result =0
    
    for i in arr:
        result += i//mid
        
    if result >= n:
        start = mid+1
    else:
        end = mid-1
        
print(start)