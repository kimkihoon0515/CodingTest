import sys
from itertools import combinations

li = []
for i in range(9):
    n = int(sys.stdin.readline().strip())
    li.append(n)
a = list(combinations(li,2))
#print(a)
result = []
for i in a:
    if sum(i) == sum(li)- 100:
        result.append(i)
#print(result)
x = result[0][0]
y = result[0][1]

li.remove(x)
li.remove(y)
li.sort()
for i in li:
    print(i)