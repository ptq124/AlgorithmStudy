import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]

for i in range(8):
    for j in range(i + 1, 9):
        if sum(arr) - arr[i] - arr[j] == 100:
            arr.pop(j)
            arr.pop(i)
            break
    if len(arr) == 7:  
        break

arr.sort()

for num in arr:
    print(num)
