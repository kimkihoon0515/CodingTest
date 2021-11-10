import sys
from itertools import permutations
n = int(sys.stdin.readline())

li = [i for i in range(1,n+1)]

result = list(permutations(li,n))
for i in range(len(result)):
    print(*result[i])
    