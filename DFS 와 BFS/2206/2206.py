import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    visit = [[[0] * 2 for i in range(m)] for i in range(n)] # 탐색상태를 저장하기 위한 배열
    visit[0][0][1] = 1 
    while queue:
        x, y, z = queue.popleft() # 좌표와 벽을 부술 수 있는 횟수
        if x == n - 1 and y == m - 1: 
            return visit[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 아직 탐색안했다면
                if li[nx][ny] == 1 and z == 1: # 벽을 한 개 부순다.
                    visit[nx][ny][0] = visit[x][y][1] + 1 
                    queue.append([nx, ny, 0])
                elif li[nx][ny] == 0 and visit[nx][ny][z] == 0: # 빈 방이라면
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    queue.append([nx, ny, z])
    return -1
n, m = map(int, input().split())
li = []
for i in range(n):
    li.append(list(map(int, list(input().strip()))))
print(bfs())