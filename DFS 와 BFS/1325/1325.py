import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n)]

for _ in range(m): # 신뢰관계의 컴퓨터를 넣는다.
    a,b = map(int,sys.stdin.readline().split())
    graph[b-1].append(a-1)

def bfs(x):
    queue = deque()
    queue.append(x)
    visit = [0 for _ in range(n)] 
    visit[x] = 1
    cnt = 1

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                queue.append(i)
    return cnt

result = []

for i in range(n): # 결과값에 bfs를 돌려서 나온 값을 넣고 최대값이면 인덱스를 출력하는식.
    result.append(bfs(i))

for i in range(n):
    if result[i] == max(result):
        print(i+1,end=' ')