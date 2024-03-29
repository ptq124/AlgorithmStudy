import sys
input = sys.stdin.readline

n=int(input())
rooms = [list(map(int,input().split())) for _ in range(n)]
rooms.sort(key=lambda x : (x[1], x[0]))

a = rooms[0]
cnt = 1
tmp = []
for i in range(1, n):
  if a[1] <= rooms[i][0]:
    a = rooms[i]
    cnt+=1

print(cnt)