import sys
from copy import deepcopy
from collections import deque

n,m = map(int,sys.stdin.readline().split())

li = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

cnt = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]


#print(graph)

def bfs():
    global cnt
    queue = deepcopy(li) # li의 배열을 복사해서 놓는다.
    result = 0
    virus = deque() # li에서 바이러스만 빼서 새로운 배열에 저장해놓는다.
    for i in range(n):
        for j in range(m):
            if queue[i][j] == 2:
                virus.append([i,j])

    while virus: # virus 증식
        x,y = virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <=ny < m:
                if queue[nx][ny] == 0:
                    queue[nx][ny] = 2
                    virus.append([nx,ny])
    for i in queue: # 안전지대 계산
        for j in i:
            if j == 0:
                result +=1
    cnt = max(cnt,result) # 안전지대 저장

def wall(wall_cnt): # 벽을 세우는 반복문
    if wall_cnt == 3: # 3개가되면 
        bfs() # bfs를 돌려서 안전지대를 계산한다
        return
    for i in range(n): # 그게아니면
        for j in range(m):
            if li[i][j] == 0: # 벽을 임의로 3개 세우고 bfs를 돌리는 것을 반복해서 가장 큰 값을 찾는다.
                li[i][j] = 1
                wall(wall_cnt+1)
                li[i][j] = 0
wall(0)
print(cnt)