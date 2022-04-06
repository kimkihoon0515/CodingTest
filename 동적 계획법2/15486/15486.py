import sys

n = int(sys.stdin.readline().strip())

t = []
p = []

for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    t.append(a)
    p.append(b)

print(t,p)

dp = [0 for i in range(n+1)]

maximum = 0

for i in range(len(t)):
    maximum = max(maximum,dp[i])
    if i + t[i] <= n: # 상담이 끝나는 날이 n보다 적어도 같은경우까지만 적용
        dp[i+t[i]] = max(maximum+p[i],dp[i+t[i]]) # 현재까지의 수익에 이번 상담의 수익을 더한값, 오늘 상담이 끝나는 시점의 수익 중 큰 값
print(max(dp))