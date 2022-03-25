import sys

n = int(sys.stdin.readline())
p = [0]+ list(map(int,sys.stdin.readline().split())) # dp와의 배열 시작점을 맞춰주기위해 0을 앞에 더해준다.

dp = [(sys.maxsize) for i in range(1001)]
dp[0] = 0 # dp[0]을 0으로 초기화

for i in range(1,n+1): # 1부터 시작한다.
    for j in range(i+1): 
        dp[i] = min(dp[i],p[j]+dp[i-j]) # 카드 i개 구매하는 최대 비용과 j번째 카드팩 + dp[i-j]를 더한 값중 최소값으로 dp를 최신화
        
print(dp[n])