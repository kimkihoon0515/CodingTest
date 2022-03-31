import sys

n = int(sys.stdin.readline())

dp = [0 for i in range(n)]

if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n):
        dp[i] = dp[i-2]+ dp[i-1]

    print(dp[-1]) 