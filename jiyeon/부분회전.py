arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
sx, sy = 2, 2
length = 3

small_arr = [[0]*length for _ in range(length)]

  
for x in range(sx,sx+length):
    for y in range(sy, sy+length):
        ox =x-sx # 0,0을 기준점으로 한 값을 만들기
        oy =y-sy
        small_arr[ox][oy] = arr[y][sx+length-1-ox]
        
print(small_arr)  

for x in range(sx,sx+length):
    for y in range(sy,sy+length):
        arr[x][y] = small_arr[x-sx][y-sy]

print(*arr,sep="\n")


# small_sq = [[0]*length for _ in range(length)]
# print(small_sq)

# for i in range(sy,sy+length):
#     for j in range(sx, sx+length):
#         small_sq[i-sy][j-sx] = arr[sx+length -j+(sx-1)][i]
        
# for i in range(sx,sx+length):
#     for j in range(sy,sy+length):
#         arr[i][j] = small_sq[i-sx][j-sy]
# print(*arr,sep="\n")