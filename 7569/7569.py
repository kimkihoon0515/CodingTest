import sys # 앞의 토마토와 비슷한 방법으로 푸는데 3차원이다.
from collections import deque
m,n,h = map(int,sys.stdin.readline().split())

li = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

queue = deque()

visit = [[[0 for _ in range(m)]for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if li[i][j][k] == 1 and visit[i][j][k] == 0:
                queue.append([i,j,k])
                visit[i][j][k] = 1

def bfs():
    while queue:
        a,b,c = queue.popleft()
        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if li[nx][ny][nz] == 0 and visit[nx][ny][nz] == 0:
                    queue.append([nx,ny,nz])
                    li[nx][ny][nz] = 1
                    visit[nx][ny][nz] = visit[a][b][c] + 1


bfs()
for i in li:
    for j in i:
        if 0 in j:
            print(-1)
            exit(0)
res = 0
for i in visit:
    for j in i:
        res = max(res,max(j))
print(res -1)