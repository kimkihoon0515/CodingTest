import sys
import heapq

n = int(input())  

li = []

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    li.append((a,b))

li.sort()

queue = []

for i in range(n):
    heapq.heappush(queue,li[i][1])
    if li[i][0] < len(queue): # deadline 보다 queue의 길이가 더 큰 경우 pop 한다.
        heapq.heappop(queue)
print(sum(queue))