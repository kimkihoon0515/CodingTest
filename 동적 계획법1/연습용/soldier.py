import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

li.reverse() # 가장 긴 증가하는 수열을 만들기 위해서 

dp = [1 for _ in range(n)] # li[i] 를 마지막 원소로 가지는 부분 수열의 길이

for i in range(1,n):
    for j in range(i):
        if li[j] < li[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(n - max(dp))