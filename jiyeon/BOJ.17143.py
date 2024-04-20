#낚시왕

R,C,M = map(int,input().split())
shark_list =[]

for i in range(M):
    x= list(map(int,input().split()))  #(r,c),속력, 이동방향,크기
    shark_list.append([x[0]-1,x[1]-1]+x[2:])
    
width = [i for i in range(C)] + [i for i in range(C-2,0,-1)]
height = [i for i in range(R)] + [i for i in range(R-2,0,-1)]
lenW = len(width)
lenH = len(height)

shark = sorted(shark_list, key= lambda x:(x[1],x[0]))

answer =0

for i in range(C): #낚시꾼의 이동

    #상어 잡기
    for sk in shark:
        if sk[1]==i:
            answer +=sk[4]
            shark.remove(sk)
            break
    
    #상어 이동
    for j in range(len(shark)):
        x,y,s,d,z = shark[j]
        
        if d ==1 or d==2: #위아래 경우
            if d==1: dr = -1
            else: dr =1
            x = (x+s*dr)%lenH
            
            if x>=R-1:
                if d==1: d=2
                else: d=1
            shark[j] = [height[x],y,s,d,z]
            
        elif d ==3 or d==4: #오른 왼 경우
            if d==4: dr = -1
            else: dr =1
            y = (y+s*dr)%lenW
            
            if y>=C-1:
                if d==3: d=4
                else: d=3
            shark[j] = [x,width[y],s,d,z]

    shark.sort(key = lambda x :(x[0], x[1],-x[4]))

    
    for j in range(len(shark)-1,0,-1):
        if shark[j][0:2] == shark[j-1][0:2]:
            shark.pop(j)

            
#print(shark)
print(answer)