import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [-1 for i in range(n+1)]

def bfs(start):
    queue=deque()
    queue.append(start)
    visit[start] = 0

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visit[i]==-1:
                queue.append(i)
                visit[i] = 0

cnt = 0

for i in range(1,n+1):
    if visit[i]==-1:
        if not graph[i]:
            cnt+=1
        else:
            bfs(i)
            cnt+=1
print(cnt)