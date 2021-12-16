import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visit = [-1 for i in range(n+1)]
result = []
def dfs(s):
    queue = deque()
    queue.append(s)
    visit[s] = 0
    
    while queue:
        x = queue.popleft()
        
        for i in graph[x]:
            if visit[i] == -1:
                visit[i] = visit[x] + 1
                queue.append(i)
                result.append([i,visit[i]]) # 도시의 번호와 거리를 결과배열에 저장
    return result
    

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs(1)
result = sorted(result,reverse=True,key=lambda x: (x[1],-x[0])) # 거리가 먼 순으로, 헛간의 번호는 작은 순서대로 정렬한다.
ans = [k for k,v in result if v == max(visit)] # 거리가 가장 긴 곳에 위치한 헛간들만 따로 뺀다.
print(*result[0],len(ans)) # 출력