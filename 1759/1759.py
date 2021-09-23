from itertools import combinations
l,c = map(int,input().split())
word = sorted(list(map(str,input().split())))
result =[]
result.extend(list(map(''.join,combinations(map(str,word),l))))
print(result)
moum = ['a','e','o','u','i']

for i in result:
    vows = 0
    coms = 0
    for j in i:
        if j in moum:
            vows +=1
        else:
            coms +=1
    if vows >=2 and coms >=1:
        print(i)