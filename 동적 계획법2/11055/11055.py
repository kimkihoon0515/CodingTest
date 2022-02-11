import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
dp = [0 for i in range(n)] # 각 자리에 올 수 있는 가장 큰 수
dp[0] = a[0] 

for i in range(1,n):
    ans = []
    for j in range(i-1,-1,-1): # i부터 역순으로 진행
        if a[i] > a[j]: # 작으면 넣는다. 그래야 가장 길게 증가하는 식으로 쌓이기 때문
            ans.append(dp[j])
    if not ans:
        dp[i] = a[i]
    else:
        dp[i] = a[i]+ max(ans) 
print(dp)
print(max(dp))