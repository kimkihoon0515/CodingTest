import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

parent = [0] * (n+1)

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if parent[i] == 0: # bfs에서 탐색이 안된 것이므로 부모노드라는 뜻
                parent[i] = x # 그 부모노드의 부모노드를 찾기 위해 x로 둔다.
                queue.append(i)
    return parent

bfs()

for i in range(2,len(parent)):
    print(parent[i])