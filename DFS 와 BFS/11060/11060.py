import sys
from collections import deque

n = int(sys.stdin.readline())

graph = list(map(int,sys.stdin.readline().split()))
visit = [0 for _ in range(n)]

def bfs():
    queue = deque()
    queue.append(0)
    visit[0] = 1
    while queue:
        x = queue.popleft()
        for i in range(1,graph[x]+1):
            nx = x + i # 점프하는 경우의 수
            if 0 <= nx < n and visit[nx] == 0:
                visit[nx] = visit[x] + 1 # 얼마나 점프를 해서 갔는지
                queue.append(nx)

bfs()
if visit[n-1] == 0:
    print(-1)
else:
    print(visit[n-1]-1) # 처음에 1부터 시작하므로 다시 1을 빼준다.