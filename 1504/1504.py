import heapq
import sys
input = sys.stdin.readline
inf = sys.maxsize

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 방향성 없는 그래프이므로 a, y일 때와 b, x일 때 모두 추가
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    distance = [inf] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            c = dist + i[1]

            if distance[i[0]] > c:
                distance[i[0]] = c
                heapq.heappush(q, (c, i[0]))

    # 반환값은 최단 거리 배열
    return distance


v1, v2 = map(int, input().split())

# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)
print(result if result < inf else -1)