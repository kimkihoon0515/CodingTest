import sys

t = int(sys.stdin.readline())


for _ in range(t):
    n = int(sys.stdin.readline())
    x = list(map(int,sys.stdin.readline().split()))
    dp = [0 for _ in range(n)]
    dp[0] = x[0]
    for i in range(1,n):
        dp[i] = max(dp[i-1]+x[i],x[i])
    print(max(dp))



