import sys

n = int(sys.stdin.readline())

dp = [1 for i in range(10)]


for i in range(n-1):
    for j in range(1,10):
        dp[j] += dp[j-1]
print(sum(dp))
        