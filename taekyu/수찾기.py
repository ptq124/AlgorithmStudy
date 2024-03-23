import sys
input = sys.stdin.readline

n=int(input())
arr = list(map(int,input().split()))
m=int(input())
numbers = list(map(int,input().split()))

arr.sort()

def binary_search(arr, find_num):
  L=0
  R=len(arr)-1

  while L<=R:
    pivot = (L+R)//2

    if arr[pivot] < find_num:
      L=pivot+1
    elif arr[pivot] > find_num:
      R=pivot-1
    else:
      return True
  return False

for num in numbers:
  if binary_search(arr, num):
    print(1)
  else:
    print(0)