import sys
from collections import deque

def dfs(s):
    queue = deque()
    queue.append(s)
    visit[s] = 1
    cnt = 0 # 비행기를 탄 횟수
    
    while queue:
        x = queue.popleft()
        for i in graph[x]: # 비행기를 타고 갈 수 있는 곳 중에서
            if visit[i] == 0: # 방문안했으면 
                visit[i] = 1 # 방문한 것으로 갱신하고
                queue.append(i)
                cnt +=1 # 비행기 탄 횟수 1증가
    return cnt
        
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visit = [0 for i in range(n+1)]
    print(dfs(1))
    
       