import sys
import heapq

n = int(sys.stdin.readline())
clas = []
for _ in range(n):
    s,t = map(int,sys.stdin.readline().split())
    clas.append([s,t])
    
clas = sorted(clas)

schedule = []
heapq.heappush(schedule,clas[0][1])

for i in range(1,n):
    if clas[i][0] < schedule[0]:
        heapq.heappush(schedule,clas[i][1])
    else:
        heapq.heappop(schedule)
        heapq.heappush(schedule,clas[i][1])
print(len(schedule))
        