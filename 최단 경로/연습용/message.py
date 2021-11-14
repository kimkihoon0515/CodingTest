import sys
import heapq

n,m,c = map(int,sys.stdin.readline().split())

inf = sys.maxsize

graph = [[] for _ in range(n+1)]

distance = [inf] * (n+1)

for _ in range(m):
    x,y,z = map(int,sys.stdin.readline().split())
    graph[x].append((y,z))

def dijkstra(c):
    queue = []
    heapq.heappush(queue,(0,c)) # 큐에다가 시작 노드를 0으로 만들어서 삽입한다.
    distance[c] = 0 # 시작노드까지의 거리는 0으로 초기화

    while queue: 
        dist,now = heapq.heappop(queue) 
        if distance[now] < dist: 
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))

dijkstra(c)

cnt = 0 # 탐색 가능한 노드의 개수

result = [] # 최대값 저장을 위한 배열

for i in distance:
    if i != inf:
        cnt += 1
        result.append(i)

print(cnt-1,max(result)) # 시작노드제외

