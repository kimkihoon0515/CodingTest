import sys
from collections import deque

r,c = map(int,sys.stdin.readline().split())

li = [list(map(str,input())) for _ in range(r)] # . : 비어있는 곳, * : 물이 차 있는 곳, X : 돌, D : 비버의 굴, S : 고슴도치 위치

visit = [[0 for _ in range(c)] for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
water = deque()

for i in range(r):
    for j in range(c):
        if li[i][j] == 'S': # 시작지점
            x,y = i,j
            li[i][j] = '.' # 비워준다
        elif li[i][j] == '*': # 빈 지점이 있으면 
            water.append([i,j]) # 물 배열에 넣어줌

def wat():
    length = len(water)
    while length:
        x,y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c :
                if li[nx][ny] == '.': # 비어있으면 물로바꿔준다.
                    li[nx][ny] = '*'
                    water.append([nx,ny])
        length -= 1

def bfs(x,y):
    queue.append([x,y])
    visit[x][y] = 1
    while queue:
        queue_len = len(queue)
        while queue_len:
            a,b = queue.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0:
                    if li[nx][ny] == '.':
                        visit[nx][ny] = visit[a][b] + 1 # 비버가 움직인 횟수를 저장해놓는다.
                        queue.append([nx,ny])
                    elif li[nx][ny] == 'D':
                        print(visit[a][b]) # 도착하면 그 횟수 출력
                        return
            queue_len -= 1
        wat()

    print('KAKTUS') # 못 가면 출력
    return

wat()
bfs(x,y)
