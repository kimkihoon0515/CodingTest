import sys

n = int(sys.stdin.readline())

dp = [0] * 91

dp[1] = 1
dp[2] = 1
for i in range(3,n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])