import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,-1,1]
def dfs(x, y):
    if x == 0 and y == 0: # 가장 마지막방문할 곳을 1로 두고 
        return 1
    if dp[x][y] == -1: # 나머지를 0으로 둔다.
        dp[x][y] = 0
        for i in range(4): # x와 y가 움직일 수 있는 범위를 정해놓고 
            nx, ny = x + dx[i], y + dy[i] 
            if 0 <= nx < M and 0 <= ny < N: # 0 ~ m-1 0 ~ n-1동안
                if m[x][y] < m[nx][ny]: #원래 것보다 이동하려는 것이 크면 방문하지 않은 경로이므로 dfs + dp 수행
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]
 
M, N = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
print(dfs(M-1, N-1))