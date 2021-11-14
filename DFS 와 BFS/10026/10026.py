import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(map(str,input())) for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visit[x][y] = 1

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[a][b] and visit[nx][ny] == 0:
                    queue.append([nx,ny])
                    visit[nx][ny] = 1
cnt = 0 # 정상인 구간

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i,j)
            cnt +=1

cnt1 = 0 # 색맹 구간

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R': # 적록색맹이면 R을 G로 바꿔준다.
            graph[i][j] = 'G'

visit = [[0 for _ in range(n)] for _ in range(n)] # 다시 탐색하기 위해 visit 행렬을 초기화해준다.      
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i,j)
            cnt1+=1

print(cnt,cnt1)