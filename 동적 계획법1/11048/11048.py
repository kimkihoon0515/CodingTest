import sys

n,m = map(int,sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split()))) # 사탕이 놓여있는 것을 표현
    
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = graph[i-1][j-1] + max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) # 새로운 dp는 왼쪽,위,대각선 으로부터 갱신되므로 그것들 중 최대값으로 갱신
print(max(max(dp)))