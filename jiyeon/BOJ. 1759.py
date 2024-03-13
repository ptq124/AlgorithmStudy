# 암호만들기(브루트 포스)

import itertools
import sys
input = sys.stdin.readline

L, C = map(int,input().split())
str_list =list(input().split())
consonant =[] #자음
vowel =[] #모음

for i in str_list:
    if i in ('a','e','i','o','u'):
        vowel.append(i)
    else:
        consonant.append(i)
result =[]
if len(vowel)>=1 and len(consonant)>=2:
    for i in range(1,len(vowel)+1):
        if L-i>=2:
            vowelComb = list(itertools.combinations(vowel,i))
            consonantComb = list(itertools.combinations(consonant,L-i))
            #print(vowelComb,consonantComb)
            for v in vowelComb:
                for c in consonantComb:
                    result.append("".join(sorted(v+c)))
            #print(result)
print(*sorted(result),sep="\n")