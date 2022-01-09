import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [list(map(str,sys.stdin.readline().strip())) for _ in range(m)]

visit = [[0 for i in range(n)] for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    cnt = 1 # 인접한 병사의 수
    queue = deque()
    visit[a][b] = 1
    queue.append([a,b])
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                if graph[nx][ny] == graph[a][b]:
                    graph[nx][ny] = 0 # 탐색이 끝난 후에는 0으로 초기화
                    queue.append([nx,ny])
                    visit[nx][ny] = 1
                    cnt +=1 # 인접한 병사의 수를 하나씩 늘려간다.
    graph[a][b] = 0 # 탐색이 끝난 시작 지점도 역시 0으로 초기화
    return cnt

w_sum = 0 # w 병사의 위력
b_sum = 0 # b 병사의 위력

for i in range(m):
    for j in range(n):
        if graph[i][j] =='W':
            w_sum += bfs(i,j)**2
        elif graph[i][j] == 'B':
            b_sum += bfs(i,j)**2

print(w_sum,b_sum)