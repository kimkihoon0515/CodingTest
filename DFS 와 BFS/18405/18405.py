import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
s,t_x,t_y = map(int,sys.stdin.readline().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

data = [] # 바이러스들의 정보를 저장하는 배열 
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append([graph[i][j],i,j,0])
data.sort()

queue = deque(data)
            
while queue:
    virus,x,y,t = queue.popleft()
    if t == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx<n and 0<=ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]= virus
                queue.append([virus,nx,ny,t+1])

print(graph[t_x-1][t_y-1])