import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
li = [list(map(str,input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[x][y] = 1
    cnt = 0
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if li[nx][ny] == 'L' and dp[nx][ny] == 0:
                    dp[nx][ny] = dp[a][b] + 1
                    cnt = max(cnt,dp[nx][ny])
                    queue.append([nx,ny])
    return cnt

result = [] # 결과값을 저장하는 배열

for i in range(n):
    for j in range(m):
        if li[i][j] =='L':
            result.append(bfs(i,j))
print(max(result)-1) # 결과값중 가장 큰 값 -1
