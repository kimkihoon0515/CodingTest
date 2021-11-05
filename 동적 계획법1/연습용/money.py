import sys

n,m = map(int,sys.stdin.readline().split())

li = [int(input()) for _ in range(n)]

inf = sys.maxsize
dp = [inf] * (m+1)
dp[0] = 0
for i in range(n): # i는 화폐 단위를 의미하고
    for j in range(li[i],m+1): # j는 금액을 의미한다. 해당 금액인 li[i] 부터 m원까지를 확인한다.
        if dp[j-li[i]] != inf: # 현재 금액에서 현재 확인하고있는 화폐 단위의 금액을 뺸 것을 만들 수 있다면
            dp[j] = min(dp[j],dp[j-li[i]]+1) # 점화식 계속 최소값으로 갱신되는 방식

if dp[m] == inf:
    print(-1)
else:
    print(dp[m])