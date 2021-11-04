import sys

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

dp = [1 for _ in range(n)] 

for i in range(1,n):
    for j in range(i):
        if li[i]>li[j]:
            dp[i] = max(dp[i],dp[j]+1)
maximum = max(dp)
print(maximum)

result = []


for i in range(n-1,-1,-1):
    if dp[i] == maximum:
        result.append(li[i])
        maximum -=1
result.reverse()

for i in result:
    print(i,end=' ')
        