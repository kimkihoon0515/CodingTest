import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

dp = [1 for i in range(n)] # 감소하는 배열의 길이

for i in range(1,n):
    ans = []
    for j in range(i):
        if a[i] < a[j]: # i번보다 j번째가 더 크다면 30 10 이런식이되므로 크면 집어넣는 식으로 한다.
            ans.append(dp[j]) 
    if not ans: # ans배열이 비어있다면 넘어간다.
        continue
    else: # ans 배열이 채워져있다면 감소하는 배열이 존재하므로 
        dp[i] += max(ans) # i번째 dp를 ans의 값중 가장 큰 값을 더해줘서 감소하는배열의 길이를 증가시킨다.
print(max(dp))