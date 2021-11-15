import sys

n,m = map(int,sys.stdin.readline().split())

graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            elif graph[a][k] and graph[k][b]:
                if graph[a][b] == 0:
                    graph[a][b] = graph[a][k] + graph[k][b]
                else:
                    graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

result = sys.maxsize

for i in range(n):
    sum = 0
    for j in range(n):
        sum += graph[i][j]
    if result > sum:
        result = sum
        answer = i
print(answer+1)