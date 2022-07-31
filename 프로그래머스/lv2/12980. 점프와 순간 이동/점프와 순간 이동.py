''' 시간초과..
def solution(n):
    ans = 0
    if n<2:
        return 1
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3,n+1):
        if (i==(i&-i)):
            dp[i] = 1
        elif i%2 == 0:
            dp[i] = dp[i//2]
        else:
            dp[i] = dp[(i-1)//2]+1
    ans = dp[-1]
    return ans
'''
def solution(n):
    ans = 0
    while n>0:
        if n%2 == 1:
            ans+=1
        n=n//2

    return ans