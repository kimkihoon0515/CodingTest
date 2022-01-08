import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(m)]

visit = [[0 for i in range(n)] for i in range(m)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    queue = deque()
    queue.append([i,j]) 
    visit[i][j] = 1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visit[nx][ny] = 1
                    queue.append([nx,ny])
    
    for i in range(n):
        if visit[m-1][i] == 1:
            return True
    return False

flag = False
for i in range(n):
    if graph[0][i] == 0: # 첫째줄만 검사해서 전류가 잘 통하는것부터 bfs를 돌린다.
        if bfs(0,i): # 하나라도 전류가 잘 통하면
            print('YES') 
            exit(0)
# 전류가 하나도 마지막 층까지 내려오지 않는다면 
print('NO')