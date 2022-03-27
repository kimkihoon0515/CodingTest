import heapq
import sys

n,k = map(int,sys.stdin.readline().split())

jewel = []

for _ in range(n):
    m,v = map(int,sys.stdin.readline().split()) # m : 무게, v : 가격
    jewel.append([m,v])

bag = []

for _ in range(k):
    c = int(sys.stdin.readline().strip())
    bag.append(c)

jewel = sorted(jewel) # 정렬
bag = sorted(bag)

result = 0
heap=[]

for i in bag:
    while jewel and i >= jewel[0][0]: # 가방의 무게가 보석의 무게보다 크면
        heapq.heappush(heap,-jewel[0][1]) # 가장 큰 보석의 무게가 heap에 들어간다.
        heapq.heappop(jewel)
        
    if heap: # 가방에 넣을 수 있으면
        result += heapq.heappop(heap) 
    elif not jewel:
        break
print(-result)