import sys

n,k = map(int,sys.stdin.readline().split())

coin = list(int(sys.stdin.readline().strip()) for _ in range(n))

dp = [0 for i in range(k+1)]

for i in range(1,k+1):
    ans=[]
    for j in coin:
        if j <=i and dp[i-j] != -1:
            ans.append(dp[i-j])
    if not ans:
        dp[i] = -1
    else:
        dp[i] = min(ans) + 1
print(dp[k])