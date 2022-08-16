# 피로도는 남은 일의 작업량을 제곱하여 더한 것
import heapq

def solution(n, works):
    answer = 0
    if n >= sum(works):
        return 0
    
    works = [-i for i in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i+=1
        heapq.heappush(works,i)
    for i in works:
        answer +=i**2
    return answer