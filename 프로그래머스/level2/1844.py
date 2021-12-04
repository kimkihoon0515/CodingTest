from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(maps):
    n = len(maps) # 세로 
    m = len(maps[0]) # 가로

    queue = deque()
    queue.append([0,0])
    visit = [[0 for _ in range(m)] for i in range(n)]
    visit[0][0] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if maps[nx][ny] == 1:
                    queue.append([nx,ny])
                    visit[nx][ny] = visit[x][y] + 1
    return visit[-1][-1]

def solution(maps):
    if bfs(maps) == 0:
        return -1
    else:
        return bfs(maps)