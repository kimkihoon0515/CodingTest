import sys

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

dp = [0] * 100

dp[0] = li[0]
dp[1] = max(li[0],li[1])
for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+li[i])
print(dp[n-1])