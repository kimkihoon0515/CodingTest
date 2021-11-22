import sys
from collections import deque

r,c = map(int,sys.stdin.readline().split())
graph = [list(map(str,input())) for _ in range(r)] # . : 빈 곳, # : 울타리, o : 양, v : 늑대
visit = [[0 for _ in range(c)] for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    global wolf,sheep
    queue = deque()
    queue.append([i,j])
    visit[i][j] = 1
    w,s = 0,0

    while queue:
        x,y = queue.popleft()
        if graph[x][y] == 'v': # 구간을 탐색해서 늑대의 개수를 세어줌
            w += 1
        if graph[x][y] == 'o': # 구간을 탐색해서 양의 개수를 세어줌
            s += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0:
                if graph[nx][ny] != '#': # 울타리가 아니면 계속해서 탐색
                    visit[nx][ny] = 1
                    queue.append([nx,ny])
    if w < s: # 구간을 탐색했는데 양이 늑대보다많으면
        wolf -= w # 늑대를 쫓아냄
    else: # 늑대가 많으면
        sheep -= s # 양이 전부 잡아 먹힘
wolf = 0
sheep = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'v': # 늑대의 전체 마리수
            wolf += 1
        elif graph[i][j] == 'o': # 양의 전체 마리수
            sheep += 1

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'o' or graph[i][j] == 'v': # 양이나 늑대이고 탐색을 안했다면
            if visit[i][j] == 0:
                visit[i][j] = 1
                bfs(i,j) # 그 점을 기점으로 탐색해준다.
print(sheep,wolf) 