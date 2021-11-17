import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

visit = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visit[x][y] = 1
    sum = 1 # 그림의 넓이

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0<= ny < m and visit[nx][ny] == 0: # 방문하지 않고 1로 연결되어 있으면 방문했다고 바꾼다.
                if graph[nx][ny] == 1:
                    visit[nx][ny] = 1
                    queue.append([nx,ny])
                    sum +=1 
    return sum # bfs 한번 돌때마다 구해지는 그림의 넓이 반환

cnt = 0 # 그림 개수
result = 0 # 영역 넓이들 중 최대값
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and graph[i][j] == 1: # 방문하지 않았고 그림이라면
            cnt += 1 # 그림의 개수를 하나늘리고 영역의 넓이의 최대값을 저장한다.
            result = max(result,bfs(i,j))

print(cnt,result)        

                

