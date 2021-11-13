# 경로 찾기는 floyd warshall 이용
import sys

n = int(sys.stdin.readline())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
    for j in range(n):
         for i in range(n):
             if graph[j][k] and graph[k][i]:
                 graph[j][i] = 1
for i in graph:
    print(*i)