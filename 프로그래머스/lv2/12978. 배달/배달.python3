import heapq


def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def solution(N, roads, K):
    answer = 0
    INF = int(1e9)

    graph = [[] for _ in range(N + 1)]
    distances = [INF] * (N + 1)

    for road in roads:
        a, b, c = road
        graph[a].append((b, c))
        graph[b].append((a, c))

    dijkstra(1, graph, distances)

    for distance in distances:
        if distance <= K:
            answer += 1

    return answer