# n=2->3,n=4->11,n=6->41,n=6->153
# n이 홀수이면 무조건 0
def solution(n):
    answer = 0
    dp = [0 for i in range(5001)]
    dp[2] = 3
    dp[4] = 11
    for i in range(6,n+1):
        if i%2!=0:
            dp[i] = 0
        else:
            dp[i] = (dp[i-2]*4 - dp[i-4])%1000000007
    answer = dp[n]
    return answer