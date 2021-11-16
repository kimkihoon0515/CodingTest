import sys
from collections import deque

f,s,g,u,d = map(int,sys.stdin.readline().split()) # F : 건물의 총 층수, S : 현재 층, G : 이동하려는 층 

graph = [0 for i in range(f)]
visit = [0 for i in range(f)]

elevator = [u,-d] # 위로 가거나 아래로 가는 경우

def bfs(x):
    queue = deque()
    queue.append(x)
    visit[x] = 1

    while queue:
        a = queue.popleft()
        for i in range(2):
            nx = a + elevator[i]
            if 0<= nx < f and visit[nx] == 0:
                visit[nx] = 1
                graph[nx] = graph[a] + 1
                queue.append(nx)

bfs(s-1)

if graph[g-1] == 0:
    if s == g:
        print(0) # 만약 출발지와 도착지가 같다면 굳이 이동할 필요가 없으므로 
    else:
        print('use the stairs')
else:
    print(graph[g-1])
