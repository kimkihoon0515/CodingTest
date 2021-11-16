import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

r,c,d = map(int,sys.stdin.readline().split()) # 좌표 (r,c) 방향 d

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

visit = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1,0,1,0] # 북,동,남,서
dy = [0,1,0,-1]
def bfs(r,c,d):
    queue = deque()
    queue.append([r,c,d])
    visit[r][c] = 1 # 현재 위치는 청소한 것으로 간주
    cnt = 1 # 청소하는 칸의 개수 현재위치를 청소했으므로 +1부터 시작

    while queue:
        x,y,z = queue.popleft()
        direction = z # 1이면 동쪽 2면 남쪽 3이면 서쪽 0이면 북쪽
        move = 0 # 움직일 수 있는지 여부 판단
        for _ in range(4):
            direction -= 1 
            if direction < 0: 
                direction = 3
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < n and 0<=ny < m and visit[nx][ny] == 0: # 움직이는 방향이 청소를 하지 않았다면
                if graph[nx][ny] == 0:
                    visit[nx][ny] = 1
                    move = 1
                    cnt += 1
                    queue.append([nx,ny,direction])
                    break
        
        if move == 1: # 청소를 했거나 벽인 경우
            continue
        else: # 방향 유지한 채로 한 칸 후진해준다.
            nx = x - dx[direction]
            ny = y - dy[direction]
            if 0<=nx < n and 0 <= ny < m and graph[nx][ny] == 0: 
                queue.append([nx,ny,direction])
    return cnt

print(bfs(r,c,d))
    



