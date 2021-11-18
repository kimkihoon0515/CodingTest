import sys
from collections import deque

n,m,k = map(int,sys.stdin.readline().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    a,b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1

dx = [-1,1,0,0]
dy = [0,0,1,-1]

visit = [[0 for _ in range(m)] for _ in range(n)]

def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    visit[i][j] = 1
    sum = 1 # 넓이
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    visit[nx][ny] = 1
                    queue.append([nx,ny])
                    sum += 1
    return sum

result = 0 # 최대값 저장하는 변수
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visit[i][j] == 0:
            result = max(result,bfs(i,j)) # 최대값 
print(result)