import sys
input = sys.stdin.readline

n=int(input())
test=[list(map(str,input().strip())) for _ in range(n)]

for arr in test:
  dx=[1,0,-1,0]
  dy=[0,1,0,-1]
  dir=1
  x,y=0,0
  max_xn, max_yn, min_xn, min_yn = 0,0,0,0

  for d in arr:
    if d=="F":
      x+=dx[dir]
      y+=dy[dir]

    if d=="B":
      x-=dx[dir]
      y-=dy[dir]

    if d=='L':
      if dir==3:
        dir=0
      else:
        dir+=1
    
    if d=='R':
      if dir==0:
        dir=3
      else:
        dir-=1

    max_xn = max(max_xn,x)
    max_yn = max(max_yn,y)
    min_xn = min(min_xn,x)
    min_yn = min(min_yn,y)

  print(abs(max_xn-min_xn)*abs(max_yn-min_yn))