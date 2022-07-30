import sys

n = int(sys.stdin.readline())

def fib(n):
    dp = [1,1]
    for i in range(n-2):
        tmp = dp[1]
        dp[1] = dp[0]+dp[1]
        dp[0] = tmp
    return dp[0]+dp[1]

print(fib(n+1)*2)