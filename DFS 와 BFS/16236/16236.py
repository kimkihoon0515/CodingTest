from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 2
            start = [i,j]


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    visit = [[0] * n for i in range(n)]
    visit[i][j] = 1
    eat = [] # 먹이 배열
    dist = [[0] * n for i in range(n)] # 먹이까지의 거리
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if graph[nx][ny] <= graph[i][j]: # 상어의 크기보다 탐색한 곳의 크기가 크지만 않으면 지나갈 수 있으므로 
                    q.append([nx, ny]) 
                    visit[nx][ny] = 1 # 방문한 것으로 바꾸고 거리를 갱신한다.
                    dist[nx][ny] = dist[x][y] + 1
                if graph[nx][ny] < graph[i][j] and graph[nx][ny] != 0: # 상어보다 물고기가 작고 물고기의 크기가 0이 아니면 먹이에 넣는다.
                    eat.append([nx, ny, dist[nx][ny]]) # 먹이의 좌표와 그곳 까지의 거리를 배열에 저장
    if not eat: # 먹을 수 있는 물고기가 없으면 -1 을 반환
        return -1, -1, -1
    eat.sort(key = lambda x : (x[2], x[0], x[1])) # 먹이를 거리 순으로 정렬한다. -> 가장 가까운 먹이 순으로 먹어야 하므로
    return eat[0][0], eat[0][1], eat[0][2] # x좌표,y좌표, 먹이까지의 거리를 반환

exp = 0 # 먹이를 몇마리 먹어야 상어가 커지는지
time = 0 # 먹이를 전부 먹는데 걸리는 시간
while True:
    i, j = start[0], start[1]
    ex, ey, dist = bfs(i, j)
    if ex == -1: 
        break # 먹이 못먹으면 그대로 0 출력
    graph[ex][ey] = graph[i][j] # 먹이를 먹고 상어의 위치를 갱신하고 원래 있던 곳을 0으로 만들어 준다.
    graph[i][j] = 0
    start = [ex, ey] # 상어의 새로운 위치가 시작점
    exp += 1 # 자신과 같은 크기의 물고기를 먹은 개수
    if exp == graph[ex][ey]: # 개수가 상어의 크기와 같으면 먹은 개수는 초기화하고 상어의 크기를 1 늘린다.
        exp = 0
        graph[ex][ey] += 1
    time += dist # 물고기 하나를 먹은 시간을 누적합으로 더해준다.
print(time)