import sys

inf = sys.maxsize

v,e = map(int,sys.stdin.readline().split())

graph = [[inf for _ in range(v+1)] for _ in range(v+1)] # 그래프를 inf 로 초기화

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = c

for k in range(1,v+1): # floyd warshall 알고리즘
    for j in range(1,v+1):
        for i in range(1,v+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

result = inf
for i in range(1,v+1): # 최소 사이클 찾는다.
    result = min(result,graph[i][i])


if result == inf:
    print(-1)
else:
    print(result)

