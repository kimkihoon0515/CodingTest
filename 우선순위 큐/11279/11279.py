""" 시간초과 발생하므로 heapq 사용해서 구현해야함.
import sys

n = int(sys.stdin.readline())
heap=[]
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(max(heap))
            heap.remove(max(heap))
    else:
        heap.append(x)
"""        
import sys
import heapq

n = int(sys.stdin.readline())
heap=[]

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,(-x))