d,k = map(int,input().split())

dp = [0 for i in range(d)]
dp[0],dp[1] = 1,1

while(True):
    for i in range(2,d):
        dp[i] = dp[i-1]+dp[i-2]
    
    if dp[d-1] == k:
        print(dp[0],dp[1],sep="\n")
        break
    elif dp[-1] > k:
        dp[0] += 1
        dp[1] = dp[0]
    else:
        dp[1] += 1