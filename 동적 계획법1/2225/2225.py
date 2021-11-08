import sys

n,k = map(int,sys.stdin.readline().split()) # 0부터 n까지 정수 k개를 더해서 n이 나오게하는것

li = []

for i in range(n+1):
    li.append(i)

dp = [[0 for _ in range(201)] for _ in range(201)]

for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i+1

for i in range(2,201):
    dp[i][1] = i
    for j in range(2,201):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] # 점화식 세우는 것이 중요함.

print(dp[k][n] % 1000000000)
