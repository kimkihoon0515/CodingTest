import sys

n = int(sys.stdin.readline())

li = []

for _ in range(n):
    t,p = map(int,sys.stdin.readline().split())
    li.append((t,p))

dp = [0 for _ in range(n+1)]

for i in range(n-1,-1,-1):
    if li[i][0] + i >n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(li[i][1]+dp[i+li[i][0]],dp[i+1])

print(max(dp))
    