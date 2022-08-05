from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        x = queue.popleft()
        cnt = 0
        for price in queue:
            if x>price:
                cnt+=1
                break
            else:
                cnt+=1
        answer.append(cnt)
    return answer