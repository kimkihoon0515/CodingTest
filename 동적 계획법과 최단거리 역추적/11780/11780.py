import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = sys.maxsize
graph = [[[] for _ in range(n+1)] for _ in range(n+1)]
dp = [[inf] * (n+1) for _ in range(n+1)]

for _ in range(m):
	a, b, c = map(int,sys.stdin.readline().split())
	dp[a][b] = min(dp[a][b], c)
	graph[a][b] = [a, b]
 
for k in range(1, n+1): # floyd warshall 알고리즘
	for i in range(1, n+1):
		for j in range(1, n+1):
			if i != j:
				if dp[i][j] > dp[i][k] + dp[k][j]:
					dp[i][j] = dp[i][k] + dp[k][j]
					graph[i][j] = graph[i][k][:-1] + graph[k][j]
 
for i in dp[1:]:
	for j in i[1:]:
		print(0 if j == inf else j, end = ' ')
	print()

for i in range(1, n+1):
	for j in range(1, n+1):
		if dp[i][j] == inf or i == j: # 갈 수 없는 경로
			print(0)
		else:
			print(len(graph[i][j]), *graph[i][j])