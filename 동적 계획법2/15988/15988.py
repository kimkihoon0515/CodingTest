import sys

t = int(sys.stdin.readline())

dp = [0 for i in range(1000001)]
dp[0] = 1 
dp[1] = 1
dp[2] = 2
for i in range(3,1000001):
    dp[i] = (dp[i-3]+dp[i-2]+dp[i-1])%1000000009 # 점화식

for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])

    