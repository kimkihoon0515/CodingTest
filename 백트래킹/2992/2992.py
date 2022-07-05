import sys
from itertools import permutations

x = int(sys.stdin.readline().strip())

x = str(x)

li = list(permutations(x,len(x)))
result = []
for i in li:
    ans = int(''.join(i))
    if ans > int(x):
        result.append(ans)
if not result:
    print(0)
else:
    print(min(result))