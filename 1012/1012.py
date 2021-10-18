import sys

t = int(sys.stdin.readline())

dx = [0,0,1,-1] # x축 방향
dy = [1,-1,0,0] # y축 방향

def bfs(x,y):
    queue = [[x,y]] # [x.y] 형태의 queue 배열을 만들고 bfs 형식으로 탐색
    while queue:
        a,b = queue[0][0],queue[0][1] # a,b를 각각 queue의 x와 y좌표로 호출한다.
        del queue[0]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx <n and 0 <= ny < m and li[nx][ny] == 1: # 만약 범위 내에 있으면서 배추가 심어져있으면
                li[nx][ny] = 0 # 탐색했다는 뜻으로 0으로 만들고 
                queue.append([nx,ny]) # queue에 추가한다. 그러한 과정을 반복한다.

for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    li = [[0 for _ in range(m)]for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        li[y][x] = 1
    for i in range(n):
        for j in range(m):
            if li[i][j] == 1:
                bfs(i,j)
                li[i][j] = 0
                cnt +=1
    print(cnt)
