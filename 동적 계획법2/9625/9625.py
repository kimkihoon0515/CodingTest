import sys

k = int(sys.stdin.readline())

dp = [0 for i in range(k+1)]

dp[0] = 1
dp[1] = 1

for i in range(2,len(dp)):
    dp[i] = dp[i-1]+dp[i-2] # 피보나치의 규칙을 따른다.

if k == 1: # 버튼을 한번 눌렀다면 B 하나만 있으므로
    print(0,1)
else: # 나머지의 경우
    print(dp[-3],dp[-2])
