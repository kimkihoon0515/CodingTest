def solution(n):
    answer = 0
    dp = [1,1]
    if n == 0:
        return 0
    for _ in range(n-1):
        tmp = dp[1]
        dp[1] = dp[0]+dp[1]
        dp[0] = tmp
    return dp[1]%1234567
