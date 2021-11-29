''' heapq를 사용하지 않으면 내가 직점 sort를 통해서 정렬을 해줘야 하는데 이 경우 시간초과가 발생함. list.sort()는 O(NlogN)의 시간복잡도가 발생하기 때문에 시간초과 발생.
import sys 

n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]

result = []
if len(li) == 1:
    print(*li)
    exit(0)
while True:
    if len(li) < 2:
        break
    li.sort(reverse=True)
    x = li.pop()
    y = li.pop()
    li.append(x+y)
    result.append(x+y)

sum = 0
for i in result:
    sum += i
print(sum)
'''
import sys
import heapq # O(logN)의 시간복잡도를 가짐

n = int(sys.stdin.readline())

heap = []

for _ in range(n):
    heapq.heappush(heap,int(sys.stdin.readline())) # heapq는 오름차순으로 정렬된다.
print(heap)


if len(heap) == 1:
    print(0)
    exit(0)
else:
    sum = 0
    while len(heap) > 1:
        x = heapq.heappop(heap) # 가장 작은 값 2개를 추출한다.
        y = heapq.heappop(heap)
        sum += x+y # 추출된 2개의 합을 계속해서 누적합계로 구해준다.
        heapq.heappush(heap,x+y) # 추출된 2개는 새로운 덱으로 합쳐지므로 그것을 다시 heap에 넣어 오름차순정렬을 해준다.
print(sum)
