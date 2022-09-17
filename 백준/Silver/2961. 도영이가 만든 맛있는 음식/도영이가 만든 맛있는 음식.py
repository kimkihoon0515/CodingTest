import sys
from itertools import combinations

n = int(sys.stdin.readline())

li = [list(map(int, input().split())) for _ in range(n)]
combi = [combinations(li,i) for i in range(1,n+1)]
ans = sys.maxsize

for i in combi:
    for j in i:
        s,b = 1,0
        for k,l in j:
            s*=k
            b+=l
        ans = min(ans,abs(s-b))
print(ans)