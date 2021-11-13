import sys
from collections import deque

dx = [-1,1,-1,1,-1,1,0,0]
dy = [0,0,-1,1,1,-1,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])

    while queue:
        a,b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1: # 만약 육지라면 
                    graph[nx][ny] = 0 # 바다로 만든다.
                    queue.append([nx,ny])

while(True):
    w,h = map(int,sys.stdin.readline().split())
    cnt = 0
    if w == 0 and h == 0:
        exit(0)
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)



