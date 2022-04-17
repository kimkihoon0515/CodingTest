import sys

n = int(sys.stdin.readline().strip())

friend = [list(sys.stdin.readline().strip()) for _ in range(n)]

visit = [[0 for i in range(n)] for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            if friend[i][j] == 'Y' or (friend[i][k] == 'Y' and friend[k][j] == 'Y'):
                visit[i][j] = 1
                
ans = 0

for i in visit:
    ans = max(ans,sum(i))
print(ans)