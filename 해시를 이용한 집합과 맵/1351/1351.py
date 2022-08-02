import sys
from collections import defaultdict

n,p,q = map(int,sys.stdin.readline().split())

dp = defaultdict(int)
 
dp[0] = 1

def dfs(k):
    if dp[k]:
        return dp[k]
    else:
        dp[k] = dfs(k//p)+dfs(k//q)
        return dp[k]
dfs(n)
print(dp[n])
    