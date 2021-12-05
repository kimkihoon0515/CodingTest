from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append([i,priorities[i]]) # 인덱스,우선순위
        
    while len(queue) != 0:
        if max(priorities) > queue[0][1]:
            queue.append(queue[0])
            queue.popleft()
        else:
            if location == queue[0][0]:
                return answer+1 # 하나 증가시켜준다.
            priorities[queue[0][0]] = 0 # 출력했으므로 그것의 우선순위 초기화
            queue.popleft() # 출력
            answer +=1 # 횟수 1 증가
    return answer