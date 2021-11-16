import sys
from collections import deque
from copy import deepcopy

n,m = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]



dx = [-1,1,0,0]
dy = [0,0,1,-1]

def count(x,y): # 빙산 주위로 0의 개수를 세는 함수
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            cnt += 1       
    return cnt

def bfs(x,y): # 빙산 덩어리를 확인
    queue = deque()
    queue.append([x,y])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[x][y] = 1

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if ice[nx][ny]!=0:
                    ice[nx][ny] = 0
                    visit[nx][ny] = 1
                    queue.append([nx,ny])

def check(): # 만약 얼음이 다 녹았으면 True 를 반환
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                return False
    return True

year = 0
while True:
    year += 1
    if check(): # 얼음이 다 녹으면 0을 출력한다.
        print(0)
        break

    ice = [[0 for _ in range(m)] for _ in range(n)] # 얼음이 녹고 나서 새롭게 저장되는 배열
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                melt = count(i,j)
                value = graph[i][j] - melt
                if value >= 0:
                    ice[i][j] = value
                else:
                    ice[i][j] = 0
    graph = deepcopy(ice) # 새로운 빙산 배열로 변경

    cnt = 0

    for i in range(n):
        for j in range(m):
            if ice[i][j] !=0: # 빙산의 개수를 파악해서 
                bfs(i,j)
                cnt +=1 
     
    if cnt >= 2: # 개수가 2개 이상이면 몇년만에 개수가 2개 이상으로 바뀌는지 출력
        print(year)
        break