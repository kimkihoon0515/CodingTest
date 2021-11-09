"""
import sys

n = int(sys.stdin.readline())

graph = [] 

inf = sys.maxsize

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

dp = [[0 for _ in range(3)] for _ in range(n)]
dp1 = [[0 for _ in range(3)] for _ in range(n)]

for i in range(3):
    dp[0][i] = graph[0][i]
    dp1[0][i] = graph[0][i]

for i in range(1,n):
    for j in range(3):
        if j == 0:
            dp[i][j] = graph[i][j] + min(dp[i-1][j],dp[i-1][j+1])
            dp1[i][j] = graph[i][j] + max(dp1[i-1][j],dp1[i-1][j+1])
        elif j == 1:
            dp[i][j] = graph[i][j] + min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
            dp1[i][j] = graph[i][j] + max(dp1[i-1][j-1],dp1[i-1][j],dp1[i-1][j+1])
        else:
            dp[i][j] = graph[i][j] + min(dp[i-1][j-1],dp[i-1][j])
            dp1[i][j] = graph[i][j] + max(dp1[i-1][j-1],dp1[i-1][j])

print(min(dp[n-1]),max(dp1[n-1]))
메모리 4MB라 초과함
"""
import sys

n = int(sys.stdin.readline())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dp = graph[0]
dp1 = graph[0]

for i in range(1,n):
    dp = [max(dp[0], dp[1]) + graph[i][0],max(dp[0], dp[1], dp[2]) + graph[i][1], max(dp[1], dp[2]) + graph[i][2]] 
    dp1 = [min(dp1[0], dp1[1]) + graph[i][0],min(dp1[0], dp1[1], dp1[2]) + graph[i][1], min(dp1[1], dp1[2]) + graph[i][2]]

print(max(dp),min(dp1))
