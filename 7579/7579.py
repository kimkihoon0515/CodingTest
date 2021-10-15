import sys

n,m = map(int,sys.stdin.readline().split()) # m 바이트의 메모리를 확보해야한다.

a = list(map(int,sys.stdin.readline().split())) # 활성화 되어있는 앱의 메모리 사용량
# 30 10 20 35 40
b = list(map(int,sys.stdin.readline().split())) # 비활성화 시 발생비용
# 3 0 3 5 4

maximum = sum(b)+1 # 최고 비용에다가 1을 더해서 배열의 길이를 정해놓는다.

dp = [[0] *maximum for _ in range(n+1)] # dp배열을 만들어놓는다.
min = maximum

for i in range(1,n+1): # 첫번째 줄은 전부 0이고 그 뒤에줄부터 생각해야한다.
    for j in range(len(dp[0])): # 가로줄의 길이만큼 비교한다. 
        if j < b[i-1]: # 현현재 앱을 비활성화할만큼 cost가 충분하지 않은 경우에
            dp[i][j] = dp[i-1][j]
        else: # 같은 비용 내에서 현재 앱을 끈 뒤와 끄지 않은 비용것을 비교한다.
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-b[i-1]]+a[i-1])
        if dp[i][j] >= m and min > j: # 조건에 맞으면 출력한다.
            min = j

print(min)

