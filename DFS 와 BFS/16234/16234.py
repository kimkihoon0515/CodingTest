from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, sys.stdin.readline().split())
s = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    temp = [] # 연합국
    temp.append([x, y])
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if l <= abs(s[nx][ny] - s[a][b]) <= r: # temp에 담을 조건
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    temp.append([nx, ny])
    return temp
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0 # 인구 이동이 발생하는 일수
while True:
    visit = [[0] * n for i in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                temp = bfs(i, j)
                if len(temp) > 1:
                    flag = True
                    num = sum([s[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        s[x][y] = num
    if not flag: # 이동이 없는 경우
        break
    cnt += 1
    
print(cnt)