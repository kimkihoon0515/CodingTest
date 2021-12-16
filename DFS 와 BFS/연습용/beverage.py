import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    queue = deque()
    visit= [[0 for i in range(m)] for _ in range(n)]
    queue.append([a,b])
    visit[a][b] = 1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append([nx,ny])
                    visit[nx][ny] = 1

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i,j)
            cnt +=1
print(cnt)