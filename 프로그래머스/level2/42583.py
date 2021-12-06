from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for i in range(bridge_length)]
    truck = deque(truck_weights)
    
    while bridge:
        answer +=1
        x = bridge.pop(0)
        if truck:
            if sum(bridge) + truck[0] <= weight:
                bridge.append(truck.popleft())
            else:
                bridge.append(0)
    return answer