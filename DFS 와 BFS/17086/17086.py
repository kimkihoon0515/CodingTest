import sys
from collections import deque

n, m = map(int, input().split())
graph = []


dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

queue = deque()
for i in range(n):
    temp = list(map(int, input().split()))
    for t in range(m):
        if temp[t] == 1:
            queue.append((i,t))
    graph.append(temp)

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
    return


bfs()
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, graph[i][j])

print(ans - 1)
