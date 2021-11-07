import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

inf = sys.maxsize

graph = [[] for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])

start,end = map(int,sys.stdin.readline().split())

dp = [inf for _ in range(n+1)]
heap = []
heapq.heappush(heap,[0,start])
dp[start] = 0

trace = [[] for _ in range(n+1)]
while heap:
    x,y = heapq.heappop(heap)

    if y == end:
        print(x)

        path = [end]
        
        while end !=start:
            path.append(trace[end])
            end = trace[end] 

        print(len(path))
        print(*reversed(path))
        break

    for next_city,cost in graph[y]:

        if dp[next_city] <=x+cost:
            continue

        dp[next_city] = x+cost
        trace[next_city] = y
        heapq.heappush(heap,[x+cost,next_city])
