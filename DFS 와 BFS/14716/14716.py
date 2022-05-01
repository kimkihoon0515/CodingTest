import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

dx = [-1,-1,-1,0,0,0,1,1,1]
dy = [1,0,-1,1,0,-1,1,0,-1]

visit = [[0 for _ in range(n)] for _ in range(m)]

def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    visit[i][j] = 1
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    visit[nx][ny] = 1
                    queue.append([nx,ny])

cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and visit[i][j] == 0:
            bfs(i,j)
            cnt += 1
            
print(cnt) 