import sys

n = int(sys.stdin.readline())

num = list(map(int,sys.stdin.readline().split()))

dp = [1 for i in range(n)] # 감소하는 dp
dp1 = [1 for i in range(n)] # 증가하는 dp

for i in range(1,n):
    if num[i]<=num[i-1]:
        dp[i] = max(dp[i],dp[i-1]+1) # 길이 1개 증가시킴.
    if num[i]>= num[i-1]:
        dp1[i] = max(dp1[i],dp1[i-1]+1) # 길이 1개 증가시킴.

print(max(max(dp),max(dp1))) # 두 길이 중 최대값 출력