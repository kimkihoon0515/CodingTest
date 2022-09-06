import sys
from collections import deque

t = int(sys.stdin.readline())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    visit[i][j] = 1
    queue = deque()
    queue.append([i,j])

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <=ny<w and visit[nx][ny] == 0:
                if graph[nx][ny] == '#':
                    queue.append([nx,ny])
                    visit[nx][ny] = 1
                    graph[nx][ny] = '.'


for _ in range(t):
    h,w = map(int,sys.stdin.readline().split())
    graph = [list(sys.stdin.readline().strip()) for _ in range(h)]
    cnt = 0
    visit = [[0 for i in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#' and visit[i][j] == 0:
                bfs(i,j)
                cnt+=1
    print(cnt)