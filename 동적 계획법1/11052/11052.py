import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

dp = [0] * (n+1)
dp[1] = li[0]
dp[2] = max(2*dp[1],li[1])

for i in range(3,n+1):
    dp[i] = li[i-1] # 자기 자신
    for j in range(1,i-j):
        dp[i] = max(dp[i],dp[j]+dp[i-j])

print(dp[n])
    