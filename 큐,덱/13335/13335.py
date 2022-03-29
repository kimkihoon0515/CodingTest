import sys
from collections import deque

n,w,l = map(int,sys.stdin.readline().split()) # n개의 트럭, 다리위에 w대, 최대 하중 l

trucks = deque(map(int,sys.stdin.readline().split()))

bridge = [0 for i in range(w)]


time = 0

while trucks:
    time +=1 
    x = bridge.pop(0)
    
    if trucks: 
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)

print(time+w)