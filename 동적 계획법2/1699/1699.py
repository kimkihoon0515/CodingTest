import sys

n = int(sys.stdin.readline())

dp = [0 for i in range(n+1)]
num = [i*i for i in range(1,100000) if i*i < 100000] # 범위 내 모든 제곱수

for i in range(1,n+1):
    ans = []
    for j in num: # i보다 작은 제곱수들을 찾는다.
        if j > i:
            break
        ans.append(dp[i-j]) # i보다 작은 제곱수들을 뺀 dp 값들을 전부 ans에 넣어준다.
    dp[i] = min(ans) + 1 # 그 중에 가장 작은것 + 1 이 i번째 dp값이다.
print(dp[n])