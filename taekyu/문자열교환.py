import math
s = input()
count  = s.count('a')
s += s[:count-1]
tmp = math.inf

for i in range(len(s) - (count-1)):
  tmp=min(s[i:i+count].count('b'), tmp)

print(tmp)