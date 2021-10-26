import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline()) 
    if x == 0:
        try:
            print(heapq.heappop(heap)) # heapq에서 heappop은 그 중 가장 작은 원소를 pop한다.
        except:
            print(0)
    else:
        heapq.heappush(heap,x) # heappush는 원소를 넣고 크기순으로 배열한다.
