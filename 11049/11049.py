import sys

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(list(map(int,sys.stdin.readline().split())))

dp=[[0 for _ in range(n)] for _ in range(n)]

for i in range(1,n):
    for j in range(0,n-i):
        if i == 1:
            dp[j][j+i] = li[j][0] * li[j][1] * li[j+i][1]
            continue
        dp[j][j+i] = 2**32
        for k in range(j,j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k]+dp[k+1][j+i]+li[j][0] * li[k][1] * li[j+i][1])

print(dp[0][n-1])