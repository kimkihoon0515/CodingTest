import sys
 
a = sys.stdin.readline().strip()
b = sys.stdin.readlines().strip()
 
result = 0
dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            result = max(dp[i][j], result)
 
print(result)