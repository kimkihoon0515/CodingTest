import sys
from itertools import combinations

s = sys.stdin.readline().strip()    

ans = []
stack = []
index = []
start,end = 0,0

for i,value in enumerate(list(s)):
    if value == '(':
        stack.append(i)
    elif value == ')':
        start = stack.pop()
        end = i
        index.append([start,end])

for i in range(len(index)):
    comb = list(combinations(index,i+1))
    for j in range(len(comb)):
        tmp = list(s)
        for k in range(len(comb[j])):
            start,end = comb[j][k]
            tmp[start] = ''
            tmp[end] = ''
        ans.append(''.join(tmp))
ans = set(sorted(ans))
ans = sorted(list(ans))

for i in ans:
    print(i)