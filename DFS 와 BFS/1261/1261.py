import sys
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

m,n = map(int,sys.stdin.readline().split()) # 가로 세로 헷갈리지말기
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
visit = [[-1 for i in range(m)] for _ in range(n)] # 벽을 부수는 개수

def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    visit[a][b] = 0
    
    while queue:
        x,y = queue.popleft() 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == -1:
                if graph[nx][ny] == 0: # 벽이없다면
                    visit[nx][ny] = visit[x][y] # 부순 벽의 개수는 그대로
                    queue.appendleft([nx,ny]) # queue의 가장 앞으로 들어가서 거기서부터 다시 탐색하도록 -> 벽을 부수는 개수가 최소가 되도록 탐색
                else: # 벽이 있다면
                    visit[nx][ny] = visit[x][y]+1 # 부순 벽의 개수를 1 증가 
                    queue.append([nx,ny])
    return visit[-1][-1]

print(bfs(0,0))



                    