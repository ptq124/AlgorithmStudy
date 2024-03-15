def dfs(home,away):
  global tmp
  global game

  if away==6:
    home+=1
    away=home+1

  if home==5:
    if game==[ [0,0,0] for _ in range(6) ]:
      tmp = 1
    return

  if game[home][0] > 0 and game[away][2] > 0:
    game[home][0], game[away][2] = game[home][0]-1, game[away][2]-1
    dfs(home,away+1)
    game[home][0], game[away][2] = game[home][0]+1, game[away][2]+1

  if game[home][2] > 0 and game[away][0] > 0:
    game[home][2], game[away][0] = game[home][2] - 1, game[away][0]-1
    dfs(home, away+1)
    game[home][2], game[away][0] = game[home][2] + 1, game[away][0]+1
  
  if game[home][1] >0 and game[away][1] > 0:
    game[home][1], game[away][1] = game[home][1] - 1, game[away][1]-1  
    dfs(home,away+1)  
    game[home][1], game[away][1] = game[home][1] + 1, game[away][1]+1  

for _ in range(4):
  arr = list(map(int,input().split()))
  game = []

  for i in range(6):
    game.append([arr[i*3],arr[(i*3)+1],arr[(i*3)+2]])

  tmp = 0
  dfs(0,1)
  print(tmp,end=" ")