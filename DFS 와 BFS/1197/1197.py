"""
prim MST 알고리즘
시작 정점으로부터 현재의 신장 트리에 연결된 간선 중 가장 작은 가중치를 가진 간선을 선택해서 정점을 확장해 나가는 방식
1. 시작 정점을 기준으로 시작 정점에서 연결된 간선 중 가장 작은 가중치를 가진 간선으로 다음 정점과 연결한다.
2. 추가된 정점을 포함하여 다시 한번 가장 작은 가중치를 가진 간선을 선택하여 정점을 연결한다.
3. 간선의 개수가 n-1 개가 될 때까지 반복한다.
"""
import sys
import heapq # 최소값만 중요한 상황이므로 heapq를 통해 문제 해결

v,e = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(v+1)]
visit = [0 for i in range(v+1)] 

queue = [[0,1]] # 정점이 1이고 가중치가 0인 시작지점

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

ans,cnt = 0,0

while queue:
    if cnt == v:
        break
    w,s = heapq.heappop(queue) # w : 가중치, s : 정점
    if visit[s] == 0:
        visit[s] = 1
        ans += w
        cnt += 1
        for i in graph[s]: 
            heapq.heappush(queue,i)

print(ans)