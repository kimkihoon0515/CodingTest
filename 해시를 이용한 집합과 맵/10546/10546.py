import sys


n = int(sys.stdin.readline().strip())

name = [sys.stdin.readline().strip() for _ in range(n)]

complete = [sys.stdin.readline().strip() for _ in range(n-1)]

n = {}

for i in name:
    n[i] = n.get(i,0)+1

for i in complete:
    n[i] -= 1
    
ans = [k for k,v in n.items() if v ==1]
print(ans[0])


