import sys
from collections import deque

n = int(sys.stdin.readline())

graph=[[0 for i in range(n)] for _ in range(n)]

r1,c1,r2,c2 = map(int,sys.stdin.readline().split())

dx = [-2,-2,2,2,0,0]
dy = [1,-1,1,-1,2,-2]

visit = [[0 for _ in range(n)] for _ in range(n)]

def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    visit[i][j] = 1

    while queue:
        x,y = queue.popleft()
        if x == r2 and y == c2:
            return visit[x][y]-1 # 시작부터 1을 집어넣었으므로 이동횟수는 -1을 해서 출력

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y]+1 # 이동횟수를 하나씩 추가한다.
                queue.append([nx,ny])
    return -1 # 도착못하면 -1을 출력한다.

print(bfs(r1,c1))


