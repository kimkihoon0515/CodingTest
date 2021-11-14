import sys
from collections import deque

m,n,k = map(int,sys.stdin.readline().split())

graph = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    a,b,c,d, = map(int,sys.stdin.readline().split())
    for i in range(b,d):
        for j in range(a,c):
            if graph[i][j] == 0:
                graph[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    graph[x][y] = 1
    s = 1 # 넓이

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append([nx,ny])
                s += 1 # 0을 계속 발견할 때마다 영역의 넓이를 1개씩 늘려준다.
    return s

result = []

cnt = 0 # 영역의 수
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt += 1
            result.append(bfs(i,j))

result.sort()
print(cnt)
print(*result)

