import sys

inf = sys.maxsize

n,m = map(int,sys.stdin.readline().split())

graph = [[inf for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0
        

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int,sys.stdin.readline().split()) # k번 회사를 x번 거쳐가는 최소 이동시간

for k in range(1,n+1): # floyd warshall 알고리즘
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

dist = graph[1][k] + graph[k][x]

print(dist)

