import sys
n = int(sys.stdin.readline())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)] # 0 은 가로 1 은 대각선 2는 세로
"""
가로는 대각선과 가로만 가능
세로는 대각선과 세로만 가능
대각선은 가로 세로 대각선 전부 가능
점화식 
"""

dp[0][0][1] = 1


for i in range(2,n): # 맨 첫 번째 줄은 계속 가로로 밖에 놓지 못한다.
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

#print(dp)

for i in range(1,n):
    for j in range(2,n):
        if graph[i][j] == 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1] # 대각선

        if graph[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1] # 가로
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j] # 세로


result = 0
for i in range(3): # 가로 세로 대각선을 전부 합한 것이 결과값
    result += dp[i][n-1][n-1]
print(result) 