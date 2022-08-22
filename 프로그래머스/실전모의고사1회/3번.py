from collections import deque

def solution(order):
    answer = 0

    main_belt = deque([i for i in range(1,len(order)+1)])
    sub_belt = []

    for i in range(len(order)):
        
        if sub_belt and sub_belt[-1] == order[i]:
            sub_belt.pop()
            answer+=1

        else:
            if not main_belt:
                break
            while main_belt:
                box = main_belt.popleft()
                if box==order[i]:
                    answer+=1
                    break
                else:
                    sub_belt.append(box)

    return answer