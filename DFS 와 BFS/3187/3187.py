from collections import deque
import sys


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    wolf, sheep = 0, 0
    while q:
        x, y = q.popleft()
        if a[x][y] == 'v':
            wolf += 1
        elif a[x][y] == 'k':
            sheep += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if a[nx][ny] != '#' and not c[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])

    if wolf >= sheep:
        sheep = 0
    else:
        wolf = 0
    return [wolf, sheep]

m, n = map(int, input().split())
a = [list(input().strip()) for _ in range(m)]
c = [[0]*n for _ in range(m)]
q = deque()

v, k = 0, 0
for i in range(m):
    for j in range(n):
        if a[i][j] != '#' and not c[i][j]:
            wolf, sheep = bfs(i, j)
            v += wolf; k += sheep
print(k, v)