import sys
input = sys.stdin.readline

n, m=map(int,input().split())

arr = [input().strip() for _ in range(n)]

dict = {}
for i in arr:
  if len(i)<m:
    continue
  if i in dict:
    dict[i][0]+=1  
  else:
    dict[i] = [1, len(i)]

a = []
for key, v in dict.items():
  a.append([key, v[0], v[1]])

a.sort(key=lambda x:(-x[1], -x[2], x[0]))

for i in a:
  print(i[0])