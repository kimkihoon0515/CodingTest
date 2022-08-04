import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split()) 

graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

visit = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    visit[a][b] = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                if graph[nx][ny] == '1':
                    visit[nx][ny] = visit[x][y]+1
                    queue.append([nx,ny])
    
bfs(0,0)
print(visit[-1][-1])
