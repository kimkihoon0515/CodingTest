from collections import deque

def solution(queue1, queue2):
    answer = 0
    target = (sum(queue1)+sum(queue2)) // 2

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    left = sum(queue1)
    right = sum(queue2)
    tmp = 0
    
    flag = False
    
    while queue1 and queue2:
        if left < target:
            tmp = queue2.popleft()
            left+=tmp
            queue1.append(tmp)
            answer+=1
            
        elif left > target:
            tmp = queue1.popleft()
            left -= tmp
            answer+=1
            
        else:
            flag = True
            break
    if flag:
        return answer
    else:
        return -1
