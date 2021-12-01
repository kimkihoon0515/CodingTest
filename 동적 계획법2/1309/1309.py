import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n+2)]

dp[1] = 3
dp[2] = 7

for i in range(2,n):
    dp[i+1] = (2 * dp[i] + dp[i-1]) % 9901 # 점화식인데 결과값에서 9901을 나누면 메모리 초과가 나므로 점화식에서 나눠줘서 숫자를 줄여준다.
print(dp[n])