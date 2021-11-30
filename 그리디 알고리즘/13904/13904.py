'''
import sys
import heapq

n = int(sys.stdin.readline())

heap = []
hw = [0 for i in range(1001)]

for i in range(n):
    d,w = map(int,sys.stdin.readline().split())
    heap.append([-w,d,w])
heapq.heapify(heap)


while heap:
    tmp = heapq.heappop(heap)
    for i in range(tmp[1],0,-1):
        if hw[i] == 0:
            hw[i] = tmp[2]
            break

print(sum(hw))    
'''
import sys

n = int(sys.stdin.readline())
heap = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
heap.sort(reverse=True, key= lambda x: x[1])


hw = [0 for i in range(n+1)] # 그 날 끝내는 과제

for i in range(n):
    for j in range(heap[i][0]-1,-1,-1): # 역순으로 반복문을 돌려서 
        if hw[j] == 0: # 만약 그날 한 과제가 없다면
            hw[j] = heap[i][1] # 가장 점수가 높은 것 순으로 넣어준다.
            break # 반복문 탈출하고 다음 날짜로 넘어간다.
sum = 0

for i in hw:
    sum += i
print(sum) 
