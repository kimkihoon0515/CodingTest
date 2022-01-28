import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

graph = [[] for i in range(n+1)] # 다리의 체중과 연결리스트를 저장하는 배열

for _ in range(m):
    x,y,z = map(int,sys.stdin.readline().split())
    graph[x].append([y,z])
    graph[y].append([x,z])
#print(graph)
a,b = map(int,sys.stdin.readline().split()) # 시작과 끝


def bfs(weight): 
    queue = deque()
    queue.append(a)
    visit = [-1 for i in range(n+1)]
    visit[a] = 1
    
    while queue:
        x = queue.popleft()
        for end,w in graph[x]:
            if visit[end] == -1 and w >= weight: # 아직 간 적 없고 중량제한에 걸리지 않으면
                queue.append(end) 
                visit[end] = 1 # 간 것으로 갱신
    if visit[b] == -1: # 갈 수 없으면 False return
        return False
    return True


left = 0
right = 1000000000

result = 0
while left <= right:
    mid = (left+right)//2
    
    if bfs(mid): # mid를 최대 무게로 해서 넣었을 때 갈 수 있다고하면 
        result = mid 
        left = mid + 1 # 무게를 늘리는 방향으로 범위를 줄인다.
    else: # 만약 못간다고 하면
        right = mid -1 # 무게를 하나 줄이는 방향으로 범위를 줄인다.


print(result)