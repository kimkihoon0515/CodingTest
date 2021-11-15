import sys
from collections import deque

n = int(sys.stdin.readline())

a,b = map(int,sys.stdin.readline().split())

m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

result = [0 for i in range(n+1)]

visit = [0 for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start] = 1 # 방문했으므로

    while queue:
        x = queue.popleft()
        for i in graph[x]: 
            if visit[i] == 0: # 방문아직 안했다면
                visit[i] = 1 # 방문했다고 바꾸고
                result[i] = result[x] + 1 # 촌수를 하나씩 올린다. 연결되어있으므로
                queue.append(i) 
        
bfs(a)
if result[b] == 0 : # 연결된 촌수가 없으면 -1을 아니면 촌수를 출력
    print(-1)
else:
    print(result[b])

