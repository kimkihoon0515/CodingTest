import sys

s = sys.stdin.readline().strip()    
n = int(sys.stdin.readline())

cnt = 0
for _ in range(n):
    ring = sys.stdin.readline().strip()

    if s in ring*2:
        cnt+=1
print(cnt)