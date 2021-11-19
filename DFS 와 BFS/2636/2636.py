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
    cnt = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0: 
                if graph[nx][ny] == 0: # 공기라면 방문했고 queue에 넣어준다.
                    visit[nx][ny] = 1
                    queue.append([nx,ny])
                elif graph[nx][ny] == 1: # 만약 치즈라면 없애고 없어진 넓이를 cnt에 저장한다.
                    visit[nx][ny] = 1
                    graph[nx][ny] = 0
                    cnt += 1
    return cnt

result = [] # 매 탐색마다 사라지는 치즈의 넓이가 저장되는 배열
time = 0 # 치즈가 녹는데 걸리는 시간 즉 탐색하는 시간
 
while True:
    cnt = bfs() 
    result.append(cnt) 
    if cnt == 0: # 치즈가 다 사라지면 종료한다.
        break
    time += 1 # 치즈를 다 녹이는데 걸리는 시간
print(time)
print(result[-2]) # 치즈가 매 순간 녹는데 마지막에 다 녹기 직전의 치즈의 넓이