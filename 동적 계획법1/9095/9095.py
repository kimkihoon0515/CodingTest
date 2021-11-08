import sys

t = int(sys.stdin.readline())

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(t):
    n = int(sys.stdin.readline())
    for i in range(4,n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])
