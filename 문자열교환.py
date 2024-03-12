import math
s = input()
count  = s.count('a')

s += s[:count-1]
tmp = math.inf

for i in range(len(s) - (count-1)):
  tmp=min(s[i:i+8].count('b'), tmp)

print(tmp)