import sys

n,m = map(int,sys.stdin.readline().split())

dp = [[0 for i in range(n+1)] for _ in range(n+1)]

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = (dp[i][j+1]+ dp[i+1][j] - dp[i][j]) + graph[i][j] # dp에 합을 계산해서 저장해놓는다.

for i in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    print(dp[x2][y2] -(dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]))