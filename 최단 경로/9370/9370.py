import sys
import heapq
inf = sys.maxsize

def dijkstra(start):
    distance = [inf] * (n + 1)
    queue = []
    # 시작 노드로 가기 위한 최단 경로를 0으로 설정하여 큐에 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(queue)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시한다.
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드를 확인한다.
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신한다.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance

T = int(sys.stdin.readline())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(n + 1)]
    target = []
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        # 양방향 간선 처리
        graph[a].append((b, d))
        graph[b].append((a, d))
    for _ in range(t):
        target.append(int(sys.stdin.readline()))

    dis_s = dijkstra(s)
    dis_g = dijkstra(g)
    dis_h = dijkstra(h)
    result = []
    for i in target:
        if dis_s[g]+dis_g[h]+dis_h[i] == dis_s[i] or dis_s[h] + dis_h[g] + dis_g[i] == dis_s[i]:
            result.append(i)
    result.sort()
    for i in result:
        print(i, end=' ')
    print()