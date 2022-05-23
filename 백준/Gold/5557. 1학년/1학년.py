import sys

input = sys.stdin.readline

n = int(input())

li = list(map(int,input().split()))

dp = [[0 for i in range(21)] for i in range(n)]

dp[0][li[0]] = 1

for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j]:
            if 0<=j+li[i] <=20:
                dp[i][j+li[i]] += dp[i-1][j]
            if 0<=j-li[i] <= 20:
                dp[i][j-li[i]] +=dp[i-1][j]
print(dp[n-2][li[-1]])





