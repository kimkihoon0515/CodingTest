'''
푸는 방법을 모르겠어서 위상정렬 코드를 보고 적은 코드입니다.
'''

import sys
from collections import deque

n = int(sys.stdin.readline())

building = [[] for _ in range(n+1)] # 노드와 간선의 정보

indegree = [0 for i in range(n+1)] # 각 노드의 진입차수

cost = [0 for i in range(n+1)] # 건물 짓는데 걸리는 시간

for i in range(1,n+1):
    data = list(map(int,sys.stdin.readline().split()))[:-1]
    cost[i] = data[0]
    building_data = data[1:]
    
    for j in building_data: # 간선 연결 및 진입차수 결정
        building[j].append(i)
        indegree[i] += 1

def topology_sort(): # 위상정렬
    result = [0 for i in range(n+1)]
    queue = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        now = queue.popleft()
        result[now] += cost[now] # 선수 건물을 짓는데 걸리는 시간 + 현재 건물 짓는데 걸리는 시간
        for b in building[now]:
            indegree[b] -= 1
            result[b] = max(result[b],result[now]) # b번호 건물을 짓기 전에 먼저 지어야하는 선수 건물을 짓는데 걸리는 시간으로 갱신
            if indegree[b] == 0:
                queue.append(b)
    
    return result


answer = topology_sort()
for i in range(1,n+1):
    print(answer[i]) 
    
