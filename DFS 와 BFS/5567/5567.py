import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

def bfs(x):
    queue = deque()
    queue.append(x)
    visit[x] = 1 # 시작 지점
    while queue:
        a = queue.popleft()
        for i in range(1,n+1): 
            if visit[i] == 0 and graph[a][i] == 1:
                visit[i] = visit[a] + 1 # 친구사이인지 친구의 친구인지 아니면 그 너머인지 판별하기 위해
                queue.append(i)

bfs(1)
cnt = 0 # 결과값
for i in range(2,n+1):
    if visit[i] < 4 and visit[i] != 0: # 친구사이 : 2 친구의 친구사이 : 3 
        cnt +=1
print(cnt)