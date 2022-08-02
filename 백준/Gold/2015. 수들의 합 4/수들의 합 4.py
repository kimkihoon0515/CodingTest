# 풀이 참고했음
import sys

n,k = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))

dp = {0:1}
cnt = 0
summary = 0

for i in range(n):
    summary += a[i]
    if summary - k in dp:
        cnt += dp[summary-k]
    if summary in dp:
        dp[summary]+=1
    else:
        dp[summary] = 1

print(cnt)