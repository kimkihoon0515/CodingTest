import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue = deque()
    queue.append([0,0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if graph[nx][ny] >= 1: # 인접한 칸이 치즈이면 1 증가 -> 격자 자리에 있는 치즈 찾는 것
                    graph[nx][ny] += 1
                else: # 공기칸일 경우
                    visit[nx][ny] = 1
                    queue.append([nx,ny])

result = 0 # 결과값

while True:
    bfs()
    #for i in range(n):
    #    print(graph[i])
    #print()
    cnt = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3: # 인접한 공기가 2개이상이므로 
                graph[i][j] = 0 # 치즈가 녹는다.
                cnt = 1
            if graph[i][j] == 2: # 인접한 공기가 1개이므로 
                graph[i][j] = 1 # 치즈 그대로 유지해줌
    
    if cnt == 1: # 치즈가 녹으면 시간을 증가시킨다.
        result += 1
    else:
        break
print(result)