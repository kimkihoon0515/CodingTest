''' 메모리 초과 오류남 왜그런지 모르겠음.
import sys
from collections import deque,defaultdict

n,m = map(int,sys.stdin.readline().split())

graph = defaultdict(list)

for i in range(n-1):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
def bfs(i,j):
    queue = deque()
    queue.append(i)
    visit = [0 for _ in range(n+1)]
    visit[i] = 1
    
    while queue:
        x = queue.popleft()
        if x == j:
            return visit[x]
        for k,v in graph[x]:
            queue.append(k)
            visit[k] += visit[x]+v

for _ in range(m):
    start,end = map(int,sys.stdin.readline().split())
    print(bfs(start,end)-1)
'''
import sys
input = sys.stdin.readline
from collections import defaultdict,deque

def Distance(a,b):
    queue = deque()
    queue.append(a)
    visited = [False]*(N+1)
    visited[a] = True
    target_dist = [0]*(N+1)
    while queue:
        v = queue.popleft()
        if v==b:
            print(target_dist[v])
            return
        for next,dist in graph[v]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                target_dist[next] += target_dist[v] +dist
                print(queue)



N,M = map(int,input().split())
graph = defaultdict(list)


for _ in range(N-1):
    a,b,dist = map(int,input().split())
    graph[a].append((b,dist))
    graph[b].append((a,dist))

for _ in range(M):
    a,b = map(int,input().split())
    Distance(a,b)    
    