p,m=map(int,input().split())

dict = {}

for _ in range(p):
  l,n=input().split()
  check = False

  if len(dict)==0:
    dict[l+' '+n] = []
    dict[l+' '+n].append([l,n])
    check = True
    
  else:
    for key in dict.keys():
      if len(dict[key]) >= m:
        continue
      elif int(key.split(' ')[0])+10 >= int(l) and int(key.split(' ')[0])-10 <= int(l):
        dict[key].append([l,n])
        check = True
        break
  
  if not check:
    dict[l+' '+n] = []
    dict[l+' '+n].append([l,n])

for v in dict.values():
  v.sort(key=lambda x:x[1])
  if len(v) >= m:
    print('Started!')
    for i in v:
      print(str(i[0])+' '+str(i[1]))
  else:
    print('Waiting!')
    for i in v:
      print(str(i[0])+' '+str(i[1]))
