import sys
from collections import deque

n,m,k,x = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visit = [-1 for i in range(n+1)]
def dfs(s):
    queue = deque()
    queue.append(s)
    visit[s] = 0
    
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visit[i] == -1:
                queue.append(i)
                visit[i] = visit[x]+1

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

dfs(x)
if k not in visit:
    print(-1)
else:
    for i in range(n+1):
        if visit[i] == k:
            print(i)
