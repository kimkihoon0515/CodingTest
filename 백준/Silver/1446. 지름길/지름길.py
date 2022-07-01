import sys

n,d = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
graph = sorted(graph,key=lambda x:(x[0],x[1],x[2]))
distance = [i for i in range(d+1)]

for i in graph:
    a,b,c = i
    if b <= d:
        distance[b] = min(distance[a]+c,distance[b])
    for j in range(a,d+1):
        distance[j] = min(distance[j-1]+1,distance[j])

print(distance[d])