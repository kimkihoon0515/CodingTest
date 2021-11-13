import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue = deque()
    result = 0 # 연결 요소의 개수
    for i in range(1,n+1):
        if visit[i] == 0: # 방문한 적 없으면 
            visit[i] = 1 # 방문했다고하고
            queue.append(i) # queue에 넣어줌
            result += 1 
            while queue:
                x = queue.popleft() 
                for i in graph[x]: # 연결요소 있는지 검사하는 것
                    if visit[i] == 0:
                        visit[i] = 1
                        queue.append(i)
    print(result)

bfs()
