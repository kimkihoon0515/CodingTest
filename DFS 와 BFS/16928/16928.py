import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())


graph = [i for i in range(101)]

for _ in range(n): # graph에 사다리와 뱀을 그래프에 입력해넣는다.
    a,b = map(int,sys.stdin.readline().split())
    graph[a] = b
    
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a] = b

visit = [-1 for i in range(101)]

def bfs(s):
    queue = deque([1])
    visit[s] = 0
    while queue:
        x = queue.popleft()
        for i in range(1,7):
            nx = x + i # 주사위를 굴려서 이동하는 발판
            if nx > 100:
                continue
            node = graph[nx] # 주사위를 굴려서 이동하게 되는 그래프의 칸
            if visit[node] == -1: # 방문한 적이없다면
                queue.append(node)
                visit[node] = visit[x] + 1 # +1씩 증가시킨다.
                if node == 100: # 100에 도달하면 도착한 것이므로 끝낸다.
                    return
                           
bfs(1)
print(visit[-1])