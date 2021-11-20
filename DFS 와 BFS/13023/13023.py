import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())


graph = [[] for _ in range(n)]
visit = [0 for i in range(n)] 


for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(cnt,num):
    if num == 4: # 만약 조건을 만족하면 1을 출력하고종료
        print(1)
        exit(0)
    for i in graph[cnt]: # dfs로 탐색을 하는과정
        if visit[i] == 0: # 방문 안했다면 했다고 하고 dfs로 재귀 탐색
            visit[i] = 1
            dfs(i,num+1)
            visit[i] = 0 # 다시 방문 안한 것으로 만든다.

for i in range(n): # 사람 1명씩 차례로
    visit[i] = 1
    dfs(i,0) # dfs 로 탐색한다.
    visit[i] = 0

print(0) # 조건 맞지 않게 된 것이므로 0을 출력한다.

