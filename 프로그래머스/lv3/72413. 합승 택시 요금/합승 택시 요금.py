import sys,heapq
def dijkstra(n,graph,s):
    distance = [sys.maxsize for _ in range(n+1)]
    distance[s] = 0
    
    queue = []
    heapq.heappush(queue,(0,s))
    
    while queue:
        dist,now = heapq.heappop(queue)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = distance[now] + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))
    return distance

def solution(n, s, a, b, fares):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    
    for i in fares:
        e,f,g = i
        graph[e].append((f,g))
        graph[f].append((e,g))
    
    distance = dijkstra(n,graph,s)
    print(distance)
    result = distance[a]+distance[b]
    
    for i in range(1,n+1):
        if i == s or result <= distance[i]:
            continue
        else:
            dist = dijkstra(n,graph,i)
            result = min(result,distance[i]+dist[a]+dist[b])
    answer = result
    return answer