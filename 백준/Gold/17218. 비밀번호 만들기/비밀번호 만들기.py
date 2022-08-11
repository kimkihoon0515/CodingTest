import sys

a = sys.stdin.readline().strip()    
b = sys.stdin.readline().strip()


dp = [[0]*len(a) for _ in range(len(b))]
ans = [['' for _ in range(len(a))] for _ in range(len(b))]


# AUTABBEHNSA
# BCUAMEFKAJNA



for i in range(len(b)):
    for j in range(len(a)):
        if i == 0:
            if b[i] in a[:j+1]:
                dp[i][j] = 1
                ans[i][j] = b[i]
        else:
            if a[j] == b[i]:
                if j == 0:
                    dp[i][j] = 1
                    ans[i][j] = a[j]
                else:
                    dp[i][j] = dp[i-1][j-1]+1
                    ans[i][j] = ans[i-1][j-1] + b[i]
               
            else:
                maximum = max(dp[i-1][j],dp[i][j-1])
                dp[i][j] = maximum
                if maximum == dp[i-1][j]:
                    ans[i][j] = ans[i-1][j]
                else:
                    ans[i][j] = ans[i][j-1] 

print(ans[-1][-1])
