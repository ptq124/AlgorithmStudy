import sys
input=sys.stdin.readline

R,C,M = map(int,input().split())
shark=[]
for _ in range(M):
  r,c,s,d,z = list(map(int,input().split()))
  shark.append([r-1,c-1,s,d,z])

W=2*C-2
H=2*R-2
wt=[i for i in range(C)] + [i for i in range(C-2,0,-1)] 
ht=[i for i in range(R)] + [i for i in range(R-2,0,-1)] 
ans=0

shark.sort(key=lambda x:(x[1],x[0]))
# 낚시왕이 오른쪽으로 한 칸 이동한다.
for j in range(C):
  # 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
  for i in range(len(shark)):
    if shark[i][1] == j:
      ans+=shark[i][4]
      shark.pop(i)
      break

  # 상어가 이동한다.
  for i in range(len(shark)):
    r, c, s, d, z = shark[i]

    if d==3 or d==4:
      # (현재 좌표 + 스피드 * +-1) % 전체길이
      if d==3:
        dr=1
      else:
        dr=-1
      c=(c+s*dr)%W
      if C<=c:
        c=wt[c]
        if d==3: # 방향전환
          d=4
        else:
          d=3
    else:
      # (현재 좌표 + 스피드 * +-1) % 전체길이
      if d==2:
        dr=1
      else:
        dr=-1
      r=(r+s*dr)%H
      if R<=r:
        r=ht[r]
        if d==2: # 방향전환
          d=1
        else:
          d=2
    shark[i] = [r,c,s,d,z]

  shark.sort(key=lambda x:(x[0],x[1],-x[4]))
  # 같은 칸인 상어 비교
  for i in range(len(shark)-1,0,-1):
    if shark[i][:2] == shark[i-1][:2]:
      shark.pop(i)
  
print(ans)