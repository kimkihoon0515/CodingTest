import sys

n = int(sys.stdin.readline())
box = list(map(int,sys.stdin.readline().split()))

dp = [1 for i in range(n)] # 무조건 상자 1개이상은 들어가므로 1로 초기화

for i in range(n):
    for j in range(i):
        if box[i]> box[j]: # 앞의 상자가 뒤쪽 상자보다 크기가 크면 
            dp[i] = max(dp[i],dp[j]+1) # 상자의 수를 한 개 더하고 그 값을 기존 dp값과 비교하여 큰 값으로 치환해준다.
print(max(dp)) 