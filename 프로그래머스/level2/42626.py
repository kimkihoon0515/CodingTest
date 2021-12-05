import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    #print(scoville)

    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        x = heapq.heappop(scoville) # 가장 크기가 작은 원소 
        y = heapq.heappop(scoville) # 두 번째로 크기가 작은 원소
        a = x + 2*y 
        heapq.heappush(scoville,a) # 계산해서 heap에 다시 넣어준다. 
        answer +=1
    if scoville[0] < K: # 최소 힙이 K보다 작을 경우 만족하지 않으므로 -1을 return
        answer = -1
    return answer