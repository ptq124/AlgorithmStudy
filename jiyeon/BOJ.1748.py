# 수 이어쓰기1

n = input().rstrip()
a= [9,90,900,9000,90000,900000,9000000,90000000]

length = len(n)
n = int(n)
i=1
answer =0

for i in range(1, length+1):
    if i==length:
        answer += (n-(10**(i-1))+1) * i
    else:
        answer += a[i-1]*i
print(answer)
 