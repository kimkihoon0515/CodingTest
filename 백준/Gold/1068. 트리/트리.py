import sys

n = int(sys.stdin.readline())

graph = list(map(int,sys.stdin.readline().split()))

k = int(sys.stdin.readline())

def dfs(k,graph):
    graph[k] = -2 # 삭제
    for i in range(len(graph)):
        if k == graph[i]: # 삭제한 노드를 부모노드로 다시 dfs
            dfs(i,graph)

dfs(k,graph)
cnt = 0

for i in range(len(graph)):
    if graph[i]!= -2 and i not in graph: # 삭제될 노드, 다른 노드의 부모노드가 아닌 것
        cnt +=1
print(cnt)