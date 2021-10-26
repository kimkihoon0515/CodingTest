import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())

li = []

for _ in range(n): # 토마토가 들어있는 공간
    li.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = deque() # 시간복잡도가 O(1)인 deque 사용
for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            queue.append([i,j])
def bfs(): # bfs 방식으로 토마토가 있는 위치 탐색
    while queue:
        a,b = queue.popleft() 
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and li[nx][ny] == 0: # 토마토가 익으면 1을 더해주고 횟수를 센다.
                li[nx][ny] = li[a][b] + 1
                queue.append([nx,ny])

bfs()
maximum = 0
for i in li:
    for j in i:
        if j == 0: # 모든 토마토를 익히지 못했다면 -1을 출력하고 종료.
            print(-1)
            exit(0)
    maximum = max(maximum,max(i))
print(maximum -1)