import sys

n, m = map(int, sys.stdin.readline().split())
li = []
dp = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = li[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
k = int(sys.stdin.readline())
for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])