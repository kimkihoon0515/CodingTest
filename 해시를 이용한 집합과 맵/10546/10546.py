import sys


n = int(sys.stdin.readline().strip())

name = [sys.stdin.readline().strip() for _ in range(n)]

complete = [sys.stdin.readline().strip() for _ in range(n-1)]

n = {}
c = {}
for i in name:
    n[i] = n.get(i,0)+1

for i in complete:
    n[i] -= 1
    
print(n)


