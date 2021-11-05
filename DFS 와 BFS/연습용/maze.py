from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
li = []
for _ in range(n):
    li.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue = deque()
    queue.append((0,0)) # queue에 시작점 넣기
    while queue:
        x,y = queue.popleft() # 가장 먼저 들어온 순서대로 queue에서 나간다.
        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if li[nx][ny] == 1:
                    li[nx][ny] = li[x][y] + 1
                    queue.append((nx,ny))
                else:
                    continue
    return li[n-1][m-1] # 가장 마지막 까지의 최단 거리 반환

print(bfs())