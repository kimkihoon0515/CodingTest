import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n,m = map(int,sys.stdin.readline().split()) # 3,4
    li = list(map(int,sys.stdin.readline().split())) # 1 3 3 2 2 1 4 1 0 6 4 7

    dp = []
    index = 0
    for i in range(n):
        dp.append(li[index:index+m])
        index += m
    #print(dp)

    for j in range(1,m):
        for i in range(n): # 모든 행 위치에 대해서
            if i == 0: # 왼쪽 위
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1: # 왼쪽 아래
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            left = dp[i][j-1] # 왼쪽
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)
    result = 0
    for i in range(n):
        result = max(result,dp[i][m-1])
    print(result)
            