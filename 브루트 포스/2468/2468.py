import sys
from collections import deque


n = int(sys.stdin.readline())

li = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]


for _ in range(n):
    li.append(list(map(int,sys.stdin.readline().split())))

def bfs(x,y,h):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 1

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <=ny < n:
                if li[nx][ny] > h and visited[nx][ny] == 0: # 물의 높이보다 그래프가 크고 아직 탐색안한곳이라면
                    visited[nx][ny] = 1 # 탐색했다고 바꾸고 queue에 넣는다.
                    queue.append([nx,ny])

max_h = max(max(li)) # 그래프중 최대 길이
result = [] # 결과값

for k in range(max_h+1):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if li[i][j] > k and visited[i][j] ==0: # 공간을 발견하는 조건 
                bfs(i,j,k)
                cnt +=1 # 공간 수 1 증가
    result.append(cnt)

print(max(result)) # 가장 큰 공간의 수를 출력

