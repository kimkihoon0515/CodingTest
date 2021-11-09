import sys

n = int(sys.stdin.readline())

dp = [0] * 31

dp[0] = 1

for i in range(2,n+1,2):
    dp[i] = dp[i-2] * 3
    for j in range(0,i-2,2):
        dp[i] += dp[j] * 2

print(dp[n])