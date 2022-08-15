import sys
import heapq

n = int(sys.stdin.readline())

li = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

heap = []

for i in range(n):
    for j in range(n):
        if li[i][j] not in heap:
            heapq.heappush(heap,li[i][j])
        if len(heap) > n:
            heapq.heappop(heap)

print(heap[0])