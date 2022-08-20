import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    queue = deque()
    cnt = 1
    visit = [[0 for _ in range(n)] for _ in range(n)]

    queue.append([a,b])
    visit[a][b] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0:
                if graph[nx][ny] == '1':
                    queue.append([nx,ny])
                    graph[nx][ny] = '0'
                    visit[nx][ny] +=1
                    cnt +=1
    return cnt

cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            ans.append(bfs(i,j))
            cnt +=1

print(cnt)
ans.sort()
for i in ans:
    print(i)